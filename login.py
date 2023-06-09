from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3, sys
from student import *
from teacher import *
from fast_func import *

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
    
        #-----------LOGIN IN-----------#

        # labels
        self.left_cont = QtWidgets.QLabel(self.centralwidget)
        self.left_cont.setGeometry(150, 150, 250, 400)
        self.left_cont.setObjectName('left_cont')
        self.right_cont = QtWidgets.QLabel(self.centralwidget)
        self.right_cont.setGeometry(410, 150, 250, 400)
        self.right_cont.setObjectName('right_cont')
        self.std_img = QtWidgets.QLabel(self.centralwidget)
        self.std_img.setGeometry(150, 140, 200, 200)
        self.std_img.setObjectName('student_cap')
        self.profile_img = QtWidgets.QLabel(self.centralwidget)
        self.profile_img.setGeometry(150, 320, 220, 200)
        self.profile_img.setObjectName('profile_img')
        self.profcap_img = QtWidgets.QLabel(self.centralwidget)
        self.profcap_img.setGeometry(435, 120, 220, 180)
        self.profcap_img.setObjectName('profcap')
        self.vers_text = QtWidgets.QLabel('v0.2.0', self.centralwidget)
        self.vers_text.setGeometry(765, 630, 70, 20)
        self.vers_text.setObjectName('version_text')
        # intputs
        self.inp_cnp = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_cnp.setGeometry(435, 320, 200, 40)
        self.inp_cnp.setPlaceholderText('YOUR CNP')
        self.inp_cnp.setObjectName('input_logpg')
        self.inp_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.inp_pass.setGeometry(435, 380, 200, 40)
        self.inp_pass.setPlaceholderText('Password')
        self.inp_pass.setObjectName('input_logpg')
        self.inp_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        #buttons
        self.btn_log = QtWidgets.QPushButton('LOGIN', self.centralwidget)
        self.btn_log.setGeometry(435, 460, 200, 50)
        self.btn_log.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_log.setObjectName('btn_log')
        self.btn_log.clicked.connect(self.check_user)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.switch_logo)
        self.timer.start(2000)
        self.cst = 1

    #when you press 'return', connect to function check_user()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.check_user()

    #verify if inputs is valid in databases
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
                    self.timer.stop()
                    for student in cursor.execute('SELECT Student FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                        is_student = student[0]
                    if is_student == "Yes":
                        for grp in cursor.execute('SELECT "Group" FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                            self.group = str(grp[0])
                            self.year = str(grp[0])[1]
                        for first in cursor.execute('SELECT First_time FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                            first_time = first[0]
                        if first_time == "Yes":
                            reset_frame = ResetPassword(self.inp_cnp.text(), True, self.group, self.year)
                            self.setCentralWidget(reset_frame)
                        else:
                            self.close()
                            self.main_app = GradesPage(self.inp_cnp.text(), self.group, self.year)
                            self.main_app.show()
                    else:
                        for first in cursor.execute('SELECT First_time FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                            first_time = first[0]
                        if first_time == "Yes":
                            reset_frame = ResetPassword(self.inp_cnp.text(), False, None, None)
                            self.setCentralWidget(reset_frame)
                        else:
                            teach_dis = []
                            for dis in cursor.execute('SELECT Discipline FROM all_users WHERE "CNP" = (?)', (self.inp_cnp.text(),)):
                                teach_dis.append(dis[0])
                            if teach_dis:
                                teach_dis = teach_dis[0].split(',')
                            else:
                                print('your disciplines not found!')
                            self.close()
                            self.main_app = Main(teach_dis, self.inp_cnp.text())
                            self.main_app.show()     
                else:
                    print('You have a problem, your password is wrong!')
                
        
        close_db(conn, cursor)
    def switch_logo(self):
            self.cst += 1
            if self.cst == 1:
                self.std_img.setObjectName('student_cap')
                self.std_img.setStyleSheet('styles/style.css')
            elif self.cst == 2:
                self.std_img.setObjectName('admin')
                self.std_img.setStyleSheet('styles/style.css')
            else:
                self.std_img.setObjectName('teacher')
                self.std_img.setStyleSheet('styles/style.css')
                self.cst = 0
#If your account in database is 'first time' login on account, he push to reset password for security
#In future this page was been costumize!
class ResetPassword(QtWidgets.QFrame):
    def __init__(self, cnp_input, student, group, year):
        super().__init__()
        self.resize(800, 650)
        self.cnp_input = cnp_input
        self.student = student
        self.group = group
        self.year = year
        #labels
        self.log_title = QtWidgets.QLabel('RESET PASSWORD', self)
        self.log_title.setGeometry(250, 70, 500, 90)
        self.log_title.setObjectName('reg_title')
        self.left_cont = QtWidgets.QLabel(self)
        self.left_cont.setGeometry(150, 150, 250, 400)
        self.left_cont.setObjectName('left_cont')
        self.right_cont = QtWidgets.QLabel(self)
        self.right_cont.setGeometry(410, 150, 250, 400)
        self.right_cont.setObjectName('right_cont')
        self.acc_logo = QtWidgets.QLabel(self)
        self.acc_logo.setGeometry(150, 140, 200, 200)
        if self.student == True:
            self.acc_logo.setObjectName('student_cap')
        else:
            self.acc_logo.setObjectName('teacher')
        self.logo_reg = QtWidgets.QLabel(self)
        self.logo_reg.setGeometry(150, 350, 200, 200)
        self.logo_reg.setObjectName('reg_logo')
        #inputs
        self.inp_npass = QtWidgets.QLineEdit(self)
        self.inp_npass.setGeometry(435, 350, 200, 50)
        self.inp_npass.setObjectName('input_logpg')
        self.inp_npass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)   
        #buttons
        self.btn_change = QtWidgets.QPushButton(self)
        self.btn_change.setGeometry(435, 450, 200, 40)
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
                        create_error(self, 'No symbol in your password.', 355, 520, 170, 30)
                else:
                    create_error(self, 'No upper case in your password.', 355, 520, 170, 30)
            else:
                create_error(self, 'No number in your password.', 355, 520, 170, 30)
        else:
            create_error(self, 'Password to short(<8 chars).', 355, 520, 170, 30)

        # Insert new password in your DataBase file
        if Strong == True:
            conn = sqlite3.connect('data/users.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE all_users SET First_Time = "No" WHERE "CNP" = (?)', (self.cnp_input,))
            cursor.execute('UPDATE all_users SET Password = (?) WHERE "CNP" = (?)', (self.inp_npass.text(), self.cnp_input))
            close_db(conn, cursor)
            if self.student == True:
                self.main_app = GradesPage(self.cnp_input, self.group, self.year)
            else:
                conn = sqlite3.connect('data/users.db')
                cursor = conn.cursor()
                teach_dis = []
                for dis in cursor.execute('SELECT Discipline FROM all_users WHERE "CNP" = (?)', (self.cnp_input,)):
                    teach_dis.append(dis[0])
                    if teach_dis:
                        teach_dis = teach_dis[0].split(',')
                    else:
                        print('your disciplines not found test!')        
                self.main_app = Main(teach_dis, self.cnp_input)
            self.main_app.show()
            window.close()
                

#Running App
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MyApp()
    window.show()
    sys.exit(app.exec())