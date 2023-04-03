import main
from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3

class AppWindow(QtWidgets.QMainWindow):
    def __init__(self, cnp, group):
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
       # self.table_border = QtWidgets.QLabel(self.centralwidget)
        #self.table_border.setGeometry(100, 100, 880, 560)
        #self.table_border.setObjectName('table_border')
        self.fac_logo = QtWidgets.QLabel(self.centralwidget)
        self.fac_logo.setGeometry(0, 0, 80, 60)
        self.put_logo(group)

        #buttons
        self.year1 = QtWidgets.QPushButton(self.centralwidget)
        self.year1.setText('YEAR I')
        self.year1.setGeometry(130,0, 110, 60)
        self.year1.setObjectName('year_btn')
        self.year1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year2 = QtWidgets.QPushButton(self.centralwidget)
        self.year2.setText('YEAR II')
        self.year2.setGeometry(250,0, 110, 60)
        self.year2.setObjectName('year_btn')
        self.year2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year3 = QtWidgets.QPushButton(self.centralwidget)
        self.year3.setText('YEAR III')
        self.year3.setGeometry(370,0, 110, 60)
        self.year3.setObjectName('year_btn')
        self.year3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year4 = QtWidgets.QPushButton(self.centralwidget)
        self.year4.setText('YEAR IV')
        self.year4.setGeometry(490,0, 110, 60)
        self.year4.setObjectName('year_btn')
        self.year4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year5 = QtWidgets.QPushButton(self.centralwidget)
        self.year5.setText('YEAR V')
        self.year5.setGeometry(610,0, 110, 60)
        self.year5.setObjectName('year_btn')
        self.year5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year6 = QtWidgets.QPushButton(self.centralwidget)
        self.year6.setText('YEAR VI')
        self.year6.setGeometry(730,0, 110, 60)
        self.year6.setObjectName('year_btn')
        self.year6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year7 = QtWidgets.QPushButton(self.centralwidget)
        self.year7.setText('ALL YEARS')
        self.year7.setGeometry(850,0, 110, 60)
        self.year7.setObjectName('year_btn')
        self.year7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(0, 160, 80, 80)
        self.btn1.setObjectName('year_btn')
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(0, 280, 80, 80)
        self.btn2.setObjectName('year_btn')
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(0, 400, 80, 80)
        self.btn3.setObjectName('year_btn')
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(0, 520, 80, 80)
        self.btn4.setObjectName('year_btn')
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

     #Table
        self.main_table = QtWidgets.QTableWidget(5, 4, self.centralwidget)
        self.main_table.setObjectName('table')
        self.main_table.setGeometry(100, 100, 880, 560)
        self.main_table.setHorizontalHeaderLabels(('Nume', 'Nota', 'Profesor', 'Email'))
        self.main_table.verticalHeader().setVisible(False)
        self.main_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.main_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.main_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.main_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def fill_table(self, year):
        pass


    def put_logo(self, group):
        
        if group[0] == '1':
            self.fac_logo.setObjectName('CH')
        elif group[0] == '2':
            self.fac_logo.setObjectName('MEC')
        elif group[0] == '3':
            self.fac_logo.setObjectName('CI')
        elif group[0] == '4':
            self.fac_logo.setObjectName('DIMA')
        elif group[0] == '5':
            self.fac_logo.setObjectName('ETTI')
        elif group[0] == '6':
            self.fac_logo.setObjectName('IEEIA')
        elif group[0] == '7':
            self.fac_logo.setObjectName('AC')
        else:
            self.fac_logo.setObjectName('app_logo')


        
