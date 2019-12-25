# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled7payment_password.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from untitled8forget_password import forget_password


class payment_password(QWidget):

    def __init__(self, parent=None):
        super(payment_password, self).__init__(parent)
        self.setupUi()

    def callback(self):
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.lineEdit_2.show()
        self.lineEdit_4.show()
        self.lineEdit_6.show()
        self.pushButton.show()
        self.pushButton_2.show()

    def setupUi(self):
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 30, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 90, 261, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 150, 261, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(320, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.child1 = forget_password(self)
        self.child1.setCallBack(self.callback)
        self.child1.setGeometry(QtCore.QRect(50, 30, 881, 421))
        self.child1.setObjectName("child1")
        self.child1.hide()
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 101, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "保存密码"))
        self.pushButton_2.clicked.connect(self.onTreeWidget2Clicked)
        self.pushButton.setText(_translate("Form", "忘记密码"))
        self.pushButton.clicked.connect(self.onTreeWidget3Clicked)
        self.label_2.setText(_translate("Form", "原支付密码："))
        self.label_3.setText(_translate("Form", "新支付密码："))
        self.label_4.setText(_translate("Form", "确认支付密码："))

    def onTreeWidget3Clicked(self):
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.lineEdit_2.hide()
        self.lineEdit_4.hide()
        self.lineEdit_6.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.child1.show()
        print("忘记密码")

    def onTreeWidget2Clicked(self):
        print("保存密码")

