# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manager.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import constants
from LiPeiHistory import LiPeiHistory
from baodan_toacc_viewer import BaoDanToAccViewer
from black_viewer import BlackViewer
from baodan_viewer import  AllBaoDanViewer
from user_viewer import UserViewer


class Manager(object):
    def setupUi(self, MainWindow,cookieJar,opener,callback):
        self.opener = opener
        self.callback = callback
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 614)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./background.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 110, 160, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setStyleSheet("background: transparent")
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.treeWidget_4 = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget_4.setStyleSheet("background: transparent")
        self.treeWidget_4.setObjectName("treeWidget_4")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_4)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_4)
        self.verticalLayout.addWidget(self.treeWidget_4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(210, 110, 881, 421))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 20, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.child = AllBaoDanViewer(self.centralwidget,cookieJar)
        self.child.setGeometry(QtCore.QRect(180, 0, 1200, 600))
        self.child.setObjectName("child")
        self.child.hide()

        self.child2 = BaoDanToAccViewer(self.centralwidget,cookieJar)
        self.child2.setGeometry(QtCore.QRect(180, 0, 1200, 600))
        self.child2.setObjectName("child2")
        self.child2.hide()

        self.child3 = LiPeiHistory(self.centralwidget,cookieJar)
        self.child3.setGeometry(QtCore.QRect(180, 0, 1200, 600))
        self.child3.setObjectName("child3")
        self.child3.hide()

        self.child4 = UserViewer(self.centralwidget,cookieJar)
        self.child4.setGeometry(QtCore.QRect(180, 0, 1200, 600))
        self.child4.setObjectName("child4")
        self.child4.hide()

        self.child5 = BlackViewer(self.centralwidget,cookieJar)
        self.child5.setGeometry(QtCore.QRect(180, 0, 1200, 600))
        self.child5.setObjectName("child5")
        self.child5.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setFixedSize(1320, 614)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "保险管理系统-管理员"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "保单"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "所有保单"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "待受理"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "已受理"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.clicked.connect(self.onTreeWidgetClicked)
        self.treeWidget_4.headerItem().setText(0, _translate("MainWindow", "黑名单"))
        __sortingEnabled = self.treeWidget_4.isSortingEnabled()
        self.treeWidget_4.setSortingEnabled(False)
        self.treeWidget_4.topLevelItem(0).setText(0, _translate("MainWindow", "用户管理"))
        self.treeWidget_4.topLevelItem(1).setText(0, _translate("MainWindow", "黑名单管理"))
        self.treeWidget_4.clicked.connect(self.onTreeWidgetClicked2)
        self.treeWidget_4.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("MainWindow", "管理员"))
        self.pushButton.setText(_translate("MainWindow", "注销"))
        self.pushButton.clicked.connect(lambda :self.onButtonClicked(MainWindow))

    def onTreeWidgetClicked(self):
       item = self.treeWidget.currentItem()
       text =  item.text(0).strip()
       self.child.hide()
       self.child2.hide()
       self.child3.hide()
       self.child4.hide()
       self.child5.hide()
       if u'所有保单' in text:
           self.child.show()
       elif u'待受理' in text:
           self.child2.show()
       elif u'已受理' in text:
           self.child3.show()
       else:
           pass

    def onTreeWidgetClicked2(self):
       item = self.treeWidget_4.currentItem()
       text =  item.text(0).strip()
       self.child.hide()
       self.child2.hide()
       self.child3.hide()
       self.child4.hide()
       self.child5.hide()
       if u'用户管理' in text:
           self.child4.show()
       else:
           self.child5.show()

    def onButtonClicked(self,MainWindow):
        constants.loginout(self.opener)
        self.callback(MainWindow)
        print("注销")