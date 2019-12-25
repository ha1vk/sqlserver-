# -*- coding: utf-8 -*-

#理赔历史
from PyQt5 import QtCore

import constants
from MyWebView import MyWebView

class LiPeiHistory(MyWebView):

    def __init__(self, parent=None,cookieJar = None):
        super(LiPeiHistory, self).__init__(parent,constants.lipei_his_url,cookieJar,QtCore.QRect(0, 40, 1120, 545))