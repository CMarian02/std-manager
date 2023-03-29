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
        self.resize(800, 650)
        self.setMinimumSize(800, 650)
        self.setMaximumSize(800, 650)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        #-----------SING IN-----------

        # labels
        self.log_title = QtWidgets.QLabel('SING IN', self.centralwidget)
        self.log_title.setGeometry(305, 70, 190, 90)
        self.log_title.setObjectName('log_title')
        self.inp_text_name = QtWidgets.QLabel('USERNAME', self.centralwidget)
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
        self.inp_name = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_name.setGeometry(280, 260, 200, 40)
        self.inp_name.setObjectName('input_logpg')
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

    def check_user(self):
        conn = sqlite3.connect('data/users.db')
        cursor = conn.cursor()
        usernames = []
        for user in cursor.execute('SELECT "Last Name" FROM all_users'):
            usernames.append(user)
        for username in usernames:
            if str(username[0]).lower() == self.inp_name.text().lower():
                for pas in cursor.execute('SELECT Password FROM all_users WHERE "Last Name" = (?)', (self.inp_name.text().capitalize(),)):
                    vfy_pass = str(pas[0])
                if vfy_pass == self.inp_pass.text():
                    for student in cursor.execute('SELECT Student FROM all_users WHERE "Last Name" = (?)', (self.inp_name.text().capitalize(),)):
                        is_student = student[0]
                    if is_student == "Yes":
                        for first in cursor.execute('SELECT First_time FROM all_users WHERE "Last Name" = (?)', (self.inp_name.text().capitalize(),)):
                            first_time = first[0]
                        if first_time == "Yes":
                            reset_frame = ResetPassword(self.inp_name.text())
                            self.setCentralWidget(reset_frame)
                        else:
                            print('go to main app')
                    else:
                        for first in cursor.execute('SELECT First_time FROM all_users WHERE "Last Name" = (?)', (self.inp_name.text().capitalize(),)):
                            first_time = first[0]
                        if first_time == "Yes":
                            reset_frame = ResetPassword(self.inp_name.text())
                            self.setCentralWidget(reset_frame)
                        else:
                            print('go to main app')
                            
                else:
                    print('You have a problem, your password is wrong!')
                
        
        conn.commit()
        cursor.close()
        conn.close()
            

#Running App

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MyApp()
    window.show()
    sys.exit(app.exec())