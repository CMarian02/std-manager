import main
from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3

class ResetPassword(QtWidgets.QFrame):
    def __init__(self):
        super().__init__
        self.windowTitle('STD-Manager -> Reset Password')
        print('yees')