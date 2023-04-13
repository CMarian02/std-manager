from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3

class TeachPg(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,850)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))

        self.student = QtWidgets.QLabel('Student Name', self)
        self.student.setGeometry(100, 300, 40, 20)
        self.std_entry = QtWidgets.QLineEdit(self)
        self.std_entry.setGeometry(100, 350, 50, 20)