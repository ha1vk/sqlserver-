# -*- coding: utf-8 -*-
from PyQt5 import QtCore

import constants
from MyWebView import MyWebView

#用户管理
class UserViewer(MyWebView):

    def __init__(self, parent=None,cookieJar = None):
        super(UserViewer, self).__init__(parent,constants.user_url,cookieJar,QtCore.QRect(0, 30, 1120, 560))