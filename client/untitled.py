# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file ''
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import json
import urllib2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint, QByteArray
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

import constants
from LiPei import LiPei
from LiPeiHistory2 import LiPeiHistory2
from baodan import BaoDan
from untitled4bianji_Info import bianji_Info
from untitled5phone_bangdin import phone_bangdin
from untitled6denglu_password import denglu_password
from untitled_help import _help
from untitled_home import MainHome
from untitled_toubao import toubao
from userbaseInfo import BaseInfo



class Ui_MainWindow(object):

    def setupUi(self, MainWindow,cookieJar,opener,callback):
        self.opener = opener
        self.callback = callback
        self.info = self.getUserInfo()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 614)
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./background.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 101, 101))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 0, 890, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.horizontalLayout.addWidget(self.commandLinkButton_5)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.horizontalLayout.addWidget(self.commandLinkButton)
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.horizontalLayout.addWidget(self.commandLinkButton_2)
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.horizontalLayout.addWidget(self.commandLinkButton_3)
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.horizontalLayout.addWidget(self.commandLinkButton_4)
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
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.treeWidget_4)
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.treeWidget_3.setStyleSheet("background: transparent")
        self.treeWidget_3.setObjectName("treeWidget_3")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        self.verticalLayout.addWidget(self.treeWidget_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 160, 31))
        self.label_2.setObjectName("label_2")
        self.child1 = BaseInfo(self.info,self.centralwidget)
        self.child1.setGeometry(QtCore.QRect(210, 110, 881, 421))
        self.child1.setObjectName("child11")
        self.child1.hide()
        self.child2 = BaoDan(self.centralwidget,cookieJar)
        self.child2.setGeometry(QtCore.QRect(200, 55, 900, 545))
        self.child2.setObjectName("child2")
        self.child2.hide()
        self.child3 = bianji_Info(self.info,self.opener,MainWindow,callback,self.centralwidget)
        self.child3.setGeometry(QtCore.QRect(210, 50, 881, 522))
        self.child3.setObjectName("child3")
        self.child3.hide()
        self.child4 = phone_bangdin(self.centralwidget)
        self.child4.setGeometry(QtCore.QRect(210, 110, 881, 421))
        self.child4.setObjectName("child4")
        self.child4.hide()
        self.child5 = denglu_password(self.opener,MainWindow,callback,self.centralwidget)
        self.child5.setGeometry(QtCore.QRect(210, 110, 881, 500))
        self.child5.setObjectName("child5")
        self.child5.hide()
        self.child6 = LiPei(self.centralwidget,cookieJar)
        self.child6.setGeometry(QtCore.QRect(0, 20, 1120, 700))
        self.child6.setObjectName("child6")
        self.child6.hide()

        self.child7 = LiPeiHistory2(self.centralwidget,cookieJar)
        self.child7.setGeometry(QtCore.QRect(200, 55, 900, 545))
        self.child7.setObjectName("child7")
        self.child7.hide()

        self.home = MainHome(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(180, 50, 600, 350))
        self.help = _help(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(0, 100, 910,1500))
        self.help.hide()
        #self.home.hide()
        self.toubao = toubao(self.centralwidget,cookieJar)
        self.toubao.setGeometry(QtCore.QRect(0, 20, 1120, 700))
        self.toubao.hide()
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 80, 61, 21))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setFixedSize(1121, 614)

    def getUserInfo(self):
        req = urllib2.Request(url=constants.get_info_url)
        # 访问该链接#
        result = self.opener.open(req)
        msg = result.read()
        print msg
        msg = json.loads(msg)
        return msg

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "保险管理系统"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.commandLinkButton_5.setText(_translate("MainWindow", "回到首页"))
        self.commandLinkButton_5.clicked.connect(self.commandButton1Click)
        self.commandLinkButton.setText(_translate("MainWindow", "用户信息管理"))
        self.commandLinkButton.clicked.connect(self.commandButton2Click)
        self.commandLinkButton_2.setText(_translate("MainWindow", "投保"))
        self.commandLinkButton_2.clicked.connect(self.commandButton4Click)
        self.commandLinkButton_3.setText(_translate("MainWindow", "发起理赔"))
        self.commandLinkButton_3.clicked.connect(self.commandButton5Click)
        self.commandLinkButton_4.setText(_translate("MainWindow", "在线帮助"))
        self.commandLinkButton_4.clicked.connect(self.commandButton3Click)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "查询用户信息"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "用户基本信息"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "用户保单信息"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "已理赔保单及信息"))
        self.treeWidget.clicked.connect(lambda:self.onTreeWidgetClicked(MainWindow))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget_4.headerItem().setText(0, _translate("MainWindow", "修改用户信息"))
        self.treeWidget_4.clicked.connect(self.onTreeWidget4Clicked)
        __sortingEnabled = self.treeWidget_4.isSortingEnabled()
        self.treeWidget_4.setSortingEnabled(False)
        self.treeWidget_4.topLevelItem(0).setText(0, _translate("MainWindow", "编辑信息"))
        self.treeWidget_4.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "用户名修改"))
        self.treeWidget_4.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "姓名修改"))
        self.treeWidget_4.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "性别修改"))
        self.treeWidget_4.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "年龄修改"))
        self.treeWidget_4.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "出生年月修改"))
        self.treeWidget_4.topLevelItem(0).child(5).setText(0, _translate("MainWindow", "身份证修改"))
        self.treeWidget_4.topLevelItem(0).child(6).setText(0, _translate("MainWindow", "家庭住址修改"))
        self.treeWidget_4.setSortingEnabled(__sortingEnabled)
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "帐号安全"))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("MainWindow", "修改手机绑定"))
        self.treeWidget_3.topLevelItem(1).setText(0, _translate("MainWindow", "修改登录密码"))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        self.treeWidget_3.clicked.connect(self.onTreeWidget3Clicked)
        self.pushButton.setText(_translate("MainWindow", "注销"))
        self.pushButton.clicked.connect(lambda :self.onTreeWidget2Clicked(MainWindow))
        #设置头像
        ima_bytearray = QByteArray.fromBase64(self.info['user_head'].encode('utf8'))
        image = QPixmap()
        image.loadFromData(ima_bytearray)
        image = image.scaled(self.label.width(), self.label.height())
        self.label.setPixmap(image)

        self.label_2.setText(_translate("MainWindow", "用户名：{}".format(self.info['username'])))
        #隐藏用户信息管理
        self.verticalLayoutWidget.hide()

    def commandButton1Click(self):
        self.child1.hide()
        self.child2.hide()
        self.child3.hide()
        self.child4.hide()
        self.child5.hide()
        self.child6.hide()
        self.child7.hide()
        self.label.show()
        self.label_2.show()
        self.pushButton.show()
        self.home.show()
        self.help.hide()
        self.toubao.hide()
        self.verticalLayoutWidget.hide()

    def commandButton2Click(self):
        self.child1.hide()
        self.child2.hide()
        self.child3.hide()
        self.child4.hide()
        self.child5.hide()
        self.child6.hide()
        self.child7.hide()
        self.help.hide()
        self.home.hide()
        self.toubao.hide()
        self.label.show()
        self.label_2.show()
        self.pushButton.show()
        self.verticalLayoutWidget.show()


    def commandButton3Click(self):
        self.child1.hide()
        self.child2.hide()
        self.child3.hide()
        self.child4.hide()
        self.child5.hide()
        self.child6.hide()
        self.child7.hide()
        self.verticalLayoutWidget.hide()
        self.home.hide()
        self.toubao.hide()
        self.label_2.show()
        self.pushButton.show()
        self.label.show()
        self.help.show()

    def commandButton4Click(self):
        self.child1.hide()
        self.child2.hide()
        self.child3.hide()
        self.child4.hide()
        self.child5.hide()
        self.child6.hide()
        self.child7.hide()
        self.verticalLayoutWidget.hide()
        self.home.hide()
        self.help.hide()
        self.label_2.hide()
        self.pushButton.hide()
        self.label.hide()
        self.toubao.show()

    def commandButton5Click(self):
        self.child1.hide()
        self.child2.hide()
        self.child3.hide()
        self.child4.hide()
        self.child5.hide()
        self.child6.hide()
        self.child7.hide()
        self.verticalLayoutWidget.hide()
        self.home.hide()
        self.help.hide()
        self.label_2.hide()
        self.pushButton.hide()
        self.label.hide()
        self.toubao.hide()
        self.child6.show()

    def onTreeWidgetClicked(self,MainWindow):
       self.child1.hide()
       self.child2.hide()
       self.child3.hide()
       self.child4.hide()
       self.child5.hide()
       self.child6.hide()
       self.child7.hide()
       item = self.treeWidget.currentItem()
       text =  item.text(0).strip()
       if u'用户基本信息' in text:
           self.child1.show()
       elif u'用户保单信息' in text:
           self.child2.show()
       else:
           self.child7.show()

    def onTreeWidget4Clicked(self, qmodelindex):
        self.child1.hide()
        self.child2.hide()
        self.child4.hide()
        self.child5.hide()
        self.child6.hide()
        self.child7.hide()
        item = self.treeWidget_4.currentItem()
        text = item.text(0).strip()
        #print("key=%s ,value=%s" % (item.text(0), item.text(1)))
        if u'编辑信息' in text:
          self.child3.show()

    def onTreeWidget3Clicked(self, qmodelindex):
       self.child1.hide()
       self.child2.hide()
       self.child3.hide()
       self.child4.hide()
       self.child5.hide()
       self.child6.hide()
       self.child7.hide()
       item = self.treeWidget_3.currentItem()
       text = item.text(0).strip()
       #print("key=%s ,value=%s" % (item.text(0), item.text(1)))
       if u'修改手机绑定' in text:
           self.child4.show()
       else:
           if u'修改登录密码' in text:
              #print("key=%s ,value=%s" % (item.text(0), item.text(1)))
              self.child5.show()
           else:
              #self.child6.show()
              pass

    def onTreeWidget2Clicked(self,MainWindow):
        constants.loginout(self.opener)
        self.callback(MainWindow)
        print("注销")