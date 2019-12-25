# -*- coding: utf-8 -*-

#理赔
from PyQt5 import QtCore

import constants
from MyWebView import MyWebView

class LiPei(MyWebView):

    def __init__(self, parent=None,cookieJar = None):
        super(LiPei, self).__init__(parent,constants.lipei_url,cookieJar,QtCore.QRect(0, 40, 1120, 545))