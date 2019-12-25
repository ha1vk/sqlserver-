# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled4编辑信息.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import json
import urllib2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QByteArray
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox

import constants
import encdec
from register import ImageView


class bianji_Info(QWidget):
    def __init__(self, info,opener,MainWindow,callback,parent=None):
        super(bianji_Info,self).__init__(parent)
        self.callback = callback
        self.setupUi(info,opener,MainWindow)

    def setupUi(self,info,opener,MainWindow):
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(360, 475, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(230, 180, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setGeometry(QtCore.QRect(230, 240, 181, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_9 = QtWidgets.QDateEdit(self)
        self.lineEdit_9.setGeometry(QtCore.QRect(230, 300, 181, 31))
        self.lineEdit_9.setObjectName("qdateedit")
        self.lineEdit_11 = QtWidgets.QLineEdit(self)
        self.lineEdit_11.setGeometry(QtCore.QRect(230, 360, 181, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_13 = QtWidgets.QLineEdit(self)
        self.lineEdit_13.setGeometry(QtCore.QRect(230, 420, 421, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.imageView = ImageView(self)
        self.imageView.setGeometry(QtCore.QRect(510, 60, 200, 200))
        self.imageView.setObjectName("imageView")
        self.imageView.setAlignment(Qt.AlignCenter)
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(120, 180, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(120, 240, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(120, 300, 81, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(120, 350, 81, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(120, 420, 81, 31))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(info,opener,MainWindow,self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self,info,opener, MainWindow,Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "保存"))
        self.pushButton.clicked.connect(lambda :self.onTreeWidget2Clicked(opener,info,MainWindow))
        self.comboBox.setItemText(0, _translate("Form", "女"))
        self.comboBox.setItemText(1, _translate("Form", "男"))
        self.imageView.setText(_translate("Form", "点击上传头像"))

        self.label_4.setText(_translate("Form", "性别："))
        self.label_5.setText(_translate("Form", "年龄："))
        self.label_6.setText(_translate("Form", "出生年月："))
        self.label_7.setText(_translate("Form", "微信号："))
        self.label_8.setText(_translate("Form", "家庭住址："))
        self.comboBox.setCurrentIndex(1 if (info['sex'] == u'男') else 0)
        self.lineEdit_7.setText(info['age'])
        self.lineEdit_9.dateTimeFromText(info['birth'])
        self.lineEdit_11.setText(info['wechat'])
        self.lineEdit_13.setText(info['home_addr'])
        # 设置头像
        self.imageView.icon_head = info['user_head'].encode('utf8')
        ima_bytearray = QByteArray.fromBase64(self.imageView.icon_head)
        image = QPixmap()
        image.loadFromData(ima_bytearray)
        image = image.scaled(self.imageView.width(), self.imageView.height())
        self.imageView.setPixmap(image)

    def updateAccount(self,userInfo,opener,info,MainWindow):
        postdata = '{"action":"update","icon_data":"' + str(
            self.imageView.icon_head) + '","id_n":"' + info['ID'] + '","type":"user"}'
        print postdata
        headers = {'Content-Type': 'application/json'}
        req = urllib2.Request(url=constants.upload_url, headers=headers, data=postdata)
        # 访问该链接#
        result = opener.open(req)
        msg = result.read()
        status = result.getcode()

        if status == 200 and msg == '上传成功':
           data = json.dumps(userInfo, sort_keys=True).encode()
           en_data = encdec.des_encrypt(data)
           # 需要POST的数据，
           postdata = '{"userData":"' + en_data + '"}'
           print postdata

           req = urllib2.Request(url=constants.updateacc_url, headers=headers, data=postdata)
           # 访问该链接#
           result = opener.open(req)
           ans = result.read()
           status = result.getcode()
           if status == 200 and ans == '更新成功':
               QMessageBox.information(self.pushButton, '亲', '更新成功!需要重新登录!', QMessageBox.Yes)
               constants.loginout(opener)
               self.callback(MainWindow)
           else:
               QMessageBox.warning(self.pushButton, '亲',ans, QMessageBox.Yes)
        else:
            QMessageBox.warning(self.pushButton, '亲', msg, QMessageBox.Yes)

    #处理按钮确定事件
    def hand(self,opener,info,MainWindow):
        if self.pushButton.clicked:
            age = self.lineEdit_7.text().strip()
            if age == '':
                QMessageBox.warning(self.pushButton, '错误', '年龄不能为空', QMessageBox.Yes)
                return
            if not constants.judge_pure_digit(age):
                QMessageBox.warning(self.pushButton,'错误', '年龄格式不对', QMessageBox.Yes)
                return
            sex = self.comboBox.currentText().strip()
            birth = self.lineEdit_9.text().strip()
            wechat = self.lineEdit_11.text().strip()
            home_addr = self.lineEdit_13.text().strip()
            if home_addr == '':
                QMessageBox.warning(self.pushButton, '错误', '家庭地址不能为空', QMessageBox.Yes)
                return

            userInfo = {
                "wechat":wechat,
                "age":age,
                "sex":sex,
                "birth":birth,
                "home_addr":home_addr
            }
            self.updateAccount(userInfo,opener,info,MainWindow)

    def onTreeWidget2Clicked(self,opener,info,MainWindow):
        self.hand(opener,info,MainWindow)
        print("保存")
