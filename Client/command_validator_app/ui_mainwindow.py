﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Tue Jul  2 13:11:27 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(805, 554)
        mainWindow.setBaseSize(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Main = QtWidgets.QWidget()
        self.Main.setObjectName("Main")
        self.layoutWidget = QtWidgets.QWidget(self.Main)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 16, 507, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(30, 0, 30, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEditDDIInputPath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditDDIInputPath.setObjectName("lineEditDDIInputPath")
        self.gridLayout.addWidget(self.lineEditDDIInputPath, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(200, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.comboBoxPlatform = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPlatform.sizePolicy().hasHeightForWidth())
        self.comboBoxPlatform.setSizePolicy(sizePolicy)
        self.comboBoxPlatform.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBoxPlatform.setObjectName("comboBoxPlatform")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.gridLayout.addWidget(self.comboBoxPlatform, 4, 2, 1, 1)
        self.comboBoxComponent = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxComponent.sizePolicy().hasHeightForWidth())
        self.comboBoxComponent.setSizePolicy(sizePolicy)
        self.comboBoxComponent.setMaximumSize(QtCore.QSize(16777215, 25))
        self.comboBoxComponent.setObjectName("comboBoxComponent")
        self.comboBoxComponent.addItem("")
        self.comboBoxComponent.addItem("")
        self.comboBoxComponent.addItem("")
        self.comboBoxComponent.addItem("")
        self.comboBoxComponent.addItem("")
        self.comboBoxComponent.addItem("")
        self.comboBoxComponent.addItem("")
        self.comboBoxComponent.addItem("")
        self.gridLayout.addWidget(self.comboBoxComponent, 5, 2, 1, 1)
        self.SelectRinginfoPath = QtWidgets.QPushButton(self.layoutWidget)
        self.SelectRinginfoPath.setObjectName("SelectRinginfoPath")
        self.gridLayout.addWidget(self.SelectRinginfoPath, 2, 2, 1, 1)
        self.lineEditMediaPath = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditMediaPath.sizePolicy().hasHeightForWidth())
        self.lineEditMediaPath.setSizePolicy(sizePolicy)
        self.lineEditMediaPath.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEditMediaPath.setObjectName("lineEditMediaPath")
        self.gridLayout.addWidget(self.lineEditMediaPath, 1, 1, 1, 1)
        self.lineEditPlatform = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPlatform.setObjectName("lineEditPlatform")
        self.gridLayout.addWidget(self.lineEditPlatform, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEditComponent = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditComponent.setObjectName("lineEditComponent")
        self.gridLayout.addWidget(self.lineEditComponent, 5, 1, 1, 1)
        self.SelectMediaPath = QtWidgets.QPushButton(self.layoutWidget)
        self.SelectMediaPath.setObjectName("SelectMediaPath")
        self.gridLayout.addWidget(self.SelectMediaPath, 1, 2, 1, 1)
        self.lineEditTestName = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTestName.sizePolicy().hasHeightForWidth())
        self.lineEditTestName.setSizePolicy(sizePolicy)
        self.lineEditTestName.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEditTestName.setObjectName("lineEditTestName")
        self.gridLayout.addWidget(self.lineEditTestName, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditFrame = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFrame.sizePolicy().hasHeightForWidth())
        self.lineEditFrame.setSizePolicy(sizePolicy)
        self.lineEditFrame.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEditFrame.setObjectName("lineEditFrame")
        self.gridLayout.addWidget(self.lineEditFrame, 6, 1, 1, 1)
        self.lineEditRinginfoPath = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditRinginfoPath.sizePolicy().hasHeightForWidth())
        self.lineEditRinginfoPath.setSizePolicy(sizePolicy)
        self.lineEditRinginfoPath.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEditRinginfoPath.setText("")
        self.lineEditRinginfoPath.setObjectName("lineEditRinginfoPath")
        self.gridLayout.addWidget(self.lineEditRinginfoPath, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(180, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.SelectDDIInputPath = QtWidgets.QPushButton(self.layoutWidget)
        self.SelectDDIInputPath.setObjectName("SelectDDIInputPath")
        self.gridLayout.addWidget(self.SelectDDIInputPath, 3, 2, 1, 1)
        self.pushButtonGAll = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonGAll.sizePolicy().hasHeightForWidth())
        self.pushButtonGAll.setSizePolicy(sizePolicy)
        self.pushButtonGAll.setMinimumSize(QtCore.QSize(150, 40))
        self.pushButtonGAll.setMaximumSize(QtCore.QSize(150, 40))
        self.pushButtonGAll.setBaseSize(QtCore.QSize(200, 200))
        self.pushButtonGAll.setObjectName("pushButtonGAll")
        self.gridLayout.addWidget(self.pushButtonGAll, 7, 1, 1, 1)
        self.tabWidget.addTab(self.Main, "")
        self.Input = QtWidgets.QWidget()
        self.Input.setObjectName("Input")
        self.label_6 = QtWidgets.QLabel(self.Input)
        self.label_6.setGeometry(QtCore.QRect(69, 19, 371, 31))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.Input)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 499, 369))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Height = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Height.setFont(font)
        self.Height.setObjectName("Height")
        self.gridLayout_2.addWidget(self.Height, 7, 0, 1, 1)
        self.RawTileType_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.RawTileType_input.setObjectName("RawTileType_input")
        self.gridLayout_2.addWidget(self.RawTileType_input, 1, 4, 1, 1)
        self.Width = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Width.setFont(font)
        self.Width.setObjectName("Width")
        self.gridLayout_2.addWidget(self.Width, 5, 0, 1, 1)
        self.GUID = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GUID.setFont(font)
        self.GUID.setObjectName("GUID")
        self.gridLayout_2.addWidget(self.GUID, 4, 0, 1, 1)
        self.ResTileType = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ResTileType.setFont(font)
        self.ResTileType.setObjectName("ResTileType")
        self.gridLayout_2.addWidget(self.ResTileType, 4, 3, 1, 1)
        self.EncFunc = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.EncFunc.setFont(font)
        self.EncFunc.setObjectName("EncFunc")
        self.gridLayout_2.addWidget(self.EncFunc, 7, 3, 1, 1)
        self.Height_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Height_input.setObjectName("Height_input")
        self.gridLayout_2.addWidget(self.Height_input, 7, 2, 1, 1)
        self.EncFunc_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.EncFunc_input.setObjectName("EncFunc_input")
        self.gridLayout_2.addWidget(self.EncFunc_input, 7, 4, 1, 1)
        self.ResTileType_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ResTileType_input.setText("")
        self.ResTileType_input.setObjectName("ResTileType_input")
        self.gridLayout_2.addWidget(self.ResTileType_input, 4, 4, 1, 1)
        self.ResFormat_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ResFormat_input.setObjectName("ResFormat_input")
        self.gridLayout_2.addWidget(self.ResFormat_input, 5, 4, 1, 1)
        self.InputPath = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.InputPath.setFont(font)
        self.InputPath.setObjectName("InputPath")
        self.gridLayout_2.addWidget(self.InputPath, 1, 0, 1, 1)
        self.RawFormat_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.RawFormat_input.setObjectName("RawFormat_input")
        self.gridLayout_2.addWidget(self.RawFormat_input, 3, 4, 1, 1)
        self.ResFormat = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ResFormat.setFont(font)
        self.ResFormat.setObjectName("ResFormat")
        self.gridLayout_2.addWidget(self.ResFormat, 5, 3, 1, 1)
        self.Component_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Component_input.setReadOnly(False)
        self.Component_input.setObjectName("Component_input")
        self.gridLayout_2.addWidget(self.Component_input, 3, 2, 1, 1)
        self.RawFormat = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RawFormat.setFont(font)
        self.RawFormat.setObjectName("RawFormat")
        self.gridLayout_2.addWidget(self.RawFormat, 3, 3, 1, 1)
        self.FrameNum_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.FrameNum_input.setObjectName("FrameNum_input")
        self.gridLayout_2.addWidget(self.FrameNum_input, 8, 4, 1, 1)
        self.RawTileType = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RawTileType.setFont(font)
        self.RawTileType.setObjectName("RawTileType")
        self.gridLayout_2.addWidget(self.RawTileType, 1, 3, 1, 1)
        self.GUID_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.GUID_input.setText("")
        self.GUID_input.setObjectName("GUID_input")
        self.gridLayout_2.addWidget(self.GUID_input, 4, 2, 1, 1)
        self.FrameNum = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FrameNum.setFont(font)
        self.FrameNum.setObjectName("FrameNum")
        self.gridLayout_2.addWidget(self.FrameNum, 8, 3, 1, 1)
        self.Component = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Component.setFont(font)
        self.Component.setObjectName("Component")
        self.gridLayout_2.addWidget(self.Component, 3, 0, 1, 1)
        self.InputPathText = QtWidgets.QLineEdit(self.layoutWidget1)
        self.InputPathText.setReadOnly(False)
        self.InputPathText.setObjectName("InputPathText")
        self.gridLayout_2.addWidget(self.InputPathText, 1, 2, 1, 1)
        self.Width_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Width_input.setObjectName("Width_input")
        self.gridLayout_2.addWidget(self.Width_input, 5, 2, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.Input)
        self.buttonBox.setGeometry(QtCore.QRect(150, 460, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tabWidget.addTab(self.Input, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.logBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logBrowser.sizePolicy().hasHeightForWidth())
        self.logBrowser.setSizePolicy(sizePolicy)
        self.logBrowser.setObjectName("logBrowser")
        self.horizontalLayout_2.addWidget(self.logBrowser)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "Command Validator", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("mainWindow", "Platform", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("mainWindow", "Ringinfo path", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("mainWindow", "Component", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("mainWindow", "Test Name", None, -1))
        self.comboBoxPlatform.setItemText(0, QtWidgets.QApplication.translate("mainWindow", "IGFX_TIGER_LAKE_HP", None, -1))
        self.comboBoxPlatform.setItemText(1, QtWidgets.QApplication.translate("mainWindow", "IGFX_UNKNOWN", None, -1))
        self.comboBoxPlatform.setItemText(2, QtWidgets.QApplication.translate("mainWindow", "IGFX_GRANTSDALE_G", None, -1))
        self.comboBoxPlatform.setItemText(3, QtWidgets.QApplication.translate("mainWindow", "IGFX_ALVISO_G", None, -1))
        self.comboBoxPlatform.setItemText(4, QtWidgets.QApplication.translate("mainWindow", "IGFX_LAKEPORT_G", None, -1))
        self.comboBoxPlatform.setItemText(5, QtWidgets.QApplication.translate("mainWindow", "IGFX_CALISTOGA_G", None, -1))
        self.comboBoxPlatform.setItemText(6, QtWidgets.QApplication.translate("mainWindow", "IGFX_BROADWATER_G", None, -1))
        self.comboBoxPlatform.setItemText(7, QtWidgets.QApplication.translate("mainWindow", "IGFX_CRESTLINE_G", None, -1))
        self.comboBoxPlatform.setItemText(8, QtWidgets.QApplication.translate("mainWindow", "IGFX_BEARLAKE_G", None, -1))
        self.comboBoxPlatform.setItemText(9, QtWidgets.QApplication.translate("mainWindow", "IGFX_CANTIGA_G", None, -1))
        self.comboBoxPlatform.setItemText(10, QtWidgets.QApplication.translate("mainWindow", "IGFX_CEDARVIEW_G", None, -1))
        self.comboBoxPlatform.setItemText(11, QtWidgets.QApplication.translate("mainWindow", "IGFX_EAGLELAKE_G", None, -1))
        self.comboBoxPlatform.setItemText(12, QtWidgets.QApplication.translate("mainWindow", "IGFX_IRONLAKE_G", None, -1))
        self.comboBoxPlatform.setItemText(13, QtWidgets.QApplication.translate("mainWindow", "IGFX_GT", None, -1))
        self.comboBoxPlatform.setItemText(14, QtWidgets.QApplication.translate("mainWindow", "IGFX_IVYBRIDGE", None, -1))
        self.comboBoxPlatform.setItemText(15, QtWidgets.QApplication.translate("mainWindow", "IGFX_HASWELL", None, -1))
        self.comboBoxPlatform.setItemText(16, QtWidgets.QApplication.translate("mainWindow", "IGFX_VALLEYVIEW", None, -1))
        self.comboBoxPlatform.setItemText(17, QtWidgets.QApplication.translate("mainWindow", "IGFX_BROADWELL", None, -1))
        self.comboBoxPlatform.setItemText(18, QtWidgets.QApplication.translate("mainWindow", "IGFX_CHERRYVIEW", None, -1))
        self.comboBoxPlatform.setItemText(19, QtWidgets.QApplication.translate("mainWindow", "IGFX_SKYLAKE", None, -1))
        self.comboBoxPlatform.setItemText(20, QtWidgets.QApplication.translate("mainWindow", "IGFX_KABYLAKE", None, -1))
        self.comboBoxPlatform.setItemText(21, QtWidgets.QApplication.translate("mainWindow", "IGFX_COFFEELAKE", None, -1))
        self.comboBoxPlatform.setItemText(22, QtWidgets.QApplication.translate("mainWindow", "IGFX_WILLOWVIEW", None, -1))
        self.comboBoxPlatform.setItemText(23, QtWidgets.QApplication.translate("mainWindow", "IGFX_BROXTON", None, -1))
        self.comboBoxPlatform.setItemText(24, QtWidgets.QApplication.translate("mainWindow", "IGFX_GEMINILAKE", None, -1))
        self.comboBoxPlatform.setItemText(25, QtWidgets.QApplication.translate("mainWindow", "IGFX_GLENVIEW", None, -1))
        self.comboBoxPlatform.setItemText(26, QtWidgets.QApplication.translate("mainWindow", "IGFX_GOLDWATERLAKE", None, -1))
        self.comboBoxPlatform.setItemText(27, QtWidgets.QApplication.translate("mainWindow", "IGFX_CANNONLAKE", None, -1))
        self.comboBoxPlatform.setItemText(28, QtWidgets.QApplication.translate("mainWindow", "IGFX_CNX_G", None, -1))
        self.comboBoxPlatform.setItemText(29, QtWidgets.QApplication.translate("mainWindow", "IGFX_ICELAKE", None, -1))
        self.comboBoxPlatform.setItemText(30, QtWidgets.QApplication.translate("mainWindow", "IGFX_ICELAKE_LP", None, -1))
        self.comboBoxPlatform.setItemText(31, QtWidgets.QApplication.translate("mainWindow", "IGFX_LAKEFIELD", None, -1))
        self.comboBoxPlatform.setItemText(32, QtWidgets.QApplication.translate("mainWindow", "IGFX_JASPERLAKE", None, -1))
        self.comboBoxPlatform.setItemText(33, QtWidgets.QApplication.translate("mainWindow", "IGFX_TIGERLAKE_LP", None, -1))
        self.comboBoxPlatform.setItemText(34, QtWidgets.QApplication.translate("mainWindow", "IGFX_RYEFIELD", None, -1))
        self.comboBoxPlatform.setItemText(35, QtWidgets.QApplication.translate("mainWindow", "IGFX_ROCKETLAKE", None, -1))
        self.comboBoxPlatform.setItemText(36, QtWidgets.QApplication.translate("mainWindow", "IGFX_DG1", None, -1))
        self.comboBoxPlatform.setItemText(37, QtWidgets.QApplication.translate("mainWindow", "IGFX_MAX_PRODUCT", None, -1))
        self.comboBoxComponent.setItemText(0, QtWidgets.QApplication.translate("mainWindow", "Decode", None, -1))
        self.comboBoxComponent.setItemText(1, QtWidgets.QApplication.translate("mainWindow", "Encode", None, -1))
        self.comboBoxComponent.setItemText(2, QtWidgets.QApplication.translate("mainWindow", "VP", None, -1))
        self.comboBoxComponent.setItemText(3, QtWidgets.QApplication.translate("mainWindow", "CP", None, -1))
        self.comboBoxComponent.setItemText(4, QtWidgets.QApplication.translate("mainWindow", "CM", None, -1))
        self.comboBoxComponent.setItemText(5, QtWidgets.QApplication.translate("mainWindow", "Kernel", None, -1))
        self.comboBoxComponent.setItemText(6, QtWidgets.QApplication.translate("mainWindow", "Upstream", None, -1))
        self.comboBoxComponent.setItemText(7, QtWidgets.QApplication.translate("mainWindow", "MSDK", None, -1))
        self.SelectRinginfoPath.setText(QtWidgets.QApplication.translate("mainWindow", "Select Folder", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("mainWindow", "DDI Input Path ", None, -1))
        self.SelectMediaPath.setText(QtWidgets.QApplication.translate("mainWindow", "Select Folder", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("mainWindow", "Media Path", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("mainWindow", "Frame", None, -1))
        self.SelectDDIInputPath.setText(QtWidgets.QApplication.translate("mainWindow", "Select Folder", None, -1))
        self.pushButtonGAll.setText(QtWidgets.QApplication.translate("mainWindow", "Generate All", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Main), QtWidgets.QApplication.translate("mainWindow", "Main", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("mainWindow", "Please type input parameters here.", None, -1))
        self.Height.setText(QtWidgets.QApplication.translate("mainWindow", "Height", None, -1))
        self.Width.setText(QtWidgets.QApplication.translate("mainWindow", "Width", None, -1))
        self.GUID.setText(QtWidgets.QApplication.translate("mainWindow", "GUID", None, -1))
        self.ResTileType.setText(QtWidgets.QApplication.translate("mainWindow", "ResTileType", None, -1))
        self.EncFunc.setText(QtWidgets.QApplication.translate("mainWindow", "EncFunc", None, -1))
        self.InputPath.setText(QtWidgets.QApplication.translate("mainWindow", "Input Path", None, -1))
        self.ResFormat.setText(QtWidgets.QApplication.translate("mainWindow", "ResFormat", None, -1))
        self.RawFormat.setText(QtWidgets.QApplication.translate("mainWindow", "RawFormat", None, -1))
        self.RawTileType.setText(QtWidgets.QApplication.translate("mainWindow", "RawTileType", None, -1))
        self.FrameNum.setText(QtWidgets.QApplication.translate("mainWindow", "FrameNum", None, -1))
        self.Component.setText(QtWidgets.QApplication.translate("mainWindow", "Component", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Input), QtWidgets.QApplication.translate("mainWindow", "Input", None, -1))

