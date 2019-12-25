# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled5phone_bangdin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class phone_bangdin(QWidget):

    def __init__(self, parent=None):
        super(phone_bangdin, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 40, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(490, 100, 93, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 160, 141, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 100, 261, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 230, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 40, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 81, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "获取验证码"))
        self.pushButton.clicked.connect(self.onTreeWidget2Clicked)
        self.pushButton_2.setText(_translate("Form", "完成"))
        self.pushButton_2.clicked.connect(self.onTreeWidget3Clicked)
        self.label.setText(_translate("Form", "原手机号："))
        self.label_2.setText(_translate("Form", "新手机号："))
        self.label_3.setText(_translate("Form", "验证码："))

    def onTreeWidget2Clicked(self):
        print("获取验证码")

    def onTreeWidget3Clicked(self):
        print("完成")
