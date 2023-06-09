from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3, sys
from fast_func import *
from datetime import datetime

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,850)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.add = AddNew()
        self.delete = Delete()
        self.dis = Discipline()
        self.stack_container = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack_container)
        self.stack_container.addWidget(self.add)
        self.stack_container.addWidget(self.delete)
        self.stack_container.addWidget(self.dis)
        self.stack_container.setCurrentWidget(self.add)
        #labels
        self.vers_text = QtWidgets.QLabel('v0.2.0', self)
        self.vers_text.setGeometry(965, 680, 70, 20)
        self.vers_text.setObjectName('version_text')
        self.left_logo = QtWidgets.QLabel(self)
        self.left_logo.setGeometry(20, 20, 80, 60)
        self.left_logo.setObjectName('admin_left')
        #buttons
        self.addBtn = QtWidgets.QPushButton('Adding', self)
        self.addBtn.setGeometry(10, 200, 100, 50)
        self.addBtn.setObjectName('grades_btn_active')
        self.addBtn.clicked.connect(lambda: self.switch_frame(1))
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delBtn = QtWidgets.QPushButton('Deleting', self)
        self.delBtn.setGeometry(10, 350, 100, 50)
        self.delBtn.setObjectName('grades_btn')
        self.delBtn.clicked.connect(lambda: self.switch_frame(2))
        self.delBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.disBtn = QtWidgets.QPushButton('Discipline', self)
        self.disBtn.setGeometry(10, 500, 100, 50)
        self.disBtn.setObjectName('grades_btn')
        self.disBtn.clicked.connect(lambda: self.switch_frame(3))
        self.disBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))    

    def switch_frame(self, page):
        if page == 2:
            self.stack_container.setCurrentWidget(self.delete)
            self.delBtn.setObjectName('grades_btn_active')
            self.delBtn.setStyleSheet('styles.css')
            for item in [self.addBtn, self.disBtn]:
                item.setObjectName('grades_btn')
                item.setStyleSheet('style.css')
        elif page == 1:
            self.stack_container.setCurrentWidget(self.add)
            self.addBtn.setObjectName('grades_btn_active')
            self.addBtn.setStyleSheet('style.css')
            for item in [self.delBtn, self.disBtn]:
                item.setObjectName('grades_btn')
                item.setStyleSheet('style.css')
        elif page == 3:
            self.stack_container.setCurrentWidget(self.dis)
            self.disBtn.setObjectName('grades_btn_active')
            self.disBtn.setStyleSheet('style.css')
            for item in [self.addBtn, self.delBtn]:
                item.setObjectName('grades_btn')
                item.setStyleSheet('style.css')
                

class AddNew(QtWidgets.QFrame):
    
    def __init__(self):
        super().__init__()
        #labels
        account = QtWidgets.QLabel('Chose Account:', self)
        account.setGeometry(320, 210, 150, 20)
        cnp = QtWidgets.QLabel('CNP:', self)
        cnp.setGeometry(410, 270, 100, 20)
        fname = QtWidgets.QLabel('First Name:', self)
        fname.setGeometry(350, 330, 100, 20)
        lname = QtWidgets.QLabel('Last Name:', self)
        lname.setGeometry(355, 390, 100, 20)
        group = QtWidgets.QLabel('Group:', self)
        group.setGeometry(388, 450, 100, 20)
        #inputs
        self.box = QtWidgets.QComboBox(self)
        self.box.addItem('Student')
        self.box.addItem('Teacher')
        self.box.setGeometry(450, 200, 200, 40)
        self.box.setObjectName('drop_box')
        self.cnp_inp = QtWidgets.QLineEdit(self)
        self.fname_inp = QtWidgets.QLineEdit(self)
        self.lname_inp = QtWidgets.QLineEdit(self)
        self.group_inp = QtWidgets.QLineEdit(self)
        self.group_inp.setMaxLength(4)
        he = 260
        for item in [self.cnp_inp, self.fname_inp, self.lname_inp, self.group_inp]:
            item.setObjectName('frame_input')
            item.setGeometry(450, he, 200, 40)
            he += 60
        for item in [account, cnp, fname, lname, group]:
            item.setObjectName('frame_text')
        #buttons
        self.add_entry = QtWidgets.QPushButton('ENTER', self)
        self.add_entry.setGeometry(450, 520, 200, 60)
        self.add_entry.setObjectName('grades_btn')
        self.add_entry.clicked.connect(self.adding)
        self.add_entry.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    
    def adding(self):
        conn = sqlite3.connect('data/users.db')
        cursor = conn.cursor()
        year = str(2000 + int(self.cnp_inp.text()[1]) * 10 + int(self.cnp_inp.text()[2]))
        if self.box.currentText() == 'Student':
            account_type = 'Yes'
        else:
            account_type = 'No'
        cursor.execute('INSERT INTO all_users ("First Name", "Last Name", "Year", "CNP", "Password", "Student", "First_time", "Group") VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (self.fname_inp.text(), self.lname_inp.text(), year, self.cnp_inp.text(), self.cnp_inp.text(), account_type, 'Yes', self.group_inp.text()))
        close_db(conn, cursor)
        conn = sqlite3.connect('data/grades.db')
        cursor = conn.cursor()
        faculty_map = {'1': 'CH', '2': 'MEC', '3': 'CI', '4': 'DIMA', '5': 'ETTI', '6': 'IEEIA', '7': 'AC'}
        fac = faculty_map.get(self.group_inp.text()[0], None)
        cursor.execute('INSERT INTO grades ("CNP", "Fac") VALUES (?, ?)', (self.cnp_inp.text(), fac, ))
        close_db(conn, cursor)
        
class Delete(QtWidgets.QFrame):
    
    def __init__(self):
        super().__init__()
        #labels
        cnp = QtWidgets.QLabel('Account CNP:', self)
        cnp.setGeometry(320, 210, 150, 20)
        cnp.setObjectName('frame_text')
        res = QtWidgets.QLabel('Reason:', self)
        res.setGeometry(365, 270, 150, 20)
        res.setObjectName('frame_text')
        #inputs
        self.cnp_inp = QtWidgets.QLineEdit(self)
        self.cnp_inp.setGeometry(450, 200, 200, 40)
        self.cnp_inp.setObjectName('frame_input')
        self.res_inp = QtWidgets.QLineEdit(self)
        self.res_inp.setGeometry(450, 260, 200, 40)
        self.res_inp.setObjectName('frame_input')
        #buttons
        self.delBtn = QtWidgets.QPushButton('DELETE',self)
        self.delBtn.setGeometry(450, 320, 200, 60)
        self.delBtn.setObjectName('grades_btn')
        self.delBtn.clicked.connect(self.delete_entry)
        self.delBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
    #Funtion verify input with db, if it's fine this delete row.
    def delete_entry(self):
        if self.cnp_inp.text().isdigit() and len(self.cnp_inp.text()) == 13:
            conn = sqlite3.connect('data/users.db')
            cursor = conn.cursor()
            cnp = []
            for c in cursor.execute('SELECT CNP FROM all_users WHERE CNP = (?)', (self.cnp_inp.text(),)):
                cnp.append(c)
            if cnp:
                if len(self.res_inp.text()) > 3:
                    adm_log = open('logs/adm_log.txt', 'a')
                    now = datetime.now()
                    dateANDtime = now.strftime("%d/%m/%Y %H:%M:%S")
                    adm_log.write(f'[{dateANDtime}] Admin delete {self.cnp_inp.text()}. Reason: {self.res_inp.text()}\n')
                    adm_log.close()
                    cursor.execute('DELETE FROM all_users WHERE CNP =(?)', (self.cnp_inp.text(),))
                    close_db(conn, cursor)
                    conn = sqlite3.connect('data/grades.db')
                    cursor = conn.cursor()
                    cursor.execute('DELETE FROM grades WHERE CNP = (?)', (self.cnp_inp.text(), ))
                    close_db(conn, cursor)
                else:
                    print('Reason to short, you must enter 3 characters.')
            else:
                print('This CNP is not in the database.')
        else:
            print("You don't enter a CNP.")       

class Discipline(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        #labels
        dis = QtWidgets.QLabel('DISCIPLINE:', self)
        dis.setGeometry(320, 210, 150, 20)
        year = QtWidgets.QLabel('Year:', self)
        year.setGeometry(363, 270, 150, 20)
        sem = QtWidgets.QLabel('SEMESTER:', self)
        sem.setGeometry(325, 330, 150, 20)
        teach = QtWidgets.QLabel('Teacher:', self)
        teach.setGeometry(335, 400, 150, 20)
        teach_email = QtWidgets.QLabel('EMAIL:', self)
        teach_email.setGeometry(355, 460, 150, 20)
        faculty = QtWidgets.QLabel('FACULTY:', self)
        faculty.setGeometry(340, 520, 150, 20)
        for item in [dis, year, sem, teach, teach_email, faculty]:
            item.setObjectName('frame_text')
        #inputs
        self.dis_inp = QtWidgets.QLineEdit(self)
        self.year_inp = QtWidgets.QLineEdit(self)
        self.year_inp.setMaxLength(4)
        self.sem_inp = QtWidgets.QLineEdit(self)
        self.sem_inp.setMaxLength(1)
        self.teach_inp = QtWidgets.QLineEdit(self)
        self.email_inp = QtWidgets.QLineEdit(self)
        self.fac_inp = QtWidgets.QLineEdit(self)
        he = 200
        for item in [self.dis_inp, self.year_inp, self.sem_inp, self.teach_inp, self.email_inp, self.fac_inp]:
            item.setGeometry(450, he, 200, 40)
            item.setObjectName('frame_input')
            he += 60
        #buttons
        self.addBtn = QtWidgets.QPushButton('ADD',self)
        self.addBtn.setGeometry(400, 580, 100, 60)
        self.addBtn.setObjectName('grades_btn')
        self.addBtn.clicked.connect(self.add_dis)
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delBtn = QtWidgets.QPushButton('DELETE',self)
        self.delBtn.setGeometry(530, 580, 100, 60)
        self.delBtn.setObjectName('grades_btn')
        self.delBtn.clicked.connect(self.del_dis)
        self.delBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    #Function to add descipline in databases 
    def add_dis(self):

        conn = sqlite3.connect('data/discipline.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO disciplines ("Name", "Year", "SEM", "Teacher", "E-mail", "Fac") VALUES (?,?,?,?,?,?)', (self.dis_inp.text(), self.year_inp.text(), self.sem_inp.text(), self.teach_inp.text(), self.email_inp.text(), self.fac_inp.text(), ))
        close_db(conn, cursor)
        conn = sqlite3.connect('data/grades.db')
        cursor = conn.cursor()
        cursor.execute('ALTER TABLE grades ADD COLUMN {} TEXT'.format(self.dis_inp.text().replace(' ', '_')))
        close_db(conn, cursor)
    
    def del_dis(self):

        conn = sqlite3.connect('data/discipline.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM disciplines WHERE "Name" = (?) AND "Fac" = (?)', (self.dis_inp.text(), self.fac_inp.text(), ))
        close_db(conn, cursor)
        conn = sqlite3.connect('data/grades.db')
        cursor = conn.cursor()
        cursor.execute('ALTER TABLE grades DROP COLUMN {}'.format(self.dis_inp.text().replace(' ', '_')))
        close_db(conn, cursor)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
