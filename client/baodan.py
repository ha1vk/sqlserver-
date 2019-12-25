# -*- coding: utf-8 -*-

#保单
from PyQt5 import QtCore

import constants
from MyWebView import MyWebView

class BaoDan(MyWebView):

    def __init__(self, parent=None,cookieJar = None):
        super(BaoDan, self).__init__(parent,constants.loadShowInsForm,cookieJar,QtCore.QRect(-60, 30, 960, 500))
