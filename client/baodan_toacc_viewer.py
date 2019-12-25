# -*- coding: utf-8 -*-
from PyQt5 import QtCore

import constants
from MyWebView import MyWebView

class BaoDanToAccViewer(MyWebView):

    def __init__(self, parent=None,cookieJar = None):
        super(BaoDanToAccViewer, self).__init__(parent,constants.baodan_to_acc_url,cookieJar,QtCore.QRect(0, 30, 1120, 560))