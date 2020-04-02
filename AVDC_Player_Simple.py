# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AVDC_Player_Simple.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1459, 795)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 201, 761))
        self.widget.setObjectName("widget")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 201, 761))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.treeWidget_media_list = QtWidgets.QTreeWidget(self.gridLayoutWidget_3)
        self.treeWidget_media_list.setObjectName("treeWidget_media_list")
        self.verticalLayout_11.addWidget(self.treeWidget_media_list)
        self.gridLayout_3.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 0, 1281, 761))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.scrollArea = QtWidgets.QScrollArea(self.page_main)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1231, 761))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1229, 759))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page_main)
        self.line_separate = QtWidgets.QFrame(self.centralwidget)
        self.line_separate.setGeometry(QtCore.QRect(200, 0, 20, 761))
        self.line_separate.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.line_separate.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_separate.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_separate.setObjectName("line_separate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AVDC_Player"))
        self.treeWidget_media_list.headerItem().setText(0, _translate("MainWindow", "媒体库"))
        self.action.setText(_translate("MainWindow", "隐藏"))
        self.action_3.setText(_translate("MainWindow", "隐藏"))
        self.action_4.setText(_translate("MainWindow", "显示"))
