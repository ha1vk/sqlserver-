# -*- coding: utf-8 -*-
from PyQt5 import QtCore

import constants
from MyWebView import MyWebView

#区块链浏览
class AllBaoDanViewer(MyWebView):

    def __init__(self, parent=None,cookieJar = None):
        super(AllBaoDanViewer, self).__init__(parent,constants.view_all_baodan_url,cookieJar,QtCore.QRect(0, 30, 1120, 560))