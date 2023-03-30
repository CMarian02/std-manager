from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3
import screeninfo
from pages import *
import sys

#for monitor in screeninfo.get_monitors():
#    if monitor.is_primary == True:
#        width = int(monitor.width/2)
#        height = int(monitor.height/2)
#        print(f'{width} and {height}')
    

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STD-Manager")
        self.resize(800,650)
        self.setMinimumSize(QtCore.QSize(800, 650))
        self.setMaximumSize(QtCore.QSize(800, 650))
        #self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
    
        #-----------SING IN-----------

        # labels
        self.log_title = QtWidgets.QLabel('SING IN', self.centralwidget)
        self.log_title.setGeometry(305, 70, 190, 90)
        self.log_title.setObjectName('log_title')
        self.inp_text_name = QtWidgets.QLabel('YOUR CNP', self.centralwidget)
        self.inp_text_name.setGeometry(150, 255, 130, 50)
        self.inp_text_name.setObjectName('input_text')
        self.inp_text_pass = QtWidgets.QLabel('PASSWORD', self.centralwidget)
        self.inp_text_pass.setGeometry(150, 315, 130, 50)
        self.inp_text_pass.setObjectName('input_text')
        self.vers_text = QtWidgets.QLabel('version 0.1', self.centralwidget)
        self.vers_text.setGeometry(735, 630, 70, 20)
        self.vers_text.setObjectName('version_text')
        self.info_title = QtWidgets.QLabel('INFO', self.centralwidget)
        self.info_title.setGeometry(680, 150, 150, 70)
        self.info_title.setObjectName('info_title')
        self.info_text = QtWidgets.QLabel(self.centralwidget)
        self.info_text.setGeometry(600, 200, 190, 300)
        self.info_text.setObjectName('info_text')
        # intputs
        self.inp_cnp = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_cnp.setGeometry(280, 260, 200, 40)
        self.inp_cnp.setObjectName('input_logpg')
        self.inp_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_pass.setGeometry(280, 320, 200, 40)
        self.inp_pass.setObjectName('input_logpg')
        self.inp_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        #buttons
        self.btn_log = QtWidgets.QPushButton(self.centralwidget)
        self.btn_log.setText('LOGIN')
        self.btn_log.setGeometry(280, 390, 200, 50)
        self.btn_log.setObjectName('btn_log')
        self.btn_log.clicked.connect(self.check_user)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.check_user()
    def check_user(self):
        conn = sqlite3.connect('data/users.db')
        cursor = conn.cursor()
        cnps = []
        for user in cursor.execute('SELECT "CNP" FROM all_users'):
            cnps.append(user)
        for cnp in cnps:
            if str(cnp[0])== self.inp_cnp.text():
                for pas in cursor.execute('SELECT Password FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                    vfy_pass = str(pas[0])
                if vfy_pass == self.inp_pass.text():
                    for student in cursor.execute('SELECT Student FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                        is_student = student[0]
                    if is_student == "Yes":
                        for first in cursor.execute('SELECT First_time FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                            first_time = first[0]
                        if first_time == "Yes":
                            reset_frame = ResetPassword(self.inp_cnp.text())
                            self.setCentralWidget(reset_frame)
                        else:
                            self.close()
                            self.main_app = AppWindow()
                            self.main_app.show()
                    else:
                        for first in cursor.execute('SELECT First_time FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                            first_time = first[0]
                        if first_time == "Yes":
                            reset_frame = ResetPassword(self.inp_cnp.text())
                            self.setCentralWidget(reset_frame)
                        else:
                            self.close()
                            self.main_app = AppWindow()
                            self.main_app.show()
                            
                else:
                    print('You have a problem, your password is wrong!')
                
        
        conn.commit()
        cursor.close()
        conn.close()

class ResetPassword(QtWidgets.QFrame):
    def __init__(self, cnp_input):
        super().__init__()
        self.resize(800, 650)
        self.cnp_input = cnp_input
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

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.reset_password()
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
            cursor.execute('UPDATE all_users SET First_Time = "No" WHERE "CNP" = (?)', (self.cnp_input,))
            cursor.execute('UPDATE all_users SET Password = (?) WHERE "CNP" = (?)', (self.inp_npass.text(), self.cnp_input))
            conn.commit()
            cursor.close()
            conn.close()
            print('Your data is updated! Now you go to Main Page')
        

#Running App

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MyApp()
    window.show()
    sys.exit(app.exec())