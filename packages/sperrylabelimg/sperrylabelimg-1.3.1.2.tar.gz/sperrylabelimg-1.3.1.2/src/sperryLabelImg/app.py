#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import codecs
# import distutils.spawn
import os.path
import platform
# import re.
# import sys
# import subprocess
import shutil
import webbrowser as wb
import logging
from datetime import time

from functools import partial
from re import split
from typing import List

# from collections import defaultdict

try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    # needed for py3+qt4
    # Ref:
    # http://pyqt.sourceforge.net/Docs/PyQt4/incompatible_apis.html
    # http://stackoverflow.com/questions/21217399/pyqt4-qtcore-qvariant-object-instead-of-a-string
    # from PyQt4.QtGui import *
    # from PyQt4.QtCore import *
    pass
from pathlib import Path
from libs.combobox import ComboBox  # noqa
from libs.resources import *  # noqa (VERY IMPORTANT LINE, IMPORTING LINE CAUSES LIBS STRING BUNDLE TO LOAD PROPERLY)
from libs.constants import *  # noqa
from libs.utils import *  # noqa
from libs.settings import Settings  # noqa
from libs.shape import Shape, DEFAULT_LINE_COLOR, DEFAULT_FILL_COLOR  # noqa
from libs.stringBundle import StringBundle  # noqa
from libs.canvas import Canvas  # noqa
from libs.zoomWidget import ZoomWidget  # noqa
from libs.labelDialog import LabelDialog  # noqa
from libs.colorDialog import ColorDialog  # noqa
from libs.labelFile import LabelFile, LabelFileError, LabelFileFormat  # noqa
from libs.toolBar import ToolBar  # noqa
from libs.pascal_voc_io import PascalVocReader  # noqa
from libs.pascal_voc_io import XML_EXT  # noqa
from libs.yolo_io import YoloReader  # noqa
from libs.yolo_io import TXT_EXT  # noqa
from libs.create_ml_io import CreateMLReader  # noqa
from libs.create_ml_io import JSON_EXT  # noqa
from libs.ustr import ustr  # noqa
from libs.hashableQListWidgetItem import HashableQListWidgetItem  # noqa

import re
from collections import defaultdict
from functools import wraps

__appname__ = 'Sperry Label Img'

logger = logging.getLogger("main")
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

image_name_pattern = r'.*\d{3}_DF\d{6}_\d{3}_\d_\d+.*\.png'
pulse_count_pattern = r'.*\d{3}_DF\d{6}_\d{3}_\d_(\d+).*\.png'
rail_pattern = r'.*\d{3}_DF\d{6}_\d{3}_(\d)_\d+.*\.png'
datasource_pattern = r'.*(\d{3}_DF\d{6}_\d{3})_\d_\d+.*\.png'

ELMER_EXT = "_elmer.png"

move_image_icon_path = Path(__file__).parent.parent / "resources/folder-move.svg"

# Added button strings (these convert buttons not in the pyqt library into button names)
# this is required because any buttons not recognized in StringBundle will cause an error,
# so they need to be added here

additional_button_names = {
    "openMultipleDirs": "Open Multiple\nDirs",
    "setActiveDir": "Set Active Dir",
    "moveImage": "Move Image",
}


class FileListWidgetEventFilter(QObject):

    def eventFilter(self, obj, event):
        if isinstance(obj, QListWidget):
            if event.type() in [QEvent.MouseButtonPress, QEvent.MouseButtonRelease, QEvent.MouseButtonDblClick]:
                item = obj.itemAt(event.pos())
                if item and not item.flags() & Qt.ItemIsEnabled:
                    return True  # Consume the event
        return super().eventFilter(obj, event)


class IndentDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(IndentDelegate, self).__init__(parent)
        self.base_indent = 20  # Base indent for all items
        self.indent_step = 20  # Additional indent for each level

    def paint(self, painter, option, index):
        indent = self.get_indent(index)
        option.rect.setLeft(option.rect.left() + indent)
        super(IndentDelegate, self).paint(painter, option, index)

    def sizeHint(self, option, index):
        size = super(IndentDelegate, self).sizeHint(option, index)
        indent = self.get_indent(index)
        size.setWidth(size.width() + indent)
        return size

    def get_indent(self, index):
        # Get the text of the item
        text = index.data(Qt.DisplayRole)
        # Calculate indent based on the number of path separators
        level = 0 if text.count("~") >= 1 else 1
        return self.base_indent + (level * self.indent_step)


class WindowMixin(object):

    def menu(self, title, actions=None):
        menu = self.menuBar().addMenu(title)  # noqa
        if actions:
            add_actions(menu, actions)
        return menu

    def toolbar(self, title, actions=None):
        toolbar = ToolBar(title)
        toolbar.setObjectName(u'%sToolBar' % title)
        # toolbar.setOrientation(Qt.Vertical)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        if actions:
            add_actions(toolbar, actions)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)  # noqa
        return toolbar


def queue_event(function):
    QTimer.singleShot(0, function)  # noqa


def scan_for_images(folder_path):
    extensions = ['.%s' % fmt.data().decode("ascii").lower() for fmt in QImageReader.supportedImageFormats()]  # noqa
    images = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:

            if not file.lower().endswith(tuple(extensions)):
                continue
            if "_elmer" in file.lower():
                continue

            relative_path = os.path.join(root, file)
            path = ustr(Path(relative_path).as_posix())  # noqa
            images.append(path)

    natural_sort(images, key=lambda x: x.lower())
    return images


def calculate_rel_cur_active_dir_msg(cur_active_dir, com_dir_path) -> str:
    """
    Calculate the relative path from `com_dir_path` to `cur_active_dir`
    and then format it into a string to be used as a window title.

    :param cur_active_dir: The current active directory.
    :param com_dir_path: The common directory of all active directories.
    :return: The window title.
    """
    rel_cur_active_dir = cur_active_dir.relative_to(com_dir_path)
    rel_cur_active_dir_msg = f"Active Directories  (SAVE TO) >>  {rel_cur_active_dir.as_posix()}"
    return rel_cur_active_dir_msg


def calculate_com_dir_path(active_dirs):
    """
    finds the most common directory amongst the active directories
    :return:
    """
    com_dir_path = Path(os.path.commonpath(active_dirs))
    is_a_true_parent_dir = False
    while is_a_true_parent_dir is False:
        if com_dir_path in active_dirs:
            com_dir_path = com_dir_path.parent
        else:
            is_a_true_parent_dir = True

    return com_dir_path


def create_container_folder_item(com_dir_path: Path):
    """
    calculates the relative path of the common directory from the home path
    and then format it into a string to be used for a container-folder's text

    :keyword common directory: common directory of all the active directories.

    :param com_dir_path: common directory of all the active directories.
    :return: text for a container folder
    """
    container_name = com_dir_path.relative_to(Path.home())
    container_name = '~' / container_name
    container_name = container_name.as_posix()
    container_name = f"📂 {container_name}"
    container_item = QListWidgetItem(container_name)
    container_item.setFlags(container_item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEnabled)
    return container_item


def create_active_dir_item(active_dir: Path, com_dir_path: Path) -> QListWidgetItem:
    """
    calculates the relative path of the active directory from the
    common directory path of all the active directories and then
    formats it into a string to be used for an active directory item
    text.

    :param active_dir: an opened directory for performing read/write operations
    :param com_dir_path: common directory of all the active directories.
    :return: an active dir item with the relative path from the common directory
    """
    folder_item_name = active_dir.relative_to(com_dir_path)
    folder_item_name = folder_item_name.as_posix()
    folder_item_name = f"📁 {folder_item_name}/"
    folder_item = QListWidgetItem(folder_item_name)
    return folder_item


def calculate_cur_active_dir_widget_index(active_dirs: List[Path], cur_active_dir: Path) -> int:
    """
    Calculates the current active directory widget index for a given.

    :param active_dirs: The directories open for read/write operations.
    :param cur_active_dir: The current set 'save' directory.
    :return: Widget index of an active directory.
    """
    index_alignment_shift = 1
    cur_active_dir_index = active_dirs.index(cur_active_dir)
    cur_active_dir_widget_index = cur_active_dir_index + index_alignment_shift
    return cur_active_dir_widget_index


def create_custom_cursor_icon(image_path: Path):
    # Load your custom image
    pixmap = QPixmap(image_path.as_posix())
    # Create a cursor with the image, specifying the hotspot (cursor position)
    cursor = QCursor(pixmap, 0, pixmap.height() // 2)  # Adjust as needed
    # Create an icon from the pixmap
    icon = QIcon(pixmap)
    return icon, cursor


class MainWindow(QMainWindow, WindowMixin):
    FIT_WINDOW, FIT_WIDTH, MANUAL_ZOOM = list(range(3))

    # IMAGE AND LABEL INFO
    label_file: LabelFile = None
    image_data: QImage = None

    com_dir_path: Path = None
    active_dir_container: Path = None
    com_img_path: Path = None

    # ACTIVE DIRECTORIES DOCK
    active_dir_dock: QDockWidget = None
    # active directories list widget
    active_dir_list_widget: QListWidget = None
    # buttons for the active directories widget
    move_to_active_dir_button: QPushButton = None
    remove_active_dir_button: QPushButton = None
    reset_active_dir_button: QPushButton = None
    add_active_dir_button: QPushButton = None

    def __init__(self, default_filename=None, default_prefdef_class_file=None, default_save_dir=None):
        super(MainWindow, self).__init__()
        self.setWindowTitle(__appname__)

        self.active_dirs: List[Path] = []
        self.cur_active_dir: Path = None

        # Load setting in the main thread
        self.settings = Settings()
        self.settings.load()
        settings = self.settings

        self.os_name = platform.system()

        # Load string bundle for i18n
        self.string_bundle = StringBundle.get_bundle()

        def get_str(str_id) -> str:
            """
            this function will get the string name for an action

            :param str_id: the string id of an action
            :return: the string name
            """
            try:
                return self.string_bundle.get_string(str_id)
            except AssertionError:
                logger.info("Using additional button name")
                return additional_button_names[str_id]

        # Save as Pascal voc xml
        self.default_save_dir = default_save_dir
        self.label_file_format = settings.get(SETTING_LABEL_FILE_FORMAT, LabelFileFormat.PASCAL_VOC)

        # For loading all images under a directory
        self.m_img_list = []
        self.dir_name = None
        self.label_hist = []
        self.last_open_dir = None
        self.cur_img_idx = 0
        self.img_count = 1

        # Whether we need to save or not.
        self.dirty = False

        self._no_selection_slot = False
        self._beginner = True
        self.screencast = "https://youtu.be/p0nR2YsCY_U"

        # Load predefined classes to the list
        self.load_predefined_classes(default_prefdef_class_file)

        # Main widgets and related state.
        self.label_dialog = LabelDialog(parent=self, list_item=self.label_hist)

        self.items_to_shapes = {}
        self.shapes_to_items = {}
        self.prev_label_text = ''

        list_layout = QVBoxLayout()
        list_layout.setContentsMargins(0, 0, 0, 0)

        # Create a widget for using default label
        self.use_default_label_checkbox = QCheckBox(get_str('useDefaultLabel'))
        self.use_default_label_checkbox.setChecked(False)
        self.default_label_text_line = QLineEdit()
        use_default_label_qhbox_layout = QHBoxLayout()
        use_default_label_qhbox_layout.addWidget(self.use_default_label_checkbox)
        use_default_label_qhbox_layout.addWidget(self.default_label_text_line)
        use_default_label_container = QWidget()
        use_default_label_container.setLayout(use_default_label_qhbox_layout)

        # Create a widget for edit and diffc button
        self.diffc_button = QCheckBox(get_str('useDifficult'))
        self.diffc_button.setChecked(False)
        self.diffc_button.stateChanged.connect(self.button_state)
        self.edit_button = QToolButton()  # noqa
        self.edit_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # Add some widgets to list_layout
        list_layout.addWidget(self.edit_button)
        list_layout.addWidget(self.diffc_button)
        list_layout.addWidget(use_default_label_container)

        # Create and add combobox for showing unique labels in a group
        self.combo_box = ComboBox(self)
        list_layout.addWidget(self.combo_box)

        # Create and add a widget for showing current label items
        self.label_list = QListWidget()  # noqa
        label_list_container = QWidget()
        label_list_container.setLayout(list_layout)
        self.label_list.itemActivated.connect(self.label_selection_changed)
        self.label_list.itemSelectionChanged.connect(self.label_selection_changed)
        self.label_list.itemDoubleClicked.connect(self.edit_label)
        # Connect to itemChanged to detect checkbox changes.
        self.label_list.itemChanged.connect(self.label_item_changed)
        list_layout.addWidget(self.label_list)

        self.dock = QDockWidget(get_str('boxLabelText'), self)
        self.dock.setObjectName(get_str('labels'))
        self.dock.setWidget(label_list_container)

        self.file_list_widget = QListWidget()  # noqa
        self.file_list_widget.itemDoubleClicked.connect(self.file_item_double_clicked)
        self.file_list_widget.itemClicked.connect(self.file_item_clicked)
        self.file_list_widget.setItemDelegate(IndentDelegate(self.file_list_widget))
        self.file_list_event_filter = FileListWidgetEventFilter(self)
        self.file_list_widget.installEventFilter(self.file_list_event_filter)
        file_list_layout = QVBoxLayout()
        file_list_layout.setContentsMargins(0, 0, 0, 0)
        file_list_layout.addWidget(self.file_list_widget)
        file_list_container = QWidget()
        file_list_container.setLayout(file_list_layout)
        self.file_dock = QDockWidget("Image List", self)
        self.file_dock.setObjectName(get_str('files'))
        self.file_dock.setWidget(file_list_container)

        self.zoom_widget = ZoomWidget()
        self.color_dialog = ColorDialog(parent=self)

        self.canvas = Canvas(parent=self)
        self.canvas.zoomRequest.connect(self.zoom_request)
        self.canvas.set_drawing_shape_to_square(settings.get(SETTING_DRAW_SQUARE, False))

        scroll = QScrollArea()  # noqa
        scroll.setWidget(self.canvas)
        scroll.setWidgetResizable(True)
        self.scroll_bars = {
            Qt.Vertical: scroll.verticalScrollBar(),
            Qt.Horizontal: scroll.horizontalScrollBar()
        }
        self.scroll_area = scroll
        self.canvas.scrollRequest.connect(self.scroll_request)

        self.canvas.newShape.connect(self.new_shape)
        self.canvas.shapeMoved.connect(self.set_dirty)
        self.canvas.selectionChanged.connect(self.shape_selection_changed)
        self.canvas.drawingPolygon.connect(self.toggle_drawing_sensitive)

        self.setCentralWidget(scroll)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.file_dock)
        self.setup_active_dir_dock()
        self.file_dock.setFeatures(QDockWidget.DockWidgetFloatable)

        self.dock_features = QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable
        self.dock.setFeatures(self.dock.features() ^ self.dock_features)

        # Actions
        action = partial(new_action, self)
        quit = action(get_str('quit'), self.close,  # noqa
                      'Ctrl+Q', 'quit', get_str('quitApp'))

        open_dir = action(get_str('openDir'), self.retain_file_list_position(self.add_active_dir),
                          'Ctrl+u', 'open', get_str('openDir'))

        move_image = action(get_str("moveImage"), self.retain_file_list_position(self.move_image_to_active_dir),
                            "Ctrl+m")
        icon, cursor = create_custom_cursor_icon(move_image_icon_path)
        move_image.setIcon(icon)

        open_annotation = action(get_str('openAnnotation'), self.open_annotation_dialog,
                                 'Ctrl+Shift+O', 'open', get_str('openAnnotationDetail'))
        copy_prev_bounding = action(get_str('copyPrevBounding'), self.copy_previous_bounding_boxes, 'Ctrl+v', 'copy',
                                    get_str('copyPrevBounding'))

        open_next_image = action(get_str('nextImg'), self.open_next_image,
                                 'd', 'next', get_str('nextImgDetail'))

        open_prev_image = action(get_str('prevImg'), self.open_prev_image,
                                 'a', 'prev', get_str('prevImgDetail'))

        verify = action(get_str('verifyImg'), self.verify_image,
                        'space', 'verify', get_str('verifyImgDetail'))

        save = action(get_str('save'), self.retain_file_list_position(self.save_file),
                      'Ctrl+S', 'save', get_str('saveDetail'), enabled=False)

        def get_format_meta(format):  # noqa
            """
            returns a tuple containing (title, icon_name) of the selected format
            """
            if format == LabelFileFormat.PASCAL_VOC:
                return '&PascalVOC', 'format_voc'
            elif format == LabelFileFormat.YOLO:
                return '&YOLO', 'format_yolo'
            elif format == LabelFileFormat.CREATE_ML:
                return '&CreateML', 'format_createml'

        save_format = action(get_format_meta(self.label_file_format)[0],
                             self.change_format, 'Ctrl+',
                             get_format_meta(self.label_file_format)[1],
                             get_str('changeSaveFormat'), enabled=True)

        save_as = action(get_str('saveAs'), self.save_file_as,
                         'Ctrl+Shift+S', 'save-as', get_str('saveAsDetail'), enabled=False)

        close = action(get_str('closeCur'), self.close_file, 'Ctrl+W', 'close', get_str('closeCurDetail'))

        delete_image = action(get_str('deleteImg'), self.delete_image, 'Ctrl+Shift+D', 'close',
                              get_str('deleteImgDetail'))

        reset_all = action(get_str('resetAll'), self.reset_all, None, 'resetall', get_str('resetAllDetail'))

        color1 = action(get_str('boxLineColor'), self.choose_color1,
                        'Ctrl+L', 'color_line', get_str('boxLineColorDetail'))

        create_mode = action(get_str('crtBox'), self.set_create_mode,
                             'w', 'new', get_str('crtBoxDetail'), enabled=False)
        edit_mode = action(get_str('editBox'), self.set_edit_mode,
                           'Ctrl+J', 'edit', get_str('editBoxDetail'), enabled=False)

        create = action(get_str('crtBox'), self.create_shape,
                        'w', 'new', get_str('crtBoxDetail'), enabled=False)
        delete = action(get_str('delBox'), self.delete_selected_shape,
                        'Delete', 'delete', get_str('delBoxDetail'), enabled=False)
        copy = action(get_str('dupBox'), self.copy_selected_shape,
                      'Ctrl+D', 'copy', get_str('dupBoxDetail'),
                      enabled=False)

        advanced_mode = action(get_str('advancedMode'), self.toggle_advanced_mode,
                               'Ctrl+Shift+A', 'expert', get_str('advancedModeDetail'),
                               checkable=True)

        hide_all = action(get_str('hideAllBox'), partial(self.toggle_polygons, False),
                          'Ctrl+H', 'hide', get_str('hideAllBoxDetail'),
                          enabled=False)
        show_all = action(get_str('showAllBox'), partial(self.toggle_polygons, True),
                          'Ctrl+A', 'hide', get_str('showAllBoxDetail'),
                          enabled=False)

        help_default = action(get_str('tutorialDefault'), self.show_default_tutorial_dialog, None, 'help',
                              get_str('tutorialDetail'))
        show_info = action(get_str('info'), self.show_info_dialog, None, 'help', get_str('info'))
        show_shortcut = action(get_str('shortcut'), self.show_shortcuts_dialog, None, 'help', get_str('shortcut'))

        zoom = QWidgetAction(self)
        zoom.setDefaultWidget(self.zoom_widget)
        self.zoom_widget.setWhatsThis(
            u"Zoom in or out of the image. Also accessible with"
            " %s and %s from the canvas." % (format_shortcut("Ctrl+[-+]"),
                                             format_shortcut("Ctrl+Wheel")))
        self.zoom_widget.setEnabled(False)

        zoom_in = action(get_str('zoomin'), partial(self.add_zoom, 10),
                         'Ctrl++', 'zoom-in', get_str('zoominDetail'), enabled=False)
        zoom_out = action(get_str('zoomout'), partial(self.add_zoom, -10),
                          'Ctrl+-', 'zoom-out', get_str('zoomoutDetail'), enabled=False)
        zoom_org = action(get_str('originalsize'), partial(self.set_zoom, 100),
                          'Ctrl+=', 'zoom', get_str('originalsizeDetail'), enabled=False)
        fit_window = action(get_str('fitWin'), self.set_fit_window,
                            'Ctrl+F', 'fit-window', get_str('fitWinDetail'),
                            checkable=True, enabled=False)
        fit_width = action(get_str('fitWidth'), self.set_fit_width,
                           'Ctrl+Shift+F', 'fit-width', get_str('fitWidthDetail'),
                           checkable=True, enabled=False)
        # Group zoom controls into a list for easier toggling.
        zoom_actions = (self.zoom_widget, zoom_in, zoom_out,
                        zoom_org, fit_window, fit_width)
        self.zoom_mode = self.MANUAL_ZOOM
        self.scalars = {
            self.FIT_WINDOW: self.scale_fit_window,
            self.FIT_WIDTH: self.scale_fit_width,
            # Set to one to scale to 100% when loading files.
            self.MANUAL_ZOOM: lambda: 1,
        }

        edit = action(get_str('editLabel'), self.edit_label,
                      'Ctrl+E', 'edit', get_str('editLabelDetail'),
                      enabled=False)
        self.edit_button.setDefaultAction(edit)

        shape_line_color = action(get_str('shapeLineColor'), self.choose_shape_line_color,
                                  icon='color_line', tip=get_str('shapeLineColorDetail'),
                                  enabled=False)
        shape_fill_color = action(get_str('shapeFillColor'), self.choose_shape_fill_color,
                                  icon='color', tip=get_str('shapeFillColorDetail'),
                                  enabled=False)

        labels = self.dock.toggleViewAction()
        labels.setText(get_str('showHide'))
        labels.setShortcut('Ctrl+Shift+L')

        # Label list context menu.
        label_menu = QMenu()
        add_actions(label_menu, (edit, delete))
        self.label_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.label_list.customContextMenuRequested.connect(
            self.pop_label_list_menu)

        # Draw squares/rectangles
        self.draw_squares_option = QAction(get_str('drawSquares'), self)
        self.draw_squares_option.setShortcut('Ctrl+Shift+R')
        self.draw_squares_option.setCheckable(True)
        self.draw_squares_option.setChecked(settings.get(SETTING_DRAW_SQUARE, False))
        self.draw_squares_option.triggered.connect(self.toggle_draw_square)

        # Store actions for further handling.
        self.actions = Struct(save=save, save_format=save_format, saveAs=save_as, close=close, resetAll=reset_all,
                              deleteImg=delete_image,
                              lineColor=color1, create=create, delete=delete, edit=edit, copy=copy,
                              createMode=create_mode, editMode=edit_mode, advancedMode=advanced_mode,
                              shapeLineColor=shape_line_color, shapeFillColor=shape_fill_color,
                              zoom=zoom, zoomIn=zoom_in, zoomOut=zoom_out, zoomOrg=zoom_org,
                              fitWindow=fit_window, fitWidth=fit_width,
                              zoomActions=zoom_actions,
                              fileMenuActions=(
                                  open_dir, save, save_as, close, reset_all, quit),
                              beginner=(), advanced=(),
                              editMenu=(edit, copy, delete,
                                        None, color1, self.draw_squares_option),
                              beginnerContext=(create, edit, copy, delete),
                              advancedContext=(create_mode, edit_mode, edit, copy,
                                               delete, shape_line_color, shape_fill_color),
                              onLoadActive=(
                                  close, create, create_mode, edit_mode),
                              onShapesPresent=(save_as, hide_all, show_all))

        self.menus = Struct(
            file=self.menu(get_str('menu_file')),
            edit=self.menu(get_str('menu_edit')),
            view=self.menu(get_str('menu_view')),
            help=self.menu(get_str('menu_help')),
            recentFiles=QMenu(get_str('menu_openRecent')),
            labelList=label_menu)

        # Auto saving : Enable auto saving if pressing next
        self.auto_saving = QAction(get_str('autoSaveMode'), self)
        self.auto_saving.setCheckable(True)
        self.auto_saving.setChecked(settings.get(SETTING_AUTO_SAVE, False))
        # Sync single class mode from PR#106
        self.single_class_mode = QAction(get_str('singleClsMode'), self)
        self.single_class_mode.setShortcut("Ctrl+Shift+S")
        self.single_class_mode.setCheckable(True)
        self.single_class_mode.setChecked(settings.get(SETTING_SINGLE_CLASS, False))
        self.lastLabel = None
        # Add an option to enable/disable labels being displayed at the top of bounding boxes
        self.display_label_option = QAction(get_str('displayLabel'), self)
        self.display_label_option.setShortcut("Ctrl+Shift+P")
        self.display_label_option.setCheckable(True)
        self.display_label_option.setChecked(settings.get(SETTING_PAINT_LABEL, False))
        self.display_label_option.triggered.connect(self.toggle_paint_labels_option)

        add_actions(self.menus.file,
                    (open_dir, open_annotation, copy_prev_bounding, self.menus.recentFiles, save, save_format, save_as,
                     close, reset_all, delete_image, quit))
        add_actions(self.menus.help, (help_default, show_info, show_shortcut))
        add_actions(self.menus.view, (
            self.auto_saving,
            self.single_class_mode,
            self.display_label_option,
            labels, advanced_mode, None,
            hide_all, show_all, None,
            zoom_in, zoom_out, zoom_org, None,
            fit_window, fit_width))

        self.menus.file.aboutToShow.connect(self.update_file_menu)

        # Custom context menu for the canvas widget:
        add_actions(self.canvas.menus[0], self.actions.beginnerContext)
        add_actions(self.canvas.menus[1], (
            action('&Copy here', self.copy_shape),
            action('&Move here', self.move_shape)))

        self.tools = self.toolbar('Tools')
        self.actions.beginner = (
            open_dir, move_image, open_next_image, open_prev_image, verify, save, save_format, None, create, copy, delete, None,
            zoom_in, zoom, zoom_out, fit_window, fit_width)

        self.actions.advanced = (
            open_dir, open_next_image, open_prev_image, save, save_format, None,
            create_mode, edit_mode, None,
            hide_all, show_all)

        self.statusBar().showMessage('%s started.' % __appname__)
        self.statusBar().show()

        # Application state.
        self.image = QImage()
        self.file_path = ustr(default_filename)
        self.last_open_dir = None
        self.recent_files = []
        self.max_recent = 7
        self.line_color = None
        self.fill_color = None
        self.zoom_level = 100
        self.fit_window = False
        # Add Chris
        self.difficult = False

        # Fix the compatible issue for qt4 and qt5. Convert the QStringList to a python list
        if settings.get(SETTING_RECENT_FILES):
            if have_qstring():
                recent_file_qstring_list = settings.get(SETTING_RECENT_FILES)
                self.recent_files = [ustr(i) for i in recent_file_qstring_list]
            else:
                self.recent_files = settings.get(SETTING_RECENT_FILES)

        self.recent_files = [file.as_posix() for file in self.recent_files if isinstance(file, Path)]

        size = settings.get(SETTING_WIN_SIZE, QSize(600, 500))
        position = QPoint(0, 0)
        saved_position = settings.get(SETTING_WIN_POSE, position)
        # Fix the multiple monitors issue
        for i in range(QApplication.desktop().screenCount()):  # noqa
            if QApplication.desktop().availableGeometry(i).contains(saved_position):  # noqa
                position = saved_position
                break
        self.resize(size)
        self.move(position)
        save_dir = ustr(settings.get(SETTING_SAVE_DIR, None))
        self.last_open_dir = ustr(settings.get(SETTING_LAST_OPEN_DIR, None))
        if self.default_save_dir is None and save_dir is not None and Path(save_dir).exists():
            self.default_save_dir = save_dir
            self.statusBar().showMessage('%s started. Annotation will be saved to %s' %
                                         (__appname__, self.default_save_dir))
            self.statusBar().show()

        self.restoreState(settings.get(SETTING_WIN_STATE, QByteArray()))
        Shape.line_color = self.line_color = QColor(settings.get(SETTING_LINE_COLOR, DEFAULT_LINE_COLOR))
        Shape.fill_color = self.fill_color = QColor(settings.get(SETTING_FILL_COLOR, DEFAULT_FILL_COLOR))
        self.canvas.set_drawing_color(self.line_color)
        # Add chris
        Shape.difficult = self.difficult

        def xbool(x):
            if isinstance(x, QVariant):
                return x.toBool()  # noqa
            return bool(x)

        if xbool(settings.get(SETTING_ADVANCE_MODE, False)):
            self.actions.advancedMode.setChecked(True)
            self.toggle_advanced_mode()

        # Populate the File menu dynamically.
        self.update_file_menu()

        # Since loading the file may take some time, make sure it runs in the background.
        if self.file_path and Path(self.file_path).is_dir():
            queue_event(partial(self.import_dir_images, self.file_path or ""))
        elif self.file_path:
            queue_event(partial(self.load_file, self.file_path or ""))

        # Callbacks:
        self.zoom_widget.valueChanged.connect(self.paint_canvas)

        self.populate_mode_actions()

        # Display cursor coordinates at the right of status bar
        self.label_coordinates = QLabel('')
        self.statusBar().addPermanentWidget(self.label_coordinates)

        # Open Dir if a default file
        if self.file_path and Path(self.file_path).is_dir():
            self.open_dir_dialog(dirpath=self.file_path, silent=True)

    def retain_file_list_position(self, func: callable) -> callable:
        """
        Retains the file position that you were at and brings you
        back to it after an operation decorated by this function

        :return: Nothing
        """

        @wraps(func)
        def wrapper():
            # get the current index
            org_file_path: Path = self.file_path

            # FUNCTION RUN HERE
            result = func()

            # if the org_file_path was None, that means there was no file path set in the first place;
            # therefore, there is no point in trying to restore something that does not exist
            if not org_file_path:
                return result

            cur_pos = self.scan_all_for_file(org_file_path.name)
            if not cur_pos:
                return result

            if cur_pos != org_file_path:
                logger.info("system detects image was moved to a different folder")

            if cur_pos.as_posix() not in self.m_img_list:
                return result

            # restore the position
            self.file_path = cur_pos
            self.load_file(self.file_path)

            return result

        return wrapper

    def file_item_clicked(self, item):
        """
        for when an item is clicked once
        :return:
        """
        if "\\" in item.text():
            self.cur_img_idx = 0
            filename = self.m_img_list[self.cur_img_idx]
            if filename:
                self.load_file(filename)

    def setup_active_dir_dock(self):
        self.active_dir_list_widget = QListWidget()  # noqa
        self.active_dir_list_widget.itemClicked.connect(self.active_dir_item_clicked)
        self.active_dir_list_widget.setItemDelegate(IndentDelegate(self.active_dir_list_widget))

        active_dir_list_layout = QVBoxLayout()
        active_dir_list_layout.addWidget(self.active_dir_list_widget)

        button_layout = QHBoxLayout()

        self.add_active_dir_button = QPushButton(self.tr("Add Dir"))
        self.add_active_dir_button.clicked.connect(self.retain_file_list_position(self.add_active_dir))
        button_layout.addWidget(self.add_active_dir_button)

        self.reset_active_dir_button = QPushButton(self.tr("Reset Dirs"))
        self.reset_active_dir_button.clicked.connect(self.reset_active_dirs)
        button_layout.addWidget(self.reset_active_dir_button)

        self.remove_active_dir_button = QPushButton(self.tr("Remove Dir"))
        self.remove_active_dir_button.clicked.connect(self.retain_file_list_position(self.remove_selected_active_dir))
        button_layout.addWidget(self.remove_active_dir_button)

        active_dir_list_layout.addLayout(button_layout)

        self.active_dir_container = QWidget()
        self.active_dir_container.setLayout(active_dir_list_layout)

        self.active_dir_dock = QDockWidget(self.tr("Active Directories"), self)
        self.active_dir_dock = QDockWidget(self.tr("Active Directories"), self)
        self.active_dir_dock.setObjectName("activeDirectoriesDockWidget")
        self.active_dir_dock.setWidget(self.active_dir_container)
        self.addDockWidget(Qt.RightDockWidgetArea, self.active_dir_dock)

    def move_image_to_active_dir(self):
        """
        moves the currently selected image, and its annotation file to the current active directory
        whilst updating their position in the self.m_img_list and anywhere else where their position
        is stored

        :return:
        """
        if self.dirty:
            self.save_file()
            return

        # Check if there is a selected image
        if self.cur_img_idx < 0:
            return

        # Get the selected image, its annotation file and elmer file
        image_file = Path(self.m_img_list[self.cur_img_idx])
        ann_file = self.scan_all_for_file(image_file.stem + XML_EXT, image_file.parent)
        elmer_file = self.scan_all_for_file(image_file.stem + ELMER_EXT, image_file.parent)

        # Get the current active directory
        active_dir = self.cur_active_dir

        # If no active directory is selected, display an error message and return
        if not active_dir:
            QMessageBox.warning(self, self.tr("Error"), self.tr("No active directory selected"))
            return

        # Move an image

        ## Move the image
        if not image_file:
            pass
        elif image_file.exists():
            new_image_path = active_dir / image_file.name
            shutil.move(image_file, new_image_path)
            self.m_img_list[self.cur_img_idx] = Path(new_image_path)

        ## Move the annotation file
        if not ann_file:
            pass
        elif ann_file.exists():
            new_annotation_path = active_dir / ann_file.name
            shutil.move(ann_file, new_annotation_path)

        ## Move the elmer file
        if not elmer_file:
            pass
        elif elmer_file.exists():
            new_elmer_file_path = self.cur_active_dir / elmer_file.name
            shutil.move(elmer_file, new_elmer_file_path)

        # Update the image list

        # Update the UI elements, if needed
        self.update_file_menu()
        self.import_dir_images(self.cur_active_dir)
        self.load_file(self.m_img_list[self.cur_img_idx])

    def export_repeating_file_names_to_cmd(self):
        """
        """
        if self.m_img_list:

            def find_identical_filenames(start_directory):
                from collections import defaultdict
                identical_files = defaultdict(list)

                # Walk through the directory
                for root, dirs, files in os.walk(start_directory):
                    for file_name in files:
                        # Get the full path of the file
                        full_path = os.path.join(root, file_name)

                        # Add the full path to the list of paths for this filename
                        identical_files[file_name].append(full_path)

                # Filter out filenames that don't have duplicates
                identical_files = {k: v for k, v in identical_files.items() if len(v) > 1}

                return identical_files

            start_dir = self.com_img_path  # Replace it with your starting directory
            result = find_identical_filenames(start_dir)

            from pathlib import Path

            # Print the results
            if result:
                for filename, paths in result.items():
                    print(f"Identical filename found: {filename}")
                    for path in paths:
                        print(f"  - {Path(path).parent}")
                    print()  # Empty line for readability
                    return True
            else:
                return False
        else:
            return True

    def active_dir_item_clicked(self, item):
        # find the true index of the active directory
        index = 0
        for index in range(self.active_dir_list_widget.count()):
            item_ = self.active_dir_list_widget.item(index)
            if item_.text() == item.text():
                index -= 1
                break

        # move the selected to the next item after the container directory
        if index < 0:
            nxt_item = self.active_dir_list_widget.item(1)
            nxt_item.setSelected(True)
            index = 0

        self.cur_active_dir = self.active_dirs[index]
        rel_cur_active_dir = self.cur_active_dir.relative_to(self.com_dir_path)
        rel_cur_active_dir_msg = f"Active Directories (SAVE TO) >>  {rel_cur_active_dir}"
        self.active_dir_dock.setWindowTitle(rel_cur_active_dir_msg)

    def add_active_dir(self):
        # setup dir_path
        dir_path = QFileDialog.getExistingDirectory(self, self.tr("Select Active Directory"))
        if not dir_path:
            return
        self.cur_active_dir = Path(dir_path)

        # Add a new active directory
        # Update the active directories list
        if self.cur_active_dir not in self.active_dirs:
            # Add the new active directory to the list
            self.active_dirs.append(self.cur_active_dir)
            # Calculate the new common directory
            self.com_dir_path = calculate_com_dir_path(self.active_dirs)

            # create the items
            active_dir_items_list = [create_container_folder_item(self.com_dir_path)]
            active_dir_items_list.extend(
                create_active_dir_item(active_dir, self.com_dir_path) for active_dir in self.active_dirs)

            self.active_dir_list_widget.clear()
            _ = [self.active_dir_list_widget.addItem(item) for item in active_dir_items_list]

        # Select the last opened active directory
        cur_active_dir_widget_index = calculate_cur_active_dir_widget_index(self.active_dirs, self.cur_active_dir)
        item = self.active_dir_list_widget.item(cur_active_dir_widget_index)

        item.setSelected(True)
        self.active_dir_list_widget.setCurrentItem(item)

        rel_cur_active_dir_msg = calculate_rel_cur_active_dir_msg(self.cur_active_dir, self.com_dir_path)
        self.active_dir_dock.setWindowTitle(rel_cur_active_dir_msg)

        # update the image list
        self.import_dir_images(dir_path)

    def reset_active_dirs(self):
        self.active_dirs.clear()
        self.active_dir_list_widget.clear()
        self.cur_active_dir = None
        self.statusBar().showMessage("Active directories reset")  # noqa
        self.file_list_widget.clear()
        self.reset_state()

    def remove_selected_active_dir(self):
        selected_items = self.active_dir_list_widget.selectedItems()
        directory = ""
        if selected_items:
            # search through selected items to find the one that is to be removed
            directory_text = selected_items[0].text()
            for i in range(self.active_dir_list_widget.count()):
                item_ = self.active_dir_list_widget.item(i)
                if item_.text() == directory_text:
                    index = i - 1
                    directory = self.active_dirs[index]
                    break

            self.remove_active_directory(directory, directory_text)

    def remove_active_directory(self, directory: Path, directory_text):
        # Remove the directory from the active_dirs list
        original_active_dir = self.cur_active_dir

        # we don't want the directory to remove to be the same as the current one,
        # so we change it to the currently active file path's parent, essentially,
        # we're just picking another one by random choice, however this is not ideal,
        # relying on an unstable variable self.file_path introduces instability to the
        # code.
        if not directory == self.cur_active_dir:
            pass
        elif self.file_path:
            self.cur_active_dir = Path(self.file_path).parent

        if not self.may_continue():
            return

        self.cur_active_dir = original_active_dir

        if directory not in self.active_dirs:
            raise ValueError("Error finding the active directory in the parallel list of active directories")

        self.active_dirs.remove(directory)
        if not self.active_dirs:
            self.reset_active_dirs()

        # Remove the directory from the active_dir_list_widget
        items = self.active_dir_list_widget.findItems(directory_text, Qt.MatchExactly)
        for item in items:
            self.active_dir_list_widget.takeItem(self.active_dir_list_widget.row(item))

        # Store the current image path
        current_image_path = self.file_path

        # Rebuild the image list
        self.m_img_list = []
        for active_dir in self.active_dirs:
            self.m_img_list.extend(scan_for_images(active_dir))
        self.sort_img_list()

        self.cur_img_idx = self.m_img_list.index(current_image_path) if current_image_path in self.m_img_list else 0
        self.import_dir_images(self.last_open_dir)

    def scan_all_images(self):
        images = []
        for active_dir in self.active_dirs:
            images.extend(scan_for_images(active_dir))
        return images

    def scan_all_for_file(self, name: str, exp_dir: Path = None) -> Path:
        exp_file_path = None
        if exp_dir:
            exp_file_path = exp_dir / name
        for directory in self.active_dirs:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file == name:
                        file_path = Path(root) / file
                        if exp_dir:
                            if not file_path == exp_file_path:
                                pass
                                # logger.info("Annotation file was not found where it was supposed")
                        return file_path

    def keyReleaseEvent(self, event):  # noqa
        if event.key() == Qt.Key_Control:
            self.canvas.set_drawing_shape_to_square(False)

    def keyPressEvent(self, event):  # noqa
        if event.key() == Qt.Key_Control:
            # Draw rectangle if Ctrl is pressed
            self.canvas.set_drawing_shape_to_square(True)

    # Support Functions #
    def set_format(self, save_format):
        if save_format == FORMAT_PASCALVOC:
            self.actions.save_format.setText(FORMAT_PASCALVOC)  # noqa
            self.actions.save_format.setIcon(new_icon("format_voc"))  # noqa
            self.label_file_format = LabelFileFormat.PASCAL_VOC
            LabelFile.suffix = XML_EXT

        elif save_format == FORMAT_YOLO:
            self.actions.save_format.setText(FORMAT_YOLO)  # noqa
            self.actions.save_format.setIcon(new_icon("format_yolo"))  # noqa
            self.label_file_format = LabelFileFormat.YOLO
            LabelFile.suffix = TXT_EXT

        elif save_format == FORMAT_CREATEML:
            self.actions.save_format.setText(FORMAT_CREATEML)  # noqa
            self.actions.save_format.setIcon(new_icon("format_createml"))  # noqa
            self.label_file_format = LabelFileFormat.CREATE_ML
            LabelFile.suffix = JSON_EXT

    def change_format(self):
        if self.label_file_format == LabelFileFormat.PASCAL_VOC:
            self.set_format(FORMAT_YOLO)
        elif self.label_file_format == LabelFileFormat.YOLO:
            self.set_format(FORMAT_CREATEML)
        elif self.label_file_format == LabelFileFormat.CREATE_ML:
            self.set_format(FORMAT_PASCALVOC)
        else:
            raise ValueError('Unknown label file format.')
        self.set_dirty()

    def no_shapes(self):
        return not self.items_to_shapes

    def toggle_advanced_mode(self, value=True):
        self._beginner = not value
        self.canvas.set_editing(True)
        self.populate_mode_actions()
        self.edit_button.setVisible(not value)
        if value:
            self.actions.createMode.setEnabled(True)
            self.actions.editMode.setEnabled(False)
            self.dock.setFeatures(self.dock.features() | self.dock_features)
        else:
            self.dock.setFeatures(self.dock.features() ^ self.dock_features)

    def populate_mode_actions(self):
        if self.beginner():
            tool, menu = self.actions.beginner, self.actions.beginnerContext
        else:
            tool, menu = self.actions.advanced, self.actions.advancedContext
        self.tools.clear()
        add_actions(self.tools, tool)
        self.canvas.menus[0].clear()
        add_actions(self.canvas.menus[0], menu)
        self.menus.edit.clear()
        actions = (self.actions.create,) if self.beginner() \
            else (self.actions.createMode, self.actions.editMode)
        add_actions(self.menus.edit, actions + self.actions.editMenu)

    def set_beginner(self):
        self.tools.clear()
        add_actions(self.tools, self.actions.beginner)

    def set_advanced(self):
        self.tools.clear()
        add_actions(self.tools, self.actions.advanced)

    def set_dirty(self):
        self.dirty = True
        self.actions.save.setEnabled(True)

    def set_clean(self):
        self.dirty = False
        self.actions.save.setEnabled(False)
        self.actions.create.setEnabled(True)

    def toggle_actions(self, value=True):
        """Enable/Disable widgets which depend on an opened image."""
        for z in self.actions.zoomActions:
            z.setEnabled(value)
        for action in self.actions.onLoadActive:
            action.setEnabled(value)

    def status(self, message, delay=5000):
        self.statusBar().showMessage(message, delay)

    def reset_state(self):
        self.items_to_shapes.clear()
        self.shapes_to_items.clear()
        self.label_list.clear()
        self.file_path = None
        self.image_data = None
        self.label_file = None
        self.canvas.reset_state()
        self.canvas.pixmap = QPixmap()
        self.canvas.shapes.clear()
        self.label_coordinates.clear()
        self.combo_box.cb.clear()

    def current_item(self):
        items = self.label_list.selectedItems()
        if items:
            return items[0]
        return None

    def add_recent_file(self, file_path):
        if file_path in self.recent_files:
            self.recent_files.remove(file_path)
        elif len(self.recent_files) >= self.max_recent:
            self.recent_files.pop()
        self.recent_files.insert(0, file_path)

    def beginner(self):
        return self._beginner

    def advanced(self):
        return not self.beginner()

    def show_tutorial_dialog(self, browser='default', link=None):
        if link is None:
            link = self.screencast

        if browser.lower() == 'default':
            wb.open(link, new=2)
        elif browser.lower() == 'chrome' and self.os_name == 'Windows':
            if shutil.which(browser.lower()):  # 'chrome' not in wb._browsers in windows
                wb.register('chrome', None, wb.BackgroundBrowser('chrome'))
            else:
                chrome_path = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                if Path(chrome_path).is_file():
                    wb.register('chrome', None, wb.BackgroundBrowser(chrome_path))
            try:
                wb.get('chrome').open(link, new=2)
            except:  # noqa
                wb.open(link, new=2)
        elif browser.lower() in wb._browsers:  # noqa
            wb.get(browser.lower()).open(link, new=2)

    def show_default_tutorial_dialog(self):
        self.show_tutorial_dialog(browser='default')

    def show_info_dialog(self):
        from libs.__init__ import __version__  # noqa
        msg = u'Name:{0} \nApp Version:{1} \n{2} '.format(__appname__, __version__, sys.version_info)
        QMessageBox.information(self, u'Information', msg)

    def show_shortcuts_dialog(self):
        self.show_tutorial_dialog(browser='default', link='https://github.com/tzutalin/labelImg#Hotkeys')

    def create_shape(self):
        assert self.beginner()
        self.canvas.set_editing(False)
        self.actions.create.setEnabled(False)

    def toggle_drawing_sensitive(self, drawing=True):
        """In the middle of drawing, toggling between modes should be disabled."""
        self.actions.editMode.setEnabled(not drawing)
        if not drawing and self.beginner():
            # Cancel creation.
            print('Cancel creation.')
            self.canvas.set_editing(True)
            self.canvas.restore_cursor()
            self.actions.create.setEnabled(True)

    def toggle_draw_mode(self, edit=True):
        self.canvas.set_editing(edit)
        self.actions.createMode.setEnabled(edit)
        self.actions.editMode.setEnabled(not edit)

    def set_create_mode(self):
        assert self.advanced()
        self.toggle_draw_mode(False)

    def set_edit_mode(self):
        assert self.advanced()
        self.toggle_draw_mode(True)
        self.label_selection_changed()

    def update_file_menu(self):
        curr_file_path = self.file_path

        def exists(filename):
            return Path(filename).exists()

        menu = self.menus.recentFiles
        menu.clear()
        files = [
            f.replace("\\", "/") for f in self.recent_files
            if f != curr_file_path
            and exists(f)
            and f is str
        ]
        for i, f in enumerate(files):
            icon = new_icon('labels')
            action = QAction(
                icon, '&%d %s' % (i + 1, QFileInfo(f).fileName()), self)
            action.triggered.connect(partial(self.load_recent, f))
            menu.addAction(action)

    def pop_label_list_menu(self, point):
        self.menus.labelList.exec_(self.label_list.mapToGlobal(point))

    def edit_label(self):
        if not self.canvas.editing():
            return
        item = self.current_item()
        if not item:
            return
        text = self.label_dialog.pop_up(item.text())
        if text is not None:
            item.setText(text)
            item.setBackground(generate_color_by_text(text))
            self.set_dirty()
            self.update_combo_box()

    def file_item_double_clicked(self, item=None):
        full_image_file_path = ustr(self.get_full_img_path(item.text()))

        if not full_image_file_path.as_posix() in self.m_img_list:
            self.cur_img_idx = 0
        else:
            self.cur_img_idx = self.m_img_list.index(full_image_file_path.as_posix())

        filename = self.m_img_list[self.cur_img_idx]
        if filename:
            self.load_file(filename)

    def get_full_img_path(self, img_path: str) -> str:
        """
        gets the full image path from

        :param img_path: the relative image path

        :return: the image path
        """
        ascii_image_path = ''.join(c for c in img_path if ord(c) < 128)
        return self.com_img_path / ascii_image_path.strip()

    # Add chris
    def button_state(self):
        """ Function to handle challenging examples
        Update on each object """
        if not self.canvas.editing():
            return

        item = self.current_item()
        if not item:  # If not selected Item, take the first one
            item = self.label_list.item(self.label_list.count() - 1)

        difficult = self.diffc_button.isChecked()

        shape = None

        try:
            shape = self.items_to_shapes[item]
        except:  # noqa
            pass
        # Checked and Update
        try:
            if difficult != shape.difficult:
                shape.difficult = difficult
                self.set_dirty()
            else:  # User probably changed item visibility
                self.canvas.set_shape_visible(shape, item.checkState() == Qt.Checked)
        except:  # noqa
            pass

    # React to canvas signals.
    def shape_selection_changed(self, selected=False):
        if self._no_selection_slot:
            self._no_selection_slot = False
        else:
            shape = self.canvas.selected_shape
            if shape:
                self.shapes_to_items[shape].setSelected(True)
            else:
                self.label_list.clearSelection()
        self.actions.delete.setEnabled(selected)
        self.actions.copy.setEnabled(selected)
        self.actions.edit.setEnabled(selected)
        self.actions.shapeLineColor.setEnabled(selected)
        self.actions.shapeFillColor.setEnabled(selected)

    def add_label(self, shape):
        shape.paint_label = self.display_label_option.isChecked()
        item = HashableQListWidgetItem(shape.label)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Checked)
        item.setBackground(generate_color_by_text(shape.label))
        self.items_to_shapes[item] = shape
        self.shapes_to_items[shape] = item
        self.label_list.addItem(item)
        for action in self.actions.onShapesPresent:
            action.setEnabled(True)
        self.update_combo_box()

    def remove_label(self, shape):
        if shape is None:
            # print('rm empty label')
            return
        item = self.shapes_to_items[shape]
        self.label_list.takeItem(self.label_list.row(item))
        del self.shapes_to_items[shape]
        del self.items_to_shapes[item]
        self.update_combo_box()

    def load_labels(self, shapes):
        s = []
        for label, points, line_color, fill_color, difficult in shapes:
            shape = Shape(label=label)
            for x, y in points:

                # Ensure the labels are within the bounds of the image. If not, fix them.
                x, y, snapped = self.canvas.snap_point_to_canvas(x, y)
                if snapped:
                    self.set_dirty()

                shape.add_point(QPointF(x, y))
            shape.difficult = difficult
            shape.close()
            s.append(shape)

            if line_color:
                shape.line_color = QColor(*line_color)
            else:
                shape.line_color = generate_color_by_text(label)

            if fill_color:
                shape.fill_color = QColor(*fill_color)
            else:
                shape.fill_color = generate_color_by_text(label)

            self.add_label(shape)
        self.update_combo_box()
        self.canvas.load_shapes(s)

    def update_combo_box(self):
        # Get the unique labels and add them to the Combobox.
        items_text_list = [str(self.label_list.item(i).text()) for i in range(self.label_list.count())]

        unique_text_list = list(set(items_text_list))
        # Add a null row for showing all the labels
        unique_text_list.append("")
        unique_text_list.sort()

        self.combo_box.update_items(unique_text_list)

    def save_labels(self, ann_file_path):
        ann_file_path = ustr(ann_file_path)
        if self.label_file is None:
            self.label_file = LabelFile()
            self.label_file.verified = self.canvas.verified

        def format_shape(s):
            return dict(label=s.label,
                        line_color=s.line_color.getRgb(),
                        fill_color=s.fill_color.getRgb(),
                        points=[(p.x(), p.y()) for p in s.points],
                        # add chris
                        difficult=s.difficult)

        shapes = [format_shape(shape) for shape in self.canvas.shapes]
        # Can add different annotation formats here
        try:
            # print("PRE SAVE")
            if self.label_file_format == LabelFileFormat.PASCAL_VOC:
                ann_file_path: Path
                if ann_file_path.suffix != ".xml":
                    ann_file_path += XML_EXT
                self.label_file.save_pascal_voc_format(ann_file_path.as_posix(), shapes, self.file_path.as_posix(), self.image_data,
                                                       self.line_color.getRgb(), self.fill_color.getRgb())

            elif self.label_file_format == LabelFileFormat.YOLO:
                if ann_file_path.suffix != ".txt":
                    ann_file_path += TXT_EXT
                self.label_file.save_yolo_format(ann_file_path.as_posix(), shapes, self.file_path.as_posix(), self.image_data,
                                                 self.label_hist,
                                                 self.line_color.getRgb(), self.fill_color.getRgb())
            elif self.label_file_format == LabelFileFormat.CREATE_ML:
                if ann_file_path.suffix != ".json":
                    ann_file_path += JSON_EXT
                self.label_file.save_create_ml_format(ann_file_path.as_posix(), shapes, self.file_path.as_posix(), self.image_data,
                                                      self.label_hist, self.line_color.getRgb(),
                                                      self.fill_color.getRgb())
            else:
                self.label_file.save(ann_file_path.as_posix(), shapes, self.file_path.as_posix(), self.image_data,
                                     self.line_color.getRgb(), self.fill_color.getRgb())
            print('Image:{0} -> Annotation:{1}'.format(self.file_path, ann_file_path))
            return True
        except LabelFileError as e:
            self.error_message(u'Error saving label data', u'<b>%s</b>' % e)
            return False

    def copy_selected_shape(self):
        self.add_label(self.canvas.copy_selected_shape())
        # fix copy and delete
        self.shape_selection_changed(True)

    def combo_selection_changed(self, index):
        text = self.combo_box.cb.itemText(index)
        for i in range(self.label_list.count()):
            if text == "":
                self.label_list.item(i).setCheckState(2)  # noqa
            elif text != self.label_list.item(i).text():
                self.label_list.item(i).setCheckState(0)  # noqa
            else:
                self.label_list.item(i).setCheckState(2)  # noqa

    def label_selection_changed(self):
        item = self.current_item()
        if item and self.canvas.editing():
            self._no_selection_slot = True
            self.canvas.select_shape(self.items_to_shapes[item])
            shape = self.items_to_shapes[item]
            # Add Chris
            self.diffc_button.setChecked(shape.difficult)

    def label_item_changed(self, item):
        shape = self.items_to_shapes[item]
        label = item.text()
        if label != shape.label:
            shape.label = item.text()
            shape.line_color = generate_color_by_text(shape.label)
            self.set_dirty()
        else:  # User probably changed item visibility
            self.canvas.set_shape_visible(shape, item.checkState() == Qt.Checked)

    # Callback functions:
    def new_shape(self):
        """Pop-up and give focus to the label editor.

        Position MUST be in global coordinates.
        """
        if not self.use_default_label_checkbox.isChecked() or not self.default_label_text_line.text():
            if len(self.label_hist) > 0:
                self.label_dialog = LabelDialog(
                    parent=self, list_item=self.label_hist)

            # Sync single class mode from PR#106
            if self.single_class_mode.isChecked() and self.lastLabel:
                text = self.lastLabel
            else:
                text = self.label_dialog.pop_up(text=self.prev_label_text)
                self.lastLabel = text
        else:
            text = self.default_label_text_line.text()

        # Add Chris
        self.diffc_button.setChecked(False)
        if text is not None:
            self.prev_label_text = text
            generate_color = generate_color_by_text(text)
            shape = self.canvas.set_last_label(text, generate_color, generate_color)
            self.add_label(shape)
            if self.beginner():  # Switch to edit mode.
                self.canvas.set_editing(True)
                self.actions.create.setEnabled(True)
            else:
                self.actions.editMode.setEnabled(True)
            self.set_dirty()

            if text not in self.label_hist:
                self.label_hist.append(text)
        else:
            # self.canvas.undoLastLine()
            self.canvas.reset_all_lines()

    def scroll_request(self, delta, orientation):
        units = - delta / (8 * 15)
        bar = self.scroll_bars[orientation]
        bar.setValue(bar.value() + bar.singleStep() * units)

    def set_zoom(self, value):
        self.actions.fitWidth.setChecked(False)
        self.actions.fitWindow.setChecked(False)
        self.zoom_mode = self.MANUAL_ZOOM
        self.zoom_widget.setValue(value)

    def add_zoom(self, increment=10):
        self.set_zoom(self.zoom_widget.value() + increment)

    def zoom_request(self, delta):
        # get the current scrollbar positions
        # calculate the percentages ~ coordinates
        h_bar = self.scroll_bars[Qt.Horizontal]
        v_bar = self.scroll_bars[Qt.Vertical]

        # get the current maximum, to know the difference after zooming
        h_bar_max = h_bar.maximum()
        v_bar_max = v_bar.maximum()

        # get the cursor position and canvas size
        # to calculate the desired movement from 0 to 1
        # where 0 = move left
        #       1 = move right
        # up and down analogous
        cursor = QCursor()
        pos = cursor.pos()
        relative_pos = QWidget.mapFromGlobal(self, pos)

        cursor_x = relative_pos.x()
        cursor_y = relative_pos.y()

        w = self.scroll_area.width()
        h = self.scroll_area.height()

        # the scaling from 0 to 1 has some padding
        # you don't have to hit the very leftmost pixel for a maximum-left movement
        margin = 0.1
        move_x = (cursor_x - margin * w) / (w - 2 * margin * w)
        move_y = (cursor_y - margin * h) / (h - 2 * margin * h)

        # clamp the values from 0 to 1
        move_x = min(max(move_x, 0), 1)
        move_y = min(max(move_y, 0), 1)

        # zoom in
        units = delta / (8 * 15)
        scale = 10
        self.add_zoom(scale * units)

        # get the difference in scrollbar values
        # this is how far we can move
        d_h_bar_max = h_bar.maximum() - h_bar_max
        d_v_bar_max = v_bar.maximum() - v_bar_max

        # get the new scrollbar values
        new_h_bar_value = h_bar.value() + move_x * d_h_bar_max
        new_v_bar_value = v_bar.value() + move_y * d_v_bar_max

        h_bar.setValue(new_h_bar_value)
        v_bar.setValue(new_v_bar_value)

    def set_fit_window(self, value=True):
        if value:
            self.actions.fitWidth.setChecked(False)
        self.zoom_mode = self.FIT_WINDOW if value else self.MANUAL_ZOOM
        self.adjust_scale()

    def set_fit_width(self, value=True):
        if value:
            self.actions.fitWindow.setChecked(False)
        self.zoom_mode = self.FIT_WIDTH if value else self.MANUAL_ZOOM
        self.adjust_scale()

    def toggle_polygons(self, value):
        for item, shape in self.items_to_shapes.items():
            item.setCheckState(Qt.Checked if value else Qt.Unchecked)

    def load_file(self, file_path=None):
        """Load the specified file, or the last opened file if None."""
        self.reset_state()
        self.canvas.setEnabled(False)
        if file_path is None:
            file_path = self.settings.get(SETTING_FILENAME)

        # Make sure that filePath is a regular python string, rather than QString
        file_path = Path(ustr(file_path))

        # Fix bug: An index error after select a directory when open a new file.
        unicode_file_path = file_path.absolute()

        # Highlight the file item
        if unicode_file_path and self.file_list_widget.count() > 0:
            if unicode_file_path.as_posix() in self.m_img_list:
                index = self.m_img_list.index(unicode_file_path.as_posix()) + 1
                file_widget_item = self.file_list_widget.item(index)
                file_widget_item.setSelected(True)
            else:
                self.file_list_widget.clear()
                self.m_img_list.clear()

        if unicode_file_path and os.path.exists(unicode_file_path):
            # Load image file
            self.image_data = read(unicode_file_path.as_posix(), None)
            self.label_file = None
            self.canvas.verified = False

            if isinstance(self.image_data, QImage):
                image = self.image_data
            else:
                image = QImage.fromData(self.image_data)  # noqa
            if image.isNull():
                self.error_message(u'Error opening file',
                                   u"<p>Make sure <i>%s</i> is a valid image file." % unicode_file_path)
                self.status("Error reading %s" % unicode_file_path)
                return False

            self.status("Loaded %s" % os.path.basename(unicode_file_path))
            self.image = image
            self.file_path = unicode_file_path
            self.canvas.load_pixmap(QPixmap.fromImage(image))  # noqa

            self.set_clean()
            self.canvas.setEnabled(True)
            self.adjust_scale(initial=True)
            self.paint_canvas()
            self.add_recent_file(self.file_path)
            self.toggle_actions(True)
            self.show_bounding_box_from_annotation_file(file_path)

            counter = self.counter_str()
            self.setWindowTitle(__appname__ + ' ' + file_path.as_posix() + ' ' + counter)

            # Default: select last item if there is at least one item
            if self.label_list.count():
                self.label_list.setCurrentItem(self.label_list.item(self.label_list.count() - 1))
                self.label_list.item(self.label_list.count() - 1).setSelected(True)

            self.canvas.setFocus(True)  # noqa
            return True
        return False

    def counter_str(self):
        """
        Converts image counter to string representation.
        """
        return '[{} / {}]'.format(self.cur_img_idx + 1, self.img_count)

    def show_bounding_box_from_annotation_file(self, file_path):
        xml_path = self.scan_all_for_file(file_path.stem + XML_EXT)
        txt_path = self.scan_all_for_file(file_path.stem + TXT_EXT)
        json_path = self.scan_all_for_file(file_path.stem + JSON_EXT)

        """
        Annotation file priority:
        XML > TXT > JSON
        """

        if xml_path or txt_path or json_path:
            if xml_path.is_file():
                self.load_pascal_xml_by_filename(xml_path)
                return
            elif txt_path.is_file():
                self.load_yolo_txt_by_filename(txt_path)
                return
            elif json_path.is_file():
                self.load_create_ml_json_by_filename(json_path, file_path)
                return

        self.label_file = None
        self.load_labels([])

    def resizeEvent(self, event):
        if self.canvas and not self.image.isNull() \
                and self.zoom_mode != self.MANUAL_ZOOM:
            self.adjust_scale()
        super(MainWindow, self).resizeEvent(event)

    def paint_canvas(self):
        assert not self.image.isNull(), "cannot paint null image"
        self.canvas.scale = 0.01 * self.zoom_widget.value()
        self.canvas.label_font_size = int(0.02 * max(self.image.width(), self.image.height()))
        self.canvas.adjustSize()
        self.canvas.update()

    def adjust_scale(self, initial=False):
        value = self.scalars[self.FIT_WINDOW if initial else self.zoom_mode]()
        self.zoom_widget.setValue(int(100 * value))

    def scale_fit_window(self):
        """Figure out the size of the pixmap to fit the main widget."""
        e = 2.0  # So that no scrollbars are generated.
        w1 = self.centralWidget().width() - e
        h1 = self.centralWidget().height() - e
        a1 = w1 / h1
        # Calculate a new scale value based on the pixmap's aspect ratio.
        w2 = self.canvas.pixmap.width() - 0.0
        h2 = self.canvas.pixmap.height() - 0.0
        a2 = w2 / h2
        return w1 / w2 if a2 >= a1 else h1 / h2

    def scale_fit_width(self):
        # The epsilon does not seem to work too well here.
        w = self.centralWidget().width() - 2.0
        return w / self.canvas.pixmap.width()

    def closeEvent(self, event):
        if not self.may_continue():
            event.ignore()
        settings = self.settings
        # If it loads images from dir, don't load it at the beginning
        if self.dir_name is None:
            settings[SETTING_FILENAME] = self.file_path if self.file_path else ''
        else:
            settings[SETTING_FILENAME] = ''

        settings[SETTING_WIN_SIZE] = self.size()
        settings[SETTING_WIN_POSE] = self.pos()
        settings[SETTING_WIN_STATE] = self.saveState()
        settings[SETTING_LINE_COLOR] = self.line_color
        settings[SETTING_FILL_COLOR] = self.fill_color
        settings[SETTING_RECENT_FILES] = self.recent_files
        settings[SETTING_ADVANCE_MODE] = not self._beginner
        if self.default_save_dir and os.path.exists(self.default_save_dir):
            settings[SETTING_SAVE_DIR] = ustr(self.default_save_dir)
        else:
            settings[SETTING_SAVE_DIR] = ''

        if self.last_open_dir and os.path.exists(self.last_open_dir):
            settings[SETTING_LAST_OPEN_DIR] = self.last_open_dir
        else:
            settings[SETTING_LAST_OPEN_DIR] = ''

        settings[SETTING_AUTO_SAVE] = self.auto_saving.isChecked()
        settings[SETTING_SINGLE_CLASS] = self.single_class_mode.isChecked()
        settings[SETTING_PAINT_LABEL] = self.display_label_option.isChecked()
        settings[SETTING_DRAW_SQUARE] = self.draw_squares_option.isChecked()
        settings[SETTING_LABEL_FILE_FORMAT] = self.label_file_format
        settings.save()

    def load_recent(self, filename):
        if self.may_continue():
            self.load_file(filename)

    def change_save_dir_dialog(self, _value=False):
        if self.default_save_dir is not None:
            path = ustr(self.default_save_dir)
        else:
            path = '../..'

        dir_path = ustr(QFileDialog.getExistingDirectory(self,
                                                         '%s - Save annotations to the directory' % __appname__, path,
                                                         QFileDialog.ShowDirsOnly
                                                         | QFileDialog.DontResolveSymlinks))

        if dir_path is not None and len(dir_path) > 1:
            self.default_save_dir = dir_path

        self.statusBar().showMessage('%s . Annotation will be saved to %s' %
                                     ('Change saved folder', self.default_save_dir))
        self.statusBar().show()

    def open_annotation_dialog(self, _value=False):
        if self.file_path is None:
            self.statusBar().showMessage('Please select image first')
            self.statusBar().show()
            return

        path = Path(ustr(self.file_path)).parent \
            if self.file_path else '.'
        if self.label_file_format == LabelFileFormat.PASCAL_VOC:
            filters = "Open Annotation XML file (%s)" % ' '.join(['*.xml'])
            filename = ustr(QFileDialog.getOpenFileName(self, '%s - Choose a xml file' % __appname__, path, filters))
            if filename:
                if isinstance(filename, (tuple, list)):
                    filename = filename[0]
            self.load_pascal_xml_by_filename(filename)

    def open_dir_dialog(self, _value=False, dirpath=None, silent=False):
        if not self.may_continue():
            return

        if self.last_open_dir and os.path.exists(self.last_open_dir):
            default_open_dir_path = self.last_open_dir
        elif hasattr(self, 'filename'):
            default_open_dir_path = Path(self.file_path).parent if self.file_path else '.'
        else:
            default_open_dir_path = ''

        if not silent:
            target_dir = QFileDialog.getExistingDirectory(self,
                                                          '%s - Open Directory' % __appname__, default_open_dir_path,
                                                          QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        else:
            target_dir = dirpath

        if not target_dir:
            raise ValueError("Failed to add new directory")

        self.last_open_dir = target_dir
        self.cur_active_dir = target_dir.replace("/", "\\")

        if target_dir not in self.active_dirs:
            self.active_dirs.append(Path(target_dir))
            self.active_dir_list_widget.addItem(target_dir)
            self.import_dir_images(target_dir)

    def import_dir_images(self, dir_path):
        if not self.may_continue() or not dir_path:
            return

        self.last_open_dir = dir_path
        self.dir_name = dir_path
        self.file_path = None
        self.file_list_widget.clear()
        self.create_m_img_list()
        self.open_next_image()
        if self.m_img_list:
            if len(self.m_img_list) > 1:
                self.com_img_path = Path(os.path.commonpath(self.m_img_list))
            else:
                self.com_img_path = Path(self.m_img_list[0]).parent

            short_com_img_dir = self.com_img_path.as_posix().replace(Path.home().as_posix(), "~")
            item = QListWidgetItem(f"📂 {short_com_img_dir}")
            item.setFlags(item.flags() & ~Qt.ItemIsSelectable & ~Qt.ItemIsEnabled)
            self.file_list_widget.addItem(item)

        for imgPath in self.m_img_list:
            item_name = os.path.relpath(imgPath, self.com_img_path).replace("\\", "/")
            item = QListWidgetItem(f"📷 {item_name}")
            self.file_list_widget.addItem(item)

    def sort_img_list(self):
        self.m_img_list = list(filter(lambda img: re.match(image_name_pattern, os.path.basename(img)), self.m_img_list))
        self.m_img_list.sort(key=lambda img: re.match(pulse_count_pattern, os.path.basename(img)).groups()[0])
        self.m_img_list.sort(key=lambda img: re.match(rail_pattern, os.path.basename(img)).groups()[0])
        self.m_img_list.sort(key=lambda img: re.match(datasource_pattern, os.path.basename(img)).groups()[0])

    def verify_image(self, _value=False):
        if self.file_path is not None:
            try:
                self.label_file.toggle_verify()
            except AttributeError:
                # If the labeling file does not exist yet, create if and
                # re-save it with the verified attribute.
                self.save_file()
                if self.label_file is not None:
                    self.label_file.toggle_verify()
                else:
                    return

            self.canvas.verified = self.label_file.verified
            self.paint_canvas()
            self.save_file()

    def create_m_img_list(self):
        """
        recreates the image list from the active directories
        """
        self.m_img_list = self.scan_all_images()
        self.sort_img_list()
        self.img_count = len(self.m_img_list)

    def open_prev_image(self, _value=False):
        if self.auto_saving.isChecked():
            if self.default_save_dir is not None:
                if self.dirty is True:
                    self.save_file()
            else:
                self.change_save_dir_dialog()
                return

        if not self.may_continue():
            return

        if self.img_count <= 0:
            return

        if self.file_path is None:
            return

        if self.cur_img_idx - 1 >= 0:
            self.cur_img_idx -= 1
            filename = self.m_img_list[self.cur_img_idx]
            if filename:
                self.load_file(filename)

    def open_next_image(self, _value=False):
        # Processing prev image without a dialog if it has a label
        if self.auto_saving.isChecked():
            if self.default_save_dir is not None:
                if self.dirty is True:
                    self.save_file()
            else:
                self.change_save_dir_dialog()
                return

        if not self.may_continue():
            return

        if self.img_count <= 0:
            return

        filename = None
        if self.file_path is None:
            filename = self.m_img_list[0]
            self.cur_img_idx = 0
        else:
            if self.cur_img_idx + 1 < self.img_count:
                self.cur_img_idx += 1
                filename = Path(self.m_img_list[self.cur_img_idx])

        if filename:
            self.load_file(filename)

    def save_file(self, _value=False):

        # Saving the new annotation

        ## Setup
        if not self.file_path:
            raise ValueError("There is no file to save, the app shouldn't allow the user to save at this point")

        image_file_dir = Path(self.file_path).parent
        label_file_name = self.file_path.stem + XML_EXT

        ## Delete old annotation file
        old_ann_path = self.scan_all_for_file(label_file_name)
        if old_ann_path:
            if os.path.exists(old_ann_path):
                os.remove(old_ann_path)

        ## Create and save a new annotation file
        if self.cur_active_dir:
            label_path = self.cur_active_dir / label_file_name
        else:
            label_path = image_file_dir / label_file_name
            label_path = label_path if self.label_file else self.save_file_dialog(remove_ext=False)

        self._save_file(label_path)
        self.move_image_to_active_dir()

    def save_file_as(self, _value=False):
        assert not self.image.isNull(), "cannot save empty image"
        self._save_file(self.save_file_dialog())

    def save_file_dialog(self, remove_ext=True):
        caption = '%s - Choose File' % __appname__  # noqa
        filters = 'File (*%s)' % LabelFile.suffix
        open_dialog_path = self.current_path()
        dlg = QFileDialog(self, caption, open_dialog_path, filters)
        dlg.setDefaultSuffix(LabelFile.suffix[1:])
        dlg.setAcceptMode(QFileDialog.AcceptSave)
        filename_without_extension = os.path.splitext(self.file_path)[0]
        dlg.selectFile(filename_without_extension)
        dlg.setOption(QFileDialog.DontUseNativeDialog, False)
        if dlg.exec_():
            full_file_path = ustr(dlg.selectedFiles()[0])
            if remove_ext:
                return os.path.splitext(full_file_path)[0]  # Return a file path without the extension.
            else:
                return full_file_path
        return ''

    def _save_file(self, annotation_file_path):
        if annotation_file_path and self.save_labels(annotation_file_path):
            self.set_clean()
            self.statusBar().showMessage('Saved to  %s' % annotation_file_path)
            self.statusBar().show()

    def close_file(self, _value=False):
        if not self.may_continue():
            return
        self.reset_state()
        self.set_clean()
        self.toggle_actions(False)
        self.canvas.setEnabled(False)
        self.actions.saveAs.setEnabled(False)

    def delete_image(self):
        delete_path = self.file_path
        if delete_path is not None:
            self.open_next_image()
            self.cur_img_idx -= 1
            self.img_count -= 1
            if os.path.exists(delete_path):
                os.remove(delete_path)
            self.import_dir_images(self.last_open_dir)

    def reset_all(self):
        self.settings.reset()
        self.close()
        process = QProcess()
        process.startDetached(os.path.abspath(__file__))

    def may_continue(self):
        if not self.dirty:
            return True
        else:
            discard_changes = self.discard_changes_dialog()
            if discard_changes == QMessageBox.No:
                return True
            elif discard_changes == QMessageBox.Yes:
                self.save_file()
                return True
            else:
                return False

    def discard_changes_dialog(self):
        yes, no, cancel = QMessageBox.Yes, QMessageBox.No, QMessageBox.Cancel
        msg = u'You have unsaved changes, would you like to save them and proceed?\nClick "No" to undo all changes.'
        return QMessageBox.warning(self, u'Attention', msg, yes | no | cancel)

    def error_message(self, title, message):
        return QMessageBox.critical(self, title,
                                    '<p><b>%s</b></p>%s' % (title, message))

    def current_path(self):
        return Path(self.file_path).parent if self.file_path else '.'

    def choose_color1(self):
        color = self.color_dialog.getColor(self.line_color, u'Choose line color',
                                           default=DEFAULT_LINE_COLOR)
        if color:
            self.line_color = color
            Shape.line_color = color
            self.canvas.set_drawing_color(color)
            self.canvas.update()
            self.set_dirty()

    def delete_selected_shape(self):
        self.remove_label(self.canvas.delete_selected())
        self.set_dirty()
        if self.no_shapes():
            for action in self.actions.onShapesPresent:
                action.setEnabled(False)

    def choose_shape_line_color(self):
        color = self.color_dialog.getColor(self.line_color, u'Choose Line Color',
                                           default=DEFAULT_LINE_COLOR)
        if color:
            self.canvas.selected_shape.line_color = color
            self.canvas.update()
            self.set_dirty()

    def choose_shape_fill_color(self):
        color = self.color_dialog.getColor(self.fill_color, u'Choose Fill Color',
                                           default=DEFAULT_FILL_COLOR)
        if color:
            self.canvas.selected_shape.fill_color = color
            self.canvas.update()
            self.set_dirty()

    def copy_shape(self):
        self.canvas.end_move(copy=True)
        self.add_label(self.canvas.selected_shape)
        self.set_dirty()

    def move_shape(self):
        self.canvas.end_move(copy=False)
        self.set_dirty()

    def load_predefined_classes(self, predef_classes_file):
        if os.path.exists(predef_classes_file) is True:
            with codecs.open(predef_classes_file, 'r', 'utf8') as f:
                for line in f:
                    line = line.strip()
                    if self.label_hist is None:
                        self.label_hist = [line]
                    else:
                        self.label_hist.append(line)

    def load_pascal_xml_by_filename(self, xml_path):
        if self.file_path is None:
            return
        if xml_path.is_file() is False:
            return

        self.set_format(FORMAT_PASCALVOC)

        t_voc_parse_reader = PascalVocReader(xml_path.as_posix())
        shapes = t_voc_parse_reader.get_shapes()
        self.load_labels(shapes)
        self.canvas.verified = t_voc_parse_reader.verified

    def load_yolo_txt_by_filename(self, txt_path):
        if self.file_path is None:
            return
        if os.path.isfile(txt_path) is False:
            return

        self.set_format(FORMAT_YOLO)
        t_yolo_parse_reader = YoloReader(txt_path, self.image)
        shapes = t_yolo_parse_reader.get_shapes()
        print(shapes)
        self.load_labels(shapes)
        self.canvas.verified = t_yolo_parse_reader.verified

    def load_create_ml_json_by_filename(self, json_path, file_path):
        if self.file_path is None:
            return
        if os.path.isfile(json_path) is False:
            return

        self.set_format(FORMAT_CREATEML)

        create_ml_parse_reader = CreateMLReader(json_path, file_path)
        shapes = create_ml_parse_reader.get_shapes()
        self.load_labels(shapes)
        self.canvas.verified = create_ml_parse_reader.verified

    def copy_previous_bounding_boxes(self):
        current_index = self.m_img_list.index(self.file_path)
        if current_index - 1 >= 0:
            prev_file_path = self.m_img_list[current_index - 1]
            self.show_bounding_box_from_annotation_file(prev_file_path)
            self.save_file()

    def toggle_paint_labels_option(self):
        for shape in self.canvas.shapes:
            shape.paint_label = self.display_label_option.isChecked()

    def toggle_draw_square(self):
        self.canvas.set_drawing_shape_to_square(self.draw_squares_option.isChecked())


def inverted(color):
    return QColor(*[255 - v for v in color.getRgb()])


def read(filename, default=None):
    """
    Reads an image from the given filename and returns a
    QImage or the given default value if the image cannot
    be read.

    :param filename: The filename of the image.
    :param default: The default value to be returned if the image cannot be read.
    :return: A QImage or the default value.
    """
    try:
        reader = QImageReader(filename)
        reader.setAutoTransform(True)
        return reader.read()
    except:  # noqa
        return default


def get_main_app(argv=[]):  # noqa
    """
    Standard boilerplate Qt application code.
    Do everything but app.exec_() -- so that we can test the application in one thread
    """
    app = QApplication(argv)
    app.setApplicationName(__appname__)
    app.setWindowIcon(new_icon("app"))
    # Accept extra arguments to change a predefined class file
    argparser = argparse.ArgumentParser()
    argparser.add_argument("image_dir", nargs="?")
    argparser.add_argument(
        "class_file",
        default=Path(__file__).parent / "data" / "predefined_classes.txt",
        nargs="?"
    )
    argparser.add_argument("save_dir", nargs="?")
    args = argparser.parse_args(argv[1:])

    args.image_dir = args.image_dir and Path(args.image_dir).absolute().as_posix()
    args.class_file = args.class_file and Path(args.class_file).absolute().as_posix()
    args.save_dir = args.save_dir and Path(args.save_dir).absolute().as_posix()

    # Usage : app.py image classFile saveDir
    win = MainWindow(args.image_dir,
                     args.class_file,
                     args.save_dir)
    win.show()
    return app, win


def main():
    """construct the main app and run it"""
    app, _win = get_main_app(sys.argv)
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())
