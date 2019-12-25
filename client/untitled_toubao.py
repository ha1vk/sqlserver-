# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_toubaoui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore
import constants
from MyWebView import MyWebView


class toubao(MyWebView):
    def __init__(self, parent=None,cookieJar = None):
        super(toubao, self).__init__(parent,constants.getInsForm_url,cookieJar,QtCore.QRect(0, 40, 1120, 545))
