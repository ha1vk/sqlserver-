# -*- coding: utf-8 -*-
from PyQt5 import QtCore

import constants
from MyWebView import MyWebView

#黑名单查看
class BlackViewer(MyWebView):

    def __init__(self, parent=None,cookieJar = None):
        super(BlackViewer, self).__init__(parent,constants.black_url,cookieJar,QtCore.QRect(0, 30, 1120, 560))