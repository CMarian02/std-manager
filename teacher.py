from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3, sys
from fast_func import *
from datetime import datetime
class Main(QtWidgets.QMainWindow):

    def __init__(self, teach_dis, cnp):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,700)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.add_page = AddPage(teach_dis, cnp)
        self.stack_container = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack_container)
        self.stack_container.addWidget(self.add_page)
        self.stack_container.setCurrentWidget(self.add_page)
        #labels
        self.vers_text = QtWidgets.QLabel('v0.2.0', self)
        self.vers_text.setGeometry(965, 680, 70, 20)
        self.vers_text.setObjectName('version_text')
        self.left_logo = QtWidgets.QLabel(self)
        self.left_logo.setGeometry(20, 20, 80, 60)
        self.left_logo.setObjectName('teachpg_left')
        #buttons
        self.add_btn = QtWidgets.QPushButton('ADD GRADE', self)
        self.add_btn.setGeometry(10, 200, 100, 50)
        self.add_btn.setObjectName('grades_btn_active')
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    #This is function to switch frames.
   
class AddPage(QtWidgets.QWidget):
    def __init__(self, teach_dis, cnp):
        super().__init__()
        #labels
        title = QtWidgets.QLabel('ADDING GRADES', self)
        title.setGeometry(400, 120, 300, 45)
        title.setObjectName('frame_title')
        f_name = QtWidgets.QLabel('FIRST NAME:', self)
        f_name.setGeometry(250, 220, 100, 20)
        l_name = QtWidgets.QLabel('LAST NAME:', self)
        l_name.setGeometry(254, 280, 100, 20)
        group = QtWidgets.QLabel('GROUP:', self)
        group.setGeometry(286, 340, 100, 20)
        discipline = QtWidgets.QLabel('DISCIPLINE:', self)
        discipline.setGeometry(253, 400, 100, 20)
        grade = QtWidgets.QLabel('GRADE:', self)
        grade.setGeometry(286, 460, 100, 20)
        #inputs
        self.fname_inp = QtWidgets.QLineEdit(self)
        self.lname_inp = QtWidgets.QLineEdit(self)
        self.group_inp = QtWidgets.QLineEdit(self)
        self.group_inp.setMaxLength(4)
        self.disci_inp = QtWidgets.QLineEdit(self)
        self.grade_inp = QtWidgets.QLineEdit(self)
        self.grade_inp.setMaxLength(2)
        #buttons
        self.send_add = QtWidgets.QPushButton('ADD', self)
        self.send_add.setGeometry(450, 520, 150, 40)
        self.send_add.setObjectName('grades_btn')
        self.send_add.clicked.connect(lambda: self.valid_entry(teach_dis, cnp))
        #Create a function to put object name and geometry!
        he = 220
        for item in [self.fname_inp, self.lname_inp, self.group_inp, self.disci_inp, self.grade_inp]:
            item.setObjectName('frame_input')
            item.setGeometry(350, he, 200, 20)
            he += 60
        for item in [f_name, l_name, group, grade, discipline]:
            item.setObjectName('frame_text')

    # A basic function to validate if your enter is in data geted after
    def valid_entry(self, teach_dis, cnp):
        user = take_data('data/users.db', self.fname_inp.text(), self.lname_inp.text(), self.group_inp.text())
        dis = take_data('data/discipline.db', '', '', self.group_inp.text(), self.disci_inp.text(), False)
        if user:
            if dis:
                if self.disci_inp.text() in teach_dis:
                    if self.grade_inp.text().isdigit() and int(self.grade_inp.text()) <= 10:
                        dis = dis.replace(' ', '_')
                        conn = sqlite3.connect('data/grades.db')
                        cursor = conn.cursor()
                        cursor.execute('UPDATE grades SET {} = ? WHERE CNP = ?'.format(dis), (self.grade_inp.text(), user))
                        log = open("logs/teach_log.txt", "a")
                        now = datetime.now()
                        dateANDtime = now.strftime("%d/%m/%Y %H:%M:%S")
                        log.write(f"[{dateANDtime}] {cnp} changed student {self.fname_inp.text()} {self.lname_inp.text()} grade in discipline {self.disci_inp.text()}.His new grade is {self.grade_inp.text()}.\n")
                        log.close()
                        close_db(conn, cursor)
                    else:
                        create_error(self, 'You enter a wrong grade!', 460, 560, 170, 30)
                else:
                    create_error(self, f'Your disciplines is not {self.disci_inp.text()}', 400, 560, 250, 30)
            else:
                create_error(self, 'Discipline not found!', 400, 560, 170, 30)
        else:
            create_error(self, 'Your user input not find!', 340, 560, 170, 30)
#Function to get data from database files
def take_data(path, fname, lname, group, discipline = '', valid = True):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    data = []
    if valid == True:
        for item in cursor.execute('SELECT CNP FROM all_users WHERE "First Name" = (?) AND "Last Name" = (?) AND "Group" = (?)', (fname, lname, group, )):
            data.append(item[0])
        if data:
            close_db(conn, cursor)
            return data[0]
        else:
            close_db(conn, cursor)
            return None
    else:
        for item in cursor.execute('SELECT Name FROM disciplines WHERE Name = ? AND Year = ?',(discipline, group[1])):
            data.append(item[0])
        if data:
            close_db(conn, cursor)
            return data[0]
        else:
            close_db(conn, cursor)
            return None
#Simple function to close connection with database.

#Run app faster.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = Main(teach_dis=['Materie ETTI An 1 1', 'Materie ETTI An 1 2'], cnp = 'randomcnp')
    window.show()
    sys.exit(app.exec())
