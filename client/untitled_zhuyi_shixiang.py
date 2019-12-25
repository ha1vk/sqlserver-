# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_zhuyi_shixiang.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class zhuyi_shixiang(QWidget):

    def __init__(self, parent=None):
        super(zhuyi_shixiang, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 700, 401))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")


        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Agency FB\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">看保险条款</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">人们在买保险之前想要准确地了解保险的内容，就要看保险条款。保险条款是保险公司同消费者签署的保险合同的核心内容，它规定着一份保险所包含的权利与义务。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">看保险条款的保险责任</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">除交费等项目外，保险条款的关键内容是保险责任。一般来说，除保险责任外，保险条款的其他各项内容基本相同，各种保险的区分主要在保险责任。当然，有时也需要看除外责任，看在何种情况下保险公司可以不承担赔偿和给付的责任；有时则还需要看一看某些保险产品自己所特有的规定和注释。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">看保险产品简介</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">许多人往往看不懂保险条款，所以要看文字材料的最通俗办法是看保险产品的简介。由于保险产品简介有时可能含有包装美化产品的不准确表述，所以看懂保险简介以后，最好还是将其与保险条款对照理解。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">了解交钱和领钱</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">人们所要了解的保险核心内容是交钱和领钱。这包括三个方面：一是交多少钱，日后领取多少钱；二是交钱的时间与方式，日后领钱的时间与方式，比如多长时间，一次性还是分期等等；三是领取的条件，比如在什么情况下可以领钱，在什么情况下不可以领钱等等。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">将了解的内容落实到文字</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">并不是所有人都能够自己看明白文字材料，所以想了解保险，最直接的办法是听懂推销员介绍保险。此时的关键点只有一个：将了解到的情况逐项落实到文字记录下来，并逐项在保险条款中找到相对应的部分加以确认。</span></p></body></html>"))
