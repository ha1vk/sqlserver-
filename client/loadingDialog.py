# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QDialog, QMessageBox


class LoadingDialog(QDialog):
    def __init__(self, parent=None):
        super(LoadingDialog, self).__init__(parent)
        self.setupUi()

    def setupUi(self):

        self.setObjectName("Dialog")
        self.resize(181, 141)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setModal(Qt.ApplicationModal)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 181, 141))
        self.gif = QMovie('loading2.gif')
        self.gif.setScaledSize(QSize(self.label.width(),self.label.height()))
        self.label.setMovie(self.gif)
        self.gif.start()
        self.label.setObjectName("label")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "加载中.."))

