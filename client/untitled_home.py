# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_home.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class MainHome(QWidget):
    def __init__(self, parent=None):
        super(MainHome, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(180, 140, 521, 301))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "欢迎使用保险管理系统"))
