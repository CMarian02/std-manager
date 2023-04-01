import main
from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3

class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,850)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        #labels
        self.icons_zone = QtWidgets.QLabel(self.centralwidget)
        self.icons_zone.setGeometry(0, 0, 80, 700)
        self.icons_zone.setObjectName('icons_zone')
        self.select_zone = QtWidgets.QLabel(self.centralwidget)
        self.select_zone.setGeometry(80 ,0, 1000, 60)
        self.select_zone.setObjectName('select_zone')
        self.vers_text = QtWidgets.QLabel('version 0.1', self.centralwidget)
        self.vers_text.setGeometry(935, 680, 70, 20)
        self.vers_text.setObjectName('version_text')
        self.table_border = QtWidgets.QLabel(self.centralwidget)
        self.table_border.setGeometry(100, 100, 880, 560)
        self.table_border.setObjectName('table_border')