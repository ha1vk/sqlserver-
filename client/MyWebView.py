# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QUrl, QByteArray
from PyQt5.QtNetwork import QNetworkCookie, QNetworkCookieJar
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QWidget, QDialog, QProgressDialog, QMessageBox
from requests.utils import dict_from_cookiejar

import constants


class MyWebView(QWidget):

    def __init__(self, parent=None,url='www.baidu.com',cookieJar = None,rect=QtCore.QRect(-60, 30, 960, 500)):
        super(MyWebView, self).__init__(parent)
        self.url = url
        self.setupUi(cookieJar,rect)

    def updateCookie(self):
        self.cookie_jar = QNetworkCookieJar()
        cookie_dict = dict_from_cookiejar(self.cookieJar)
        cookies = []
        for key, values in cookie_dict.items():
            my_cookie = QNetworkCookie(QByteArray(key), QByteArray(values))
            #my_cookie.setDomain('.oicp.io')
            my_cookie.setDomain(constants.domain)
            cookies.append(my_cookie)
        self.cookie_jar.setAllCookies(cookies)
        self.web.page().networkAccessManager().setCookieJar(self.cookie_jar)


    def show(self):
        super(MyWebView,self).show()
        self.web.load(QUrl(self.url))

    def setupUi(self,cookieJar,rect):
        self.cookieJar = cookieJar
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(rect)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.web = QWebView()
        self.updateCookie()
        self.formLayout.addWidget(self.web)
        #self.web.load(QUrl(self.url))
        #self.web.showMaximized()
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

