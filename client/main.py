#encoding:utf-8

from login import LoginWindow
from register import RegisterWindow
from PyQt5 import QtCore
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
    ui = LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
    MainWindow.show()
    sys.exit(app.exec_())