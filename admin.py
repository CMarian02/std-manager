from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3, sys
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,850)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.add = AddNew()
        self.delete = Delete()
        self.stack_container = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack_container)
        self.stack_container.addWidget(self.add)
        self.stack_container.addWidget(self.delete)
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
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.delBtn = QtWidgets.QPushButton('Deleting', self)
        self.delBtn.setGeometry(10, 350, 100, 50)
        self.delBtn.setObjectName('grades_btn')
        self.delBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

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
        self.cnp_inp = QtWidgets.QLineEdit(self)
        self.fname_inp = QtWidgets.QLineEdit(self)
        self.lname_inp = QtWidgets.QLineEdit(self)
        self.group_inp = QtWidgets.QLineEdit(self)
        self.group_inp.setMaxLength(4)
        he = 260
        inputs = [self.cnp_inp, self.fname_inp, self.lname_inp, self.group_inp]
        labels = [account, cnp, fname, lname, group]
        for item in inputs:
            item.setObjectName('frame_input')
            item.setGeometry(450, he, 200, 40)
            he += 60
        for item in labels:
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
        conn.commit()
        cursor.close()
        conn.close()

class Delete(QtWidgets.QFrame):
    
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
