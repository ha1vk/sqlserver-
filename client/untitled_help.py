# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_help.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from untitled_lipei import lipei
from untitled_xinyongdu import xinyongdu
from untitled_zhuyi_shixiang import zhuyi_shixiang


class _help(QWidget):
    def __init__(self, parent=None):
        super(_help, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 10, 161, 141))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setStyleSheet("background: transparent")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.child1 = zhuyi_shixiang(self.centralwidget)
        self.child1.setGeometry(QtCore.QRect(200, 0, 1500,800))
        self.child1.setObjectName("child1")
        self.child2 = lipei(self.centralwidget)
        self.child2.setGeometry(QtCore.QRect(200, 0, 1500, 800))
        self.child2.setObjectName("child1")
        self.child2.hide()
        self.child3 = xinyongdu(self.centralwidget)
        self.child3.setGeometry(QtCore.QRect(200, 0, 1500, 800))
        self.child3.setObjectName("child1")
        self.child3.hide()


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "常见问题帮助"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "购买保险注意事项"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "用户如何理赔"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "如何提高信用度"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.clicked.connect(self.onTreeWidgetClicked)
        self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0))

        #self.child1.hide()


    def onTreeWidgetClicked(self):
       self.child1.hide()
       self.child2.hide()
       self.child3.hide()
       item = self.treeWidget.currentItem()
       text =  item.text(0).strip()
       #print("key=%s ,value=%s" % (item.text(0), item.text(1)))
       if u'购买保险注意事项' in text:
           self.child1.show()

       else:
           if u'用户如何理赔' in text:
               # print("key=%s ,value=%s" % (item.text(0), item.text(1)))
               self.child2.show()
           else:
               self.child3.show()

