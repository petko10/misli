# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'misliwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MisliWindow(object):
    def setupUi(self, MisliWindow):
        if not MisliWindow.objectName():
            MisliWindow.setObjectName(u"MisliWindow")
        MisliWindow.resize(800, 600)
        self.actionCopy = QAction(MisliWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MisliWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionCut = QAction(MisliWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionUndo = QAction(MisliWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionHelp = QAction(MisliWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionAdd_new = QAction(MisliWindow)
        self.actionAdd_new.setObjectName(u"actionAdd_new")
        self.actionAdd_new.setCheckable(False)
        self.actionRemove_current = QAction(MisliWindow)
        self.actionRemove_current.setObjectName(u"actionRemove_current")
        self.actionEdit_note = QAction(MisliWindow)
        self.actionEdit_note.setObjectName(u"actionEdit_note")
        self.actionNew_note = QAction(MisliWindow)
        self.actionNew_note.setObjectName(u"actionNew_note")
        self.actionNew_notefile = QAction(MisliWindow)
        self.actionNew_notefile.setObjectName(u"actionNew_notefile")
        self.actionNew_notefile.setCheckable(False)
        self.actionNew_notefile.setChecked(False)
        self.actionMake_link = QAction(MisliWindow)
        self.actionMake_link.setObjectName(u"actionMake_link")
        self.actionNext_notefile = QAction(MisliWindow)
        self.actionNext_notefile.setObjectName(u"actionNext_notefile")
        self.actionPrevious_notefile = QAction(MisliWindow)
        self.actionPrevious_notefile.setObjectName(u"actionPrevious_notefile")
        self.actionDelete_selected = QAction(MisliWindow)
        self.actionDelete_selected.setObjectName(u"actionDelete_selected")
        self.actionZoom_in = QAction(MisliWindow)
        self.actionZoom_in.setObjectName(u"actionZoom_in")
        self.actionZoom_out = QAction(MisliWindow)
        self.actionZoom_out.setObjectName(u"actionZoom_out")
        self.actionMake_this_view_point_default_for_the_notefile = QAction(MisliWindow)
        self.actionMake_this_view_point_default_for_the_notefile.setObjectName(u"actionMake_this_view_point_default_for_the_notefile")
        self.actionMake_this_notefile_appear_first_on_program_start = QAction(MisliWindow)
        self.actionMake_this_notefile_appear_first_on_program_start.setObjectName(u"actionMake_this_notefile_appear_first_on_program_start")
        self.actionClose = QAction(MisliWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionBulgarian = QAction(MisliWindow)
        self.actionBulgarian.setObjectName(u"actionBulgarian")
        self.actionEnglish = QAction(MisliWindow)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionClear_settings_and_exit = QAction(MisliWindow)
        self.actionClear_settings_and_exit.setObjectName(u"actionClear_settings_and_exit")
        self.actionRename_notefile = QAction(MisliWindow)
        self.actionRename_notefile.setObjectName(u"actionRename_notefile")
        self.actionDelete_notefile = QAction(MisliWindow)
        self.actionDelete_notefile.setObjectName(u"actionDelete_notefile")
        self.actionColor_blue = QAction(MisliWindow)
        self.actionColor_blue.setObjectName(u"actionColor_blue")
        self.actionColor_green = QAction(MisliWindow)
        self.actionColor_green.setObjectName(u"actionColor_green")
        self.actionColor_red = QAction(MisliWindow)
        self.actionColor_red.setObjectName(u"actionColor_red")
        self.actionColor_black = QAction(MisliWindow)
        self.actionColor_black.setObjectName(u"actionColor_black")
        self.actionMove_down = QAction(MisliWindow)
        self.actionMove_down.setObjectName(u"actionMove_down")
        self.actionMove_up = QAction(MisliWindow)
        self.actionMove_up.setObjectName(u"actionMove_up")
        self.actionMove_left = QAction(MisliWindow)
        self.actionMove_left.setObjectName(u"actionMove_left")
        self.actionMove_right = QAction(MisliWindow)
        self.actionMove_right.setObjectName(u"actionMove_right")
        self.actionSearch = QAction(MisliWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionSearch.setCheckable(True)
        self.actionSelect_all_notes = QAction(MisliWindow)
        self.actionSelect_all_notes.setObjectName(u"actionSelect_all_notes")
        self.actionJump_to_nearest_note = QAction(MisliWindow)
        self.actionJump_to_nearest_note.setObjectName(u"actionJump_to_nearest_note")
        self.actionDetails = QAction(MisliWindow)
        self.actionDetails.setObjectName(u"actionDetails")
        self.actionAbout = QAction(MisliWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSelect_note_under_mouse = QAction(MisliWindow)
        self.actionSelect_note_under_mouse.setObjectName(u"actionSelect_note_under_mouse")
        self.actionCreate_note_from_the_clipboard_text = QAction(MisliWindow)
        self.actionCreate_note_from_the_clipboard_text.setObjectName(u"actionCreate_note_from_the_clipboard_text")
        self.actionTransparent_background = QAction(MisliWindow)
        self.actionTransparent_background.setObjectName(u"actionTransparent_background")
        self.actionSet_this_height_as_default = QAction(MisliWindow)
        self.actionSet_this_height_as_default.setObjectName(u"actionSet_this_height_as_default")
        self.actionCopy_donation_address = QAction(MisliWindow)
        self.actionCopy_donation_address.setObjectName(u"actionCopy_donation_address")
        self.actionSelect_all_red_notes = QAction(MisliWindow)
        self.actionSelect_all_red_notes.setObjectName(u"actionSelect_all_red_notes")
        self.actionRedo = QAction(MisliWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCheck_for_updates = QAction(MisliWindow)
        self.actionCheck_for_updates.setObjectName(u"actionCheck_for_updates")
        self.actionCheck_for_updates.setCheckable(True)
        self.actionCheck_for_updates.setChecked(False)
        self.actionDownload_it = QAction(MisliWindow)
        self.actionDownload_it.setObjectName(u"actionDownload_it")
        self.actionGotoTab1 = QAction(MisliWindow)
        self.actionGotoTab1.setObjectName(u"actionGotoTab1")
        self.actionGotoTab2 = QAction(MisliWindow)
        self.actionGotoTab2.setObjectName(u"actionGotoTab2")
        self.actionSwitch_to_the_last_note_file = QAction(MisliWindow)
        self.actionSwitch_to_the_last_note_file.setObjectName(u"actionSwitch_to_the_last_note_file")
        self.actionExport_all_as_web_notes = QAction(MisliWindow)
        self.actionExport_all_as_web_notes.setObjectName(u"actionExport_all_as_web_notes")
        self.actionToggle_tags_view = QAction(MisliWindow)
        self.actionToggle_tags_view.setObjectName(u"actionToggle_tags_view")
        self.actionToggle_tags_view.setCheckable(True)
        self.actionToggle_tag = QAction(MisliWindow)
        self.actionToggle_tag.setObjectName(u"actionToggle_tag")
        self.actionUse_JSON_format = QAction(MisliWindow)
        self.actionUse_JSON_format.setObjectName(u"actionUse_JSON_format")
        self.actionMigrate_to_JSON_format = QAction(MisliWindow)
        self.actionMigrate_to_JSON_format.setObjectName(u"actionMigrate_to_JSON_format")
        self.centralwidget = QWidget(MisliWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchScopeComboBox = QComboBox(self.centralwidget)
        self.searchScopeComboBox.setObjectName(u"searchScopeComboBox")

        self.verticalLayout.addWidget(self.searchScopeComboBox)

        self.searchLineEdit = QLineEdit(self.centralwidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.searchLineEdit)

        self.searchListView = QListView(self.centralwidget)
        self.searchListView.setObjectName(u"searchListView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchListView.sizePolicy().hasHeightForWidth())
        self.searchListView.setSizePolicy(sizePolicy1)
        self.searchListView.setProperty("isWrapping", False)
        self.searchListView.setResizeMode(QListView.Adjust)
        self.searchListView.setWordWrap(True)

        self.verticalLayout.addWidget(self.searchListView)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.jumpToNearestNotePushButton = QPushButton(self.centralwidget)
        self.jumpToNearestNotePushButton.setObjectName(u"jumpToNearestNotePushButton")

        self.mainLayout.addWidget(self.jumpToNearestNotePushButton)

        self.addMisliDirPushButton = QPushButton(self.centralwidget)
        self.addMisliDirPushButton.setObjectName(u"addMisliDirPushButton")

        self.mainLayout.addWidget(self.addMisliDirPushButton)

        self.makeNoteFilePushButton = QPushButton(self.centralwidget)
        self.makeNoteFilePushButton.setObjectName(u"makeNoteFilePushButton")

        self.mainLayout.addWidget(self.makeNoteFilePushButton)

        self.tagGUI = QWidget(self.centralwidget)
        self.tagGUI.setObjectName(u"tagGUI")
        self.verticalLayout_2 = QVBoxLayout(self.tagGUI)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tagFirstRowHLayout = QHBoxLayout()
        self.tagFirstRowHLayout.setObjectName(u"tagFirstRowHLayout")
        self.tagTextLabel = QLabel(self.tagGUI)
        self.tagTextLabel.setObjectName(u"tagTextLabel")

        self.tagFirstRowHLayout.addWidget(self.tagTextLabel)

        self.tagTextLineEdit = QLineEdit(self.tagGUI)
        self.tagTextLineEdit.setObjectName(u"tagTextLineEdit")

        self.tagFirstRowHLayout.addWidget(self.tagTextLineEdit)

        self.exitTagModeButton = QPushButton(self.tagGUI)
        self.exitTagModeButton.setObjectName(u"exitTagModeButton")

        self.tagFirstRowHLayout.addWidget(self.exitTagModeButton)


        self.verticalLayout_2.addLayout(self.tagFirstRowHLayout)


        self.mainLayout.addWidget(self.tagGUI)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)

        self.mainLayout.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.mainLayout)

        MisliWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MisliWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit.setToolTipsVisible(True)
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setToolTipsVisible(True)
        self.menuFolders = QMenu(self.menubar)
        self.menuFolders.setObjectName(u"menuFolders")
        self.menuFolders.setToolTipsVisible(True)
        self.menuNoteFile = QMenu(self.menubar)
        self.menuNoteFile.setObjectName(u"menuNoteFile")
        self.menuNoteFile.setToolTipsVisible(True)
        self.menuSwitch_to_another_note_file = QMenu(self.menuNoteFile)
        self.menuSwitch_to_another_note_file.setObjectName(u"menuSwitch_to_another_note_file")
        self.menuNote = QMenu(self.menubar)
        self.menuNote.setObjectName(u"menuNote")
        self.menuNote.setToolTipsVisible(True)
        self.menuColor = QMenu(self.menuNote)
        self.menuColor.setObjectName(u"menuColor")
        self.menuColor.setToolTipsVisible(True)
        self.menuOther = QMenu(self.menubar)
        self.menuOther.setObjectName(u"menuOther")
        self.menuOther.setToolTipsVisible(True)
        self.menuNavigation = QMenu(self.menuOther)
        self.menuNavigation.setObjectName(u"menuNavigation")
        self.menuNavigation.setToolTipsVisible(True)
        self.menuDonate_Bitcoin = QMenu(self.menuOther)
        self.menuDonate_Bitcoin.setObjectName(u"menuDonate_Bitcoin")
        self.menuLanguage = QMenu(self.menubar)
        self.menuLanguage.setObjectName(u"menuLanguage")
        self.menuLanguage.setToolTipsVisible(True)
        MisliWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFolders.menuAction())
        self.menubar.addAction(self.menuNoteFile.menuAction())
        self.menubar.addAction(self.menuNote.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionCreate_note_from_the_clipboard_text)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionDelete_selected)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFolders.addAction(self.actionAdd_new)
        self.menuFolders.addAction(self.actionRemove_current)
        self.menuFolders.addSeparator()
        self.menuNoteFile.addAction(self.actionNew_notefile)
        self.menuNoteFile.addAction(self.actionRename_notefile)
        self.menuNoteFile.addAction(self.actionDelete_notefile)
        self.menuNoteFile.addSeparator()
        self.menuNoteFile.addSeparator()
        self.menuNoteFile.addAction(self.actionMake_this_view_point_default_for_the_notefile)
        self.menuNoteFile.addAction(self.actionSet_this_height_as_default)
        self.menuNoteFile.addAction(self.actionMake_this_notefile_appear_first_on_program_start)
        self.menuNoteFile.addSeparator()
        self.menuNoteFile.addAction(self.actionSelect_all_notes)
        self.menuNoteFile.addAction(self.actionSelect_all_red_notes)
        self.menuNoteFile.addSeparator()
        self.menuNoteFile.addAction(self.menuSwitch_to_another_note_file.menuAction())
        self.menuNoteFile.addAction(self.actionSwitch_to_the_last_note_file)
        self.menuNoteFile.addSeparator()
        self.menuNoteFile.addAction(self.actionToggle_tags_view)
        self.menuNote.addAction(self.actionNew_note)
        self.menuNote.addAction(self.actionEdit_note)
        self.menuNote.addAction(self.actionMake_link)
        self.menuNote.addAction(self.menuColor.menuAction())
        self.menuNote.addAction(self.actionToggle_tag)
        self.menuColor.addAction(self.actionColor_blue)
        self.menuColor.addAction(self.actionColor_green)
        self.menuColor.addAction(self.actionColor_red)
        self.menuColor.addAction(self.actionColor_black)
        self.menuColor.addAction(self.actionTransparent_background)
        self.menuOther.addAction(self.menuNavigation.menuAction())
        self.menuOther.addAction(self.actionClear_settings_and_exit)
        self.menuOther.addAction(self.actionSearch)
        self.menuOther.addAction(self.actionJump_to_nearest_note)
        self.menuOther.addAction(self.menuDonate_Bitcoin.menuAction())
        self.menuOther.addAction(self.actionExport_all_as_web_notes)
        self.menuNavigation.addAction(self.actionZoom_in)
        self.menuNavigation.addAction(self.actionZoom_out)
        self.menuNavigation.addAction(self.actionMove_down)
        self.menuNavigation.addAction(self.actionMove_up)
        self.menuNavigation.addAction(self.actionMove_left)
        self.menuNavigation.addAction(self.actionMove_right)
        self.menuDonate_Bitcoin.addAction(self.actionCopy_donation_address)
        self.menuLanguage.addAction(self.actionBulgarian)
        self.menuLanguage.addAction(self.actionEnglish)

        self.retranslateUi(MisliWindow)
        self.actionClose.triggered.connect(self.actionToggle_tag.toggle)
        self.actionSearch.toggled.connect(self.searchLineEdit.setVisible)
        self.actionSearch.toggled.connect(self.searchListView.setVisible)
        self.actionSearch.triggered.connect(self.searchLineEdit.setFocus)
        self.actionSearch.toggled.connect(self.searchScopeComboBox.setVisible)
        self.tagTextLineEdit.textChanged.connect(self.tabWidget.update)
        self.jumpToNearestNotePushButton.clicked.connect(self.actionJump_to_nearest_note.trigger)

        QMetaObject.connectSlotsByName(MisliWindow)
    # setupUi

    def retranslateUi(self, MisliWindow):
        MisliWindow.setWindowTitle(QCoreApplication.translate("MisliWindow", u"MainWindow", None))
        self.actionCopy.setText(QCoreApplication.translate("MisliWindow", u"&Copy", None))
#if QT_CONFIG(tooltip)
        self.actionCopy.setToolTip(QCoreApplication.translate("MisliWindow", u"Copies notes to the internal clipboard, and copies their text to the regular clipboard.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MisliWindow", u"&Paste", None))
#if QT_CONFIG(tooltip)
        self.actionPaste.setToolTip(QCoreApplication.translate("MisliWindow", u"Pastes the notes from the internal clipboard.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("MisliWindow", u"Cut", None))
#if QT_CONFIG(tooltip)
        self.actionCut.setToolTip(QCoreApplication.translate("MisliWindow", u"See the tooltip of \"Copy\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndo.setText(QCoreApplication.translate("MisliWindow", u"&Undo", None))
#if QT_CONFIG(tooltip)
        self.actionUndo.setToolTip(QCoreApplication.translate("MisliWindow", u"Reverts the last action. The max is 30 undo steps. (note there is no Redo for now)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelp.setText(QCoreApplication.translate("MisliWindow", u"&Help", None))
#if QT_CONFIG(tooltip)
        self.actionHelp.setToolTip(QCoreApplication.translate("MisliWindow", u"Shows the help notefile.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(QCoreApplication.translate("MisliWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionAdd_new.setText(QCoreApplication.translate("MisliWindow", u"&Add another folder", None))
        self.actionRemove_current.setText(QCoreApplication.translate("MisliWindow", u"&Remove current", None))
#if QT_CONFIG(tooltip)
        self.actionRemove_current.setToolTip(QCoreApplication.translate("MisliWindow", u"Remove the current folder (does not delete the notefiles from the disk)", None))
#endif // QT_CONFIG(tooltip)
        self.actionEdit_note.setText(QCoreApplication.translate("MisliWindow", u"&Edit note", None))
#if QT_CONFIG(shortcut)
        self.actionEdit_note.setShortcut(QCoreApplication.translate("MisliWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew_note.setText(QCoreApplication.translate("MisliWindow", u"&New note", None))
#if QT_CONFIG(tooltip)
        self.actionNew_note.setToolTip(QCoreApplication.translate("MisliWindow", u"Create a new note", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNew_note.setShortcut(QCoreApplication.translate("MisliWindow", u"N", None))
#endif // QT_CONFIG(shortcut)
        self.actionNew_notefile.setText(QCoreApplication.translate("MisliWindow", u"&New notefile", None))
#if QT_CONFIG(tooltip)
        self.actionNew_notefile.setToolTip(QCoreApplication.translate("MisliWindow", u"Create a new notefile on the disk and open it to add notes.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNew_notefile.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionMake_link.setText(QCoreApplication.translate("MisliWindow", u"&Make link", None))
#if QT_CONFIG(tooltip)
        self.actionMake_link.setToolTip(QCoreApplication.translate("MisliWindow", u"Link notes with arrows to visualize their connections.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionMake_link.setShortcut(QCoreApplication.translate("MisliWindow", u"L", None))
#endif // QT_CONFIG(shortcut)
        self.actionNext_notefile.setText(QCoreApplication.translate("MisliWindow", u"Next notefile", None))
#if QT_CONFIG(tooltip)
        self.actionNext_notefile.setToolTip(QCoreApplication.translate("MisliWindow", u"Switch to the next notefile in the alphabetical order.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionNext_notefile.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+PgUp", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrevious_notefile.setText(QCoreApplication.translate("MisliWindow", u"Previous notefile", None))
#if QT_CONFIG(tooltip)
        self.actionPrevious_notefile.setToolTip(QCoreApplication.translate("MisliWindow", u"Switch to the previous notefile in thealphabetical order.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPrevious_notefile.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+PgDown", None))
#endif // QT_CONFIG(shortcut)
        self.actionDelete_selected.setText(QCoreApplication.translate("MisliWindow", u"&Delete selected", None))
#if QT_CONFIG(tooltip)
        self.actionDelete_selected.setToolTip(QCoreApplication.translate("MisliWindow", u"Delete selected notes.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionDelete_selected.setShortcut(QCoreApplication.translate("MisliWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionZoom_in.setText(QCoreApplication.translate("MisliWindow", u"&Zoom in", None))
#if QT_CONFIG(tooltip)
        self.actionZoom_in.setToolTip(QCoreApplication.translate("MisliWindow", u"Change the height of the viewpoint over the canvas.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionZoom_in.setShortcut(QCoreApplication.translate("MisliWindow", u"PgDown", None))
#endif // QT_CONFIG(shortcut)
        self.actionZoom_out.setText(QCoreApplication.translate("MisliWindow", u"Zoom &out", None))
#if QT_CONFIG(tooltip)
        self.actionZoom_out.setToolTip(QCoreApplication.translate("MisliWindow", u"Change the height of the viewpoint over the canvas.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionZoom_out.setShortcut(QCoreApplication.translate("MisliWindow", u"PgUp", None))
#endif // QT_CONFIG(shortcut)
        self.actionMake_this_view_point_default_for_the_notefile.setText(QCoreApplication.translate("MisliWindow", u"&Make this view point default for the notefile", None))
#if QT_CONFIG(tooltip)
        self.actionMake_this_view_point_default_for_the_notefile.setToolTip(QCoreApplication.translate("MisliWindow", u"Fix the current viewpoint (height excluded) in the notefile as default on program start.", None))
#endif // QT_CONFIG(tooltip)
        self.actionMake_this_notefile_appear_first_on_program_start.setText(QCoreApplication.translate("MisliWindow", u"Make this notefile appear first &on program start", None))
#if QT_CONFIG(tooltip)
        self.actionMake_this_notefile_appear_first_on_program_start.setToolTip(QCoreApplication.translate("MisliWindow", u"Marks the notefile as default on program start for its folder.", None))
#endif // QT_CONFIG(tooltip)
        self.actionClose.setText(QCoreApplication.translate("MisliWindow", u"Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MisliWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionBulgarian.setText(QCoreApplication.translate("MisliWindow", u"\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438", None))
        self.actionEnglish.setText(QCoreApplication.translate("MisliWindow", u"&English", None))
#if QT_CONFIG(tooltip)
        self.actionEnglish.setToolTip(QCoreApplication.translate("MisliWindow", u"Change the language to english.", None))
#endif // QT_CONFIG(tooltip)
        self.actionClear_settings_and_exit.setText(QCoreApplication.translate("MisliWindow", u"&Clear settings and exit", None))
#if QT_CONFIG(tooltip)
        self.actionClear_settings_and_exit.setToolTip(QCoreApplication.translate("MisliWindow", u"Clear program settings and kill this instance.", None))
#endif // QT_CONFIG(tooltip)
        self.actionRename_notefile.setText(QCoreApplication.translate("MisliWindow", u"&Rename notefile", None))
#if QT_CONFIG(tooltip)
        self.actionRename_notefile.setToolTip(QCoreApplication.translate("MisliWindow", u"Also changes all of the notes that link to it to the new name.", None))
#endif // QT_CONFIG(tooltip)
        self.actionDelete_notefile.setText(QCoreApplication.translate("MisliWindow", u"&Delete notefile", None))
#if QT_CONFIG(tooltip)
        self.actionDelete_notefile.setToolTip(QCoreApplication.translate("MisliWindow", u"Delete the notefile permanetly (on the disk too).", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionDelete_notefile.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+Del", None))
#endif // QT_CONFIG(shortcut)
        self.actionColor_blue.setText(QCoreApplication.translate("MisliWindow", u"&Color blue", None))
#if QT_CONFIG(shortcut)
        self.actionColor_blue.setShortcut(QCoreApplication.translate("MisliWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.actionColor_green.setText(QCoreApplication.translate("MisliWindow", u"Color &green", None))
#if QT_CONFIG(shortcut)
        self.actionColor_green.setShortcut(QCoreApplication.translate("MisliWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.actionColor_red.setText(QCoreApplication.translate("MisliWindow", u"Color &red", None))
#if QT_CONFIG(shortcut)
        self.actionColor_red.setShortcut(QCoreApplication.translate("MisliWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.actionColor_black.setText(QCoreApplication.translate("MisliWindow", u"Color &black", None))
#if QT_CONFIG(shortcut)
        self.actionColor_black.setShortcut(QCoreApplication.translate("MisliWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_down.setText(QCoreApplication.translate("MisliWindow", u"&Move down", None))
#if QT_CONFIG(shortcut)
        self.actionMove_down.setShortcut(QCoreApplication.translate("MisliWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_up.setText(QCoreApplication.translate("MisliWindow", u"Move &up", None))
#if QT_CONFIG(shortcut)
        self.actionMove_up.setShortcut(QCoreApplication.translate("MisliWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_left.setText(QCoreApplication.translate("MisliWindow", u"Move &left", None))
#if QT_CONFIG(shortcut)
        self.actionMove_left.setShortcut(QCoreApplication.translate("MisliWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.actionMove_right.setText(QCoreApplication.translate("MisliWindow", u"Move &right", None))
#if QT_CONFIG(shortcut)
        self.actionMove_right.setShortcut(QCoreApplication.translate("MisliWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.actionSearch.setText(QCoreApplication.translate("MisliWindow", u"&Search ", None))
#if QT_CONFIG(tooltip)
        self.actionSearch.setToolTip(QCoreApplication.translate("MisliWindow", u"Search in all notes. Click in the results shown under the search field to go to the note.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSearch.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actionSelect_all_notes.setText(QCoreApplication.translate("MisliWindow", u"S&elect all notes", None))
#if QT_CONFIG(shortcut)
        self.actionSelect_all_notes.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionJump_to_nearest_note.setText(QCoreApplication.translate("MisliWindow", u"&Jump to nearest note", None))
#if QT_CONFIG(shortcut)
        self.actionJump_to_nearest_note.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+J", None))
#endif // QT_CONFIG(shortcut)
        self.actionDetails.setText(QCoreApplication.translate("MisliWindow", u"Details", None))
#if QT_CONFIG(shortcut)
        self.actionDetails.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MisliWindow", u"&About", None))
        self.actionSelect_note_under_mouse.setText(QCoreApplication.translate("MisliWindow", u"Select note under mouse", None))
#if QT_CONFIG(shortcut)
        self.actionSelect_note_under_mouse.setShortcut(QCoreApplication.translate("MisliWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.actionCreate_note_from_the_clipboard_text.setText(QCoreApplication.translate("MisliWindow", u"Create &note from the clipboard text", None))
#if QT_CONFIG(tooltip)
        self.actionCreate_note_from_the_clipboard_text.setToolTip(QCoreApplication.translate("MisliWindow", u"Create note from the text in the regular clipboard.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionCreate_note_from_the_clipboard_text.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+Shift+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionTransparent_background.setText(QCoreApplication.translate("MisliWindow", u"&Transparent background", None))
#if QT_CONFIG(tooltip)
        self.actionTransparent_background.setToolTip(QCoreApplication.translate("MisliWindow", u"Changes only the background color of the note to be transparent.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionTransparent_background.setShortcut(QCoreApplication.translate("MisliWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.actionSet_this_height_as_default.setText(QCoreApplication.translate("MisliWindow", u"&Set this height as default", None))
#if QT_CONFIG(tooltip)
        self.actionSet_this_height_as_default.setToolTip(QCoreApplication.translate("MisliWindow", u"Set the current height as default for all files on startup.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionSet_this_height_as_default.setStatusTip(QCoreApplication.translate("MisliWindow", u"Set the current height as default for all files on startup.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.actionSet_this_height_as_default.setWhatsThis(QCoreApplication.translate("MisliWindow", u"Set the current height as default for all files on startup.", None))
#endif // QT_CONFIG(whatsthis)
        self.actionCopy_donation_address.setText(QCoreApplication.translate("MisliWindow", u"&Copy donation address", None))
        self.actionSelect_all_red_notes.setText(QCoreApplication.translate("MisliWindow", u"Se&lect all red notes", None))
#if QT_CONFIG(shortcut)
        self.actionSelect_all_red_notes.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MisliWindow", u"&Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+Shift+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionCheck_for_updates.setText(QCoreApplication.translate("MisliWindow", u"Check for updates", None))
        self.actionDownload_it.setText(QCoreApplication.translate("MisliWindow", u"Download it", None))
        self.actionGotoTab1.setText(QCoreApplication.translate("MisliWindow", u"gotoTab1", None))
#if QT_CONFIG(shortcut)
        self.actionGotoTab1.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.actionGotoTab2.setText(QCoreApplication.translate("MisliWindow", u"gotoTab2", None))
#if QT_CONFIG(shortcut)
        self.actionGotoTab2.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.actionSwitch_to_the_last_note_file.setText(QCoreApplication.translate("MisliWindow", u"S&witch to the last note file", None))
#if QT_CONFIG(shortcut)
        self.actionSwitch_to_the_last_note_file.setShortcut(QCoreApplication.translate("MisliWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.actionExport_all_as_web_notes.setText(QCoreApplication.translate("MisliWindow", u"&Export all as web notes", None))
        self.actionToggle_tags_view.setText(QCoreApplication.translate("MisliWindow", u"Toggle tags view", None))
#if QT_CONFIG(shortcut)
        self.actionToggle_tags_view.setShortcut(QCoreApplication.translate("MisliWindow", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
        self.actionToggle_tag.setText(QCoreApplication.translate("MisliWindow", u"Toggle tag", None))
#if QT_CONFIG(shortcut)
        self.actionToggle_tag.setShortcut(QCoreApplication.translate("MisliWindow", u"T", None))
#endif // QT_CONFIG(shortcut)
        self.actionUse_JSON_format.setText(QCoreApplication.translate("MisliWindow", u"Use JSON format", None))
        self.actionMigrate_to_JSON_format.setText(QCoreApplication.translate("MisliWindow", u"Migrate to JSON format", None))
        self.jumpToNearestNotePushButton.setText(QCoreApplication.translate("MisliWindow", u"Jump to the nearest note", None))
        self.addMisliDirPushButton.setText(QCoreApplication.translate("MisliWindow", u"Add a directory for note files", None))
        self.makeNoteFilePushButton.setText(QCoreApplication.translate("MisliWindow", u"Make a new note file", None))
        self.tagTextLabel.setText(QCoreApplication.translate("MisliWindow", u"Tag label:", None))
        self.exitTagModeButton.setText(QCoreApplication.translate("MisliWindow", u"Exit tag mode", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MisliWindow", u"Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MisliWindow", u"Help", None))
        self.menuFolders.setTitle(QCoreApplication.translate("MisliWindow", u"Folders", None))
        self.menuNoteFile.setTitle(QCoreApplication.translate("MisliWindow", u"&NoteFile", None))
        self.menuSwitch_to_another_note_file.setTitle(QCoreApplication.translate("MisliWindow", u"Switch to another note &file", None))
        self.menuNote.setTitle(QCoreApplication.translate("MisliWindow", u"Note", None))
        self.menuColor.setTitle(QCoreApplication.translate("MisliWindow", u"&Color", None))
        self.menuOther.setTitle(QCoreApplication.translate("MisliWindow", u"Othe&r", None))
        self.menuNavigation.setTitle(QCoreApplication.translate("MisliWindow", u"&Navigation", None))
        self.menuDonate_Bitcoin.setTitle(QCoreApplication.translate("MisliWindow", u"&Donate Bitcoin", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MisliWindow", u"&Language", None))
    # retranslateUi

