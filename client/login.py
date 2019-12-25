# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cookielib
import hashlib
import urllib2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

import constants
from loadingDialog import LoadingDialog
from manager import Manager
from register import RegisterWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressDialog, QProgressBar, QDialog, QFormLayout, \
    QLabel

from untitled import Ui_MainWindow
from untitled8forget_password import forget_password


class LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./login.jpg);}")
        MainWindow.resize(435, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 20, 281, 41))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 90, 281, 41))
        self.lineEdit.setObjectName("textEdit_2")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 180, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 180, 161, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(110, 138, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 150, 91, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "保险管理系统-登录"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "注册"))
        self.checkBox.setText(_translate("MainWindow", "管理员登录"))
        self.pushButton_3.setText(_translate("MainWindow", "忘记密码"))
        self.pushButton.clicked.connect( lambda:self.loginAcc(MainWindow))
        self.pushButton_2.clicked.connect(self.regAcc)
        self.pushButton_3.clicked.connect(lambda:self.forgetPass(MainWindow))

    def forgetPass(self,MainWindow):
        self.ui_f = forget_password()
        self.ui_f.show()

    def showRegisterWindow(self):
        self.regWindow = QMainWindow()
        self.regWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.ui = RegisterWindow()
        self.ui.setupUi(self.regWindow)
        self.regWindow.setFixedSize(self.regWindow.width(), self.regWindow.height())
        self.regWindow.show()

    def loginAcc(self,MainWindow):
        username = self.textEdit.toPlainText().strip()
        if username == '':
            QMessageBox.warning(self.pushButton, '错误', '用户名不能为空', QMessageBox.Yes)
            return
        if not constants.judge_pure_english(username):
            QMessageBox.warning(self.pushButton, '错误', '用户名只能是英文字符', QMessageBox.Yes)
            return
        password = self.lineEdit.text().strip()
        if password == '':
            QMessageBox.warning(self.pushButton, '错误', '密码不能为空', QMessageBox.Yes)
            return
        if not constants.judge_pure_english(password):
            QMessageBox.warning(self.pushButton, '错误', '密码只能是英文字符', QMessageBox.Yes)
            return

        dialog = LoadingDialog()
        dialog.show()

        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = '{"type":"' + ('mgr' if (self.checkBox.isChecked()) else 'user') + '","username":"' + username + '","password":"' + hashlib.md5(password).hexdigest() + '"}'
        print postdata
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url=constants.login_url, headers=headers, data=postdata)
        # 访问该链接#
        result = opener.open(req)
        msg = result.read()
        status = result.getcode()
        dialog.close()
        if "success" in msg:
            QMessageBox.information(self.pushButton, '亲','登陆成功!', QMessageBox.Yes)
            if self.checkBox.isChecked():
                self.ui = Manager()
            else:
                self.ui = Ui_MainWindow()
            print cookie
            self.ui.setupUi(MainWindow,cookie,opener,self.callback)
            MainWindow.show()
        else:
            QMessageBox.warning(self.pushButton, '亲', msg, QMessageBox.Yes)

    def callback(self,MainWindow):
        self.ui = LoginWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.setFixedSize(435, 289)
        MainWindow.show()

    def regAcc(self):
        if self.pushButton_2.clicked:  # 返回按钮的状态
            self.showRegisterWindow()
        else:
            print("button released")