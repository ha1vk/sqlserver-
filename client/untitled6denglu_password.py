# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled6denglu_password.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import json
import urllib2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox

import constants
import encdec


class denglu_password(QWidget):

    def __init__(self,opener,MainWindow,callback,parent=None):
        super(denglu_password, self).__init__(parent)
        self.opener = opener
        self.callback0 = callback
        self.MainWindow = MainWindow
        self.setupUi()

    def setupUi(self):
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 30, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 90, 261, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(170, 150, 261, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 230, 180, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 30, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 101, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "保存密码"))
        self.pushButton_2.clicked.connect(self.onTreeWidget3Clicked)
        self.label.setText(_translate("Form", "原登陆密码："))
        self.label_2.setText(_translate("Form", "新登陆密码："))
        self.label_3.setText(_translate("Form", "确认登陆密码："))

    def updatePassword0(self,userInfo,opener,MainWindow):
        data = json.dumps(userInfo, sort_keys=True).encode()
        en_data = encdec.des_encrypt(data)
        # 需要POST的数据，
        postdata = '{"userData":"' + en_data + '"}'
        print postdata
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url=constants.updatepass0_url, headers=headers, data=postdata)
        # 访问该链接#
        result = opener.open(req)
        ans = result.read()
        status = result.getcode()
        if status == 200 and ans == '更新成功':
            QMessageBox.information(self.pushButton_2, '亲', '更新成功!需要重新登录!', QMessageBox.Yes)
            constants.loginout(opener)
            self.callback0(MainWindow)
        else:
            QMessageBox.warning(self.pushButton_2, '亲',ans, QMessageBox.Yes)


    #处理按钮确定事件
    def hand(self,opener):
        if self.pushButton_2.clicked:
            password0 = self.lineEdit_2.text().strip()
            password1 = self.lineEdit_4.text().strip()
            password2 = self.lineEdit_6.text().strip()
            if password0 == '' or password1 == '' or password2 == '':
                QMessageBox.warning(self.pushButton_2, '错误', '密码不能为空', QMessageBox.Yes)
                return
            if password2 != password1:
                QMessageBox.warning(self.pushButton_2, '错误', '两次输入的密码不一样', QMessageBox.Yes)
                return
            if (not constants.judge_pure_english(password0)) or (not constants.judge_pure_english(password1)):
                QMessageBox.warning(self.pushButton_2, '错误', '密码只能是英文字符', QMessageBox.Yes)
                return

            userInfo = {
                "password":password0,
                "new_password":password1
            }
            self.updatePassword0(userInfo,opener,self.MainWindow)


    def onTreeWidget3Clicked(self):
        self.hand(self.opener)
