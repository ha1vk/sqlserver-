# -*- coding: utf-8 -*-

#普通用户界面的理赔历史
from PyQt5 import QtCore

import constants
from MyWebView import MyWebView

class LiPeiHistory2(MyWebView):

    def __init__(self, parent=None,cookieJar = None):
        super(LiPeiHistory2, self).__init__(parent,constants.lipei_his_2_url,cookieJar,QtCore.QRect(-60, 30, 960, 500))