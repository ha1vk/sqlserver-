# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled8forget_password_.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cookielib
import json
import urllib2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QDialog

import constants
import encdec


class forget_password(QDialog):

    def __init__(self,parent=None):
        super(forget_password, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(400, 480)
        self.setStyleSheet("#Form{border-image:url(./background.jpg);}")
        self.setModal(QtCore.Qt.WindowModal)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 81, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(140, 81, 221, 31))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(140, 140, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 430, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 430, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 81, 31))
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(140, 201, 221, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 260, 221, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 81, 31))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 320, 221, 31))
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(30, 370, 81, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 370, 221, 31))
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 81, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 20, 221, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "忘记密码"))
        self.label_2.setText(_translate("Form", "密保问题1："))
        self.label_3.setText(_translate("Form", "答案1："))
        self.comboBox.addItem("你的母校")
        self.comboBox.addItem("你父亲的名字")
        self.comboBox.addItem("你爱人的名字")
        self.comboBox.addItem("你喜欢的电影")
        self.comboBox.addItem("最想去的地方")
        self.pushButton.setText(_translate("Form", "提交"))
        self.pushButton_2.setText(_translate("Form", "退出"))
        self.label_4.setText(_translate("Form", "答案2："))
        self.comboBox_2.addItem("你的母校")
        self.comboBox_2.addItem("你父亲的名字")
        self.comboBox_2.addItem("你爱人的名字")
        self.comboBox_2.addItem("你喜欢的电影")
        self.comboBox_2.addItem("最想去的地方")
        self.label_5.setText(_translate("Form", "密保问题2："))
        self.label_6.setText(_translate("Form", "密码："))
        self.label_7.setText(_translate("Form", "确认密码："))
        self.label_8.setText(_translate("Form", "用户名："))
        self.pushButton.clicked.connect(self.onTreeWidget2Clicked)
        self.pushButton_2.clicked.connect(self.onTreeWidget3Clicked)

    def updatePassword1(self,userInfo):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        data = json.dumps(userInfo, sort_keys=True).encode()
        en_data = encdec.des_encrypt(data)
        # 需要POST的数据，
        postdata = '{"userData":"' + en_data + '"}'
        print postdata
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url=constants.updatepass1_url, headers=headers, data=postdata)
        # 访问该链接#
        result = opener.open(req)
        ans = result.read()
        status = result.getcode()
        if status == 200 and ans == '更新成功':
            QMessageBox.information(self.pushButton, '亲', '修改成功!请登录!', QMessageBox.Yes)
            self.close()
        else:
            QMessageBox.warning(self.pushButton, '亲',ans, QMessageBox.Yes)


    #处理按钮确定事件
    def hand(self):
        if self.pushButton.clicked:
            username = self.lineEdit_5.text().strip()
            if username == '':
                QMessageBox.warning(self.pushButton, '错误', '用户名不能为空', QMessageBox.Yes)
                return
            if not constants.judge_pure_english(username):
                QMessageBox.warning(self.pushButton, '错误', '用户名只能是英文字符', QMessageBox.Yes)
                return
            secretK1 = self.lineEdit.text().strip()
            if secretK1 == '':
                QMessageBox.warning(self.pushButton, '亲', '您还没有填写密保问题1', QMessageBox.Yes)
                return
            secretK2 = self.lineEdit_2.text().strip()
            if secretK2 == '':
                QMessageBox.warning(self.pushButton, '亲', '您还没有填写密保问题2', QMessageBox.Yes)
                return
            if self.comboBox.currentText() == self.comboBox_2.currentText():
                QMessageBox.warning(self.pushButton, '亲', '两个密保问题不能一样', QMessageBox.Yes)
                return
            password1 = self.lineEdit_3.text().strip()
            password2 = self.lineEdit_4.text().strip()
            if password1 == '' or password2 == '':
                QMessageBox.warning(self.pushButton, '错误', '密码不能为空', QMessageBox.Yes)
                return
            if password2 != password1:
                QMessageBox.warning(self.pushButton, '错误', '两次输入的密码不一样', QMessageBox.Yes)
                return
            if not constants.judge_pure_english(password1):
                QMessageBox.warning(self.pushButton, '错误', '密码只能是英文字符', QMessageBox.Yes)
                return

            userInfo = {
                'username':username,
                'mibao_q1':self.comboBox.currentText(),
                'mibao_a1':secretK1,
                'mibao_q2': self.comboBox_2.currentText(),
                'mibao_a2': secretK2,
                "new_password":password1
            }
            self.updatePassword1(userInfo)

    def onTreeWidget2Clicked(self):
        self.hand()
        print("提交")

    def onTreeWidget3Clicked(self):
        self.close()
        print("退出")