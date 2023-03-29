import main
from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3

class ResetPassword(QtWidgets.QFrame):
    def __init__(self, name_input):
        super().__init__()
        self.resize(800, 650)
        self.name_input = name_input
        #labels
        self.log_title = QtWidgets.QLabel('CHANGE PASSWORD', self)
        self.log_title.setGeometry(150, 70, 500, 90)
        self.log_title.setObjectName('log_title')
        #inputs
        self.inp_npass = QtWidgets.QLineEdit(self)
        self.inp_npass.setGeometry(300, 350, 200, 50)
        self.inp_npass.setObjectName('input_logpg')
        self.inp_npass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)   
        #buttons
        self.btn_change = QtWidgets.QPushButton(self)
        self.btn_change.setGeometry(300, 450, 200, 40)
        self.btn_change.setText('CHANGE')
        self.btn_change.setObjectName('btn_log')
        self.btn_change.clicked.connect(self.reset_password)
    
    def reset_password(self):

        #Check If Password is Strong
        Number = False
        Upper = False
        Symbol = False
        Strong = False

        if len(self.inp_npass.text()) >= 8:
            for l in self.inp_npass.text():
                if l.isnumeric():
                    Number = True
                if l.isupper():
                    Upper = True
                if l in '?!@#%^&*+_-=':
                    Symbol = True
            if Number == True:
                if Upper == True:
                    if Symbol == True:
                        Strong = True
                    else:
                        print('No symbol in your password')
                else:
                    print('No upper case in your password')
            else:
                print('No Number in your password:')
        else:
            print('<8 char.')

        # Insert new password in your DataBase file

        if Strong == True:
            conn = sqlite3.connect('data/users.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE all_users SET First_Time = "No" WHERE "Last Name" = (?)', (self.name_input,))
            cursor.execute('UPDATE all_users SET Password = (?) WHERE "Last Name" = (?)', (self.inp_npass.text(), self.name_input))
            conn.commit()
            cursor.close()
            conn.close()
            print('Your data is updated! Now you go to Main Page')
        
