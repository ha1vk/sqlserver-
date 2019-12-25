from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import *


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        tmp = QWebView()
        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(tmp)
        mainLayout = QGridLayout()
        mainLayout.addLayout(buttonLayout1, 1, 1)
        self.setLayout(mainLayout)
        self.setWindowTitle("Hello Qt")
        tmp.load(QUrl('http://www.baidu.com'))
        tmp.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())
