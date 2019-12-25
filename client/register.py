# -*- coding: utf-8 -*-

# 注册界面
import cookielib
import json
import urllib2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QBuffer
from PyQt5.QtWidgets import QMessageBox, QFileDialog,QLabel
import encdec
import constants

class ImageView(QLabel):
    def mousePressEvent(self, e):  ##重载一下鼠标点击事件
        self.selectPic()

    def selectPic(self):
        openfile_name,type = QFileDialog.getOpenFileName(self, '选择文件', '', '图片(*.jpg , *.jpeg , *.png)')
        jpg = QtGui.QPixmap(openfile_name)
        if jpg.isNull():
            self.icon_head = None
            self.setText("点击我上传")
            return
        jpg = jpg.scaled(self.width(), self.height())
        buffer0 = QBuffer()
        buffer0.open(QBuffer.WriteOnly)
        jpg.save(buffer0, "JPG")
        self.icon_head = buffer0.data().toBase64()
        #print encoded
        self.setPixmap(jpg)

class RegisterWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{border-image:url(./register.jpg);}")
        MainWindow.resize(1212, 774)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 100, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 100, 251, 41))
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 610, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(110, 610, 251, 41))
        self.textEdit_4.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 680, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(110, 680, 251, 41))
        self.textEdit_5.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.textEdit_5.setObjectName("textEdit_5")
        self.imageView = ImageView(self.centralwidget)
        self.imageView.setGeometry(QtCore.QRect(110, 390, 256, 192))
        self.imageView.setObjectName("imageView")
        self.imageView.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView.setText("点我上传")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 450, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.label_6.setLineWidth(3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 340, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 50, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(820, 50, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.Box)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(790, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(790, 230, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(890, 100, 251, 41))
        self.textEdit_6.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(890, 230, 251, 41))
        self.textEdit_7.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.textEdit_7.setObjectName("textEdit_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(790, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(890, 170, 251, 41))
        self.textEdit_8.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(770, 300, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(890, 300, 251, 41))
        self.textEdit_9.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.textEdit_9.setObjectName("textEdit_9")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(420, 548, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 620, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 170, 251, 41))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 230, 251, 41))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(820, 370, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(820, 430, 321, 31))
        self.comboBox.setObjectName("comboBox")
        self.textEdit_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(820, 480, 321, 41))
        self.textEdit_10.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.textEdit_10.setObjectName("textEdit_10")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(430, 230, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(500, 230, 111, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.textEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(510, 100, 251, 41))
        self.textEdit_11.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.textEdit_11.setObjectName("textEdit_11")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(430, 100, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(400, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(510, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.imageView2 = ImageView(self.centralwidget)
        self.imageView2.setGeometry(QtCore.QRect(500, 320, 150, 150))
        self.imageView2.setObjectName("imageView2")
        self.imageView2.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView2.setText("点我上传")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(400, 360, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(820, 630, 321, 41))
        self.textEdit_12.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.textEdit_12.setObjectName("textEdit_12")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(820, 580, 321, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1212, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "用户注册"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.label_3.setText(_translate("MainWindow", "确认密码："))
        self.label_4.setText(_translate("MainWindow", "姓名："))
        self.label_5.setText(_translate("MainWindow", "身份证："))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>手持正面</p><p>身份证照：</p><p><br/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "实名信息填写"))
        self.label_8.setText(_translate("MainWindow", "登录信息填写"))
        self.label_9.setText(_translate("MainWindow", "联系方式填写"))
        self.label_10.setText(_translate("MainWindow", "家庭电话："))
        self.label_11.setText(_translate("MainWindow", "手机号码："))
        self.label_12.setText(_translate("MainWindow", "家庭住址："))
        self.label_13.setText(_translate("MainWindow", "微信(可选)："))
        self.checkBox.setText(_translate("MainWindow", "本人承诺以上提供的信息属实"))
        self.pushButton.setText(_translate("MainWindow", "注册"))
        self.label_14.setText(_translate("MainWindow", "密保问题"))
        self.label_15.setText(_translate("MainWindow", "性别："))
        self.label_16.setText(_translate("MainWindow", "年龄："))
        self.label_17.setText(_translate("MainWindow", "出生年月："))
        self.label_18.setText(_translate("MainWindow", "账户头像："))
        self.comboBox.addItem("你的母校")
        self.comboBox.addItem("你父亲的名字")
        self.comboBox.addItem("你爱人的名字")
        self.comboBox.addItem("你喜欢的电影")
        self.comboBox.addItem("最想去的地方")
        self.comboBox_3.addItem("你的母校")
        self.comboBox_3.addItem("你父亲的名字")
        self.comboBox_3.addItem("你爱人的名字")
        self.comboBox_3.addItem("你喜欢的电影")
        self.comboBox_3.addItem("最想去的地方")
        self.comboBox_2.addItem("男")
        self.comboBox_2.addItem("女")

        self.imageView.icon_head = None
        self.imageView2.icon_head = None
        self.pushButton.clicked.connect(lambda:self.hand(MainWindow))

    def registerAccount(self,userInfo,MainWindow):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = '{"icon_data":"' + str(self.imageView.icon_head) + '","id_n":"' + self.textEdit_5.toPlainText().strip() + '","type":"id"}'
        print postdata
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url=constants.upload_url, headers=headers, data=postdata)
        # 访问该链接#
        result = opener.open(req)
        msg0 = result.read()
        status0 = result.getcode()

        postdata = '{"icon_data":"' + str(
            self.imageView2.icon_head) + '","id_n":"' + self.textEdit_5.toPlainText().strip() + '","type":"user"}'
        print postdata
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url=constants.upload_url, headers=headers, data=postdata)
        # 访问该链接#
        result = opener.open(req)
        msg1 = result.read()
        status1 = result.getcode()

        if status0 == 200 and msg0 == '上传成功' and status1 == 200 and msg1 == '上传成功':
           data = json.dumps(userInfo, sort_keys=True).encode()
           en_data = encdec.des_encrypt(data)
           # 需要POST的数据，
           postdata = '{"userData":"' + en_data + '"}'
           print postdata

           req = urllib2.Request(url=constants.regacc_url, headers=headers, data=postdata)
           # 访问该链接#
           result = opener.open(req)
           ans = result.read()
           status = result.getcode()
           if status == 200 and ans == '注册成功':
               QMessageBox.information(self.pushButton, '亲', '注册成功!', QMessageBox.Yes)
               MainWindow.close()
           else:
               QMessageBox.warning(self.pushButton, '亲',ans, QMessageBox.Yes)
           # 打印返回的内容#
           a = result.read()
           print a
        else:
            QMessageBox.warning(self.pushButton, '亲', msg0, QMessageBox.Yes)


    #处理按钮确定事件
    def hand(self,MainWindow):
        if self.pushButton.clicked:
            userName = self.textEdit.toPlainText().strip()
            if userName == '':
                QMessageBox.warning(self.pushButton, '错误', '用户名不能为空', QMessageBox.Yes)
                return
            if not constants.judge_pure_english(userName):
                QMessageBox.warning(self.pushButton,'错误', '用户名只能是英文字符', QMessageBox.Yes)
                return
            password0 = self.lineEdit.text().strip()
            password1 = self.lineEdit_2.text().strip()
            if password0 == '' or password1 == '':
                QMessageBox.warning(self.pushButton, '错误', '密码不能为空', QMessageBox.Yes)
                return
            if password0 != password1:
                QMessageBox.warning(self.pushButton,'错误', '两次输入的密码不一样', QMessageBox.Yes)
                return
            if not constants.judge_pure_english(password0):
                QMessageBox.warning(self.pushButton,'错误', '密码只能是英文字符', QMessageBox.Yes)
                return
            name = self.textEdit_4.toPlainText().strip()
            if name == '':
                QMessageBox.warning(self.pushButton, '错误', '姓名不能为空', QMessageBox.Yes)
                return
            id_num = self.textEdit_5.toPlainText().strip()
            if id_num == '':
                QMessageBox.warning(self.pushButton, '错误', '身份证不能为空', QMessageBox.Yes)
                return
            if not constants.judge_id(id_num):
                QMessageBox.warning(self.pushButton,'错误', '身份证格式不对，请输入18位有效身份证', QMessageBox.Yes)
                return
            home_addr = self.textEdit_6.toPlainText().strip()
            if home_addr == '':
                QMessageBox.warning(self.pushButton, '错误', '家庭地址不能为空', QMessageBox.Yes)
                return
            home_phone = self.textEdit_8.toPlainText().strip()
            if home_phone == '':
                QMessageBox.warning(self.pushButton, '错误', '家庭电话不能为空', QMessageBox.Yes)
                return
            if not constants.judge_pure_digit(home_phone):
                QMessageBox.warning(self.pushButton,'错误', '电话只能是纯数字', QMessageBox.Yes)
                return
            mobphone = self.textEdit_7.toPlainText().strip()
            if mobphone == '':
                QMessageBox.warning(self.pushButton, '错误', '手机号码不能为空', QMessageBox.Yes)
                return
            if not constants.judge_pure_digit(mobphone):
                QMessageBox.warning(self.pushButton,'错误', '手机号只能是纯数字', QMessageBox.Yes)
                return
            wechat = self.textEdit_9.toPlainText().strip()
            promise = self.checkBox.isChecked()
            if not promise:
                QMessageBox.warning(self.pushButton, '亲', '您还没有勾选承诺', QMessageBox.Yes)
                return
            if self.imageView2.icon_head is None:
                QMessageBox.warning(self.pushButton, '亲', '您还没有上传用户头像', QMessageBox.Yes)
                return
            if self.imageView.icon_head is None:
                QMessageBox.warning(self.pushButton, '亲', '您还没有上传手持身份证照片', QMessageBox.Yes)
                return
            secretK1 = self.textEdit_10.toPlainText().strip()
            if secretK1 == '':
                QMessageBox.warning(self.pushButton, '亲', '您还没有填写密保问题1', QMessageBox.Yes)
                return
            secretK2 = self.textEdit_12.toPlainText().strip()
            if secretK2 == '':
                QMessageBox.warning(self.pushButton, '亲', '您还没有填写密保问题2', QMessageBox.Yes)
                return
            age = self.textEdit_11.toPlainText().strip()
            if age == '':
                QMessageBox.warning(self.pushButton, '亲', '您还没有填写年龄', QMessageBox.Yes)
                return
            birth = self.dateEdit.text().strip()
            if self.comboBox.currentText() == self.comboBox_3.currentText():
                QMessageBox.warning(self.pushButton, '亲', '两个密保问题不能一样', QMessageBox.Yes)
                return


            userInfo = {
                "username":userName,
                "password":password0,
                "name":name,
                "ID":id_num,
                "age":age,
                "sex":self.comboBox_2.currentText().strip(),
                "birth":birth,
                "user_head":'icons/' + id_num + '_user.jpg',
                "icon_head":'icons/' + id_num + '_id.jpg',
                "home_addr":home_addr,
                "home_phone":home_phone,
                "mobphone":mobphone,
                "wechat":wechat,
                'mibao_q1':self.comboBox.currentText(),
                'mibao_a1':secretK1,
                'mibao_q2': self.comboBox_3.currentText(),
                'mibao_a2': secretK2
            }
            self.registerAccount(userInfo,MainWindow)
