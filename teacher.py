from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3, sys

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,700)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.add_page = AddPage()
        self.del_page = DelPage()
        self.mod_page = ModPage()
        self.stack_container = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack_container)
        self.stack_container.addWidget(self.add_page)
        self.stack_container.addWidget(self.del_page)
        self.stack_container.addWidget(self.mod_page)
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
        self.add_btn.clicked.connect(lambda: self.switch_frame(1))
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.del_btn = QtWidgets.QPushButton('DEL GRADE', self)
        self.del_btn.setGeometry(10, 350, 100, 50)
        self.del_btn.setObjectName('grades_btn')
        self.del_btn.clicked.connect(lambda: self.switch_frame(2))
        self.del_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.mod_btn = QtWidgets.QPushButton('MOD GRADE', self)
        self.mod_btn.setGeometry(10, 500, 100, 50)
        self.mod_btn.setObjectName('grades_btn')
        self.mod_btn.clicked.connect(lambda: self.switch_frame(3))

    def switch_frame(self, page):
        if page == 2:
            self.stack_container.setCurrentWidget(self.del_page)
            self.add_btn.setObjectName('grades_btn')
            self.add_btn.setStyleSheet('styles.css')
            self.del_btn.setObjectName('grades_btn_active')
            self.del_btn.setStyleSheet('styles.css')
            self.mod_btn.setObjectName('grades_btn')
            self.mod_btn.setStyleSheet('styles.css')
        elif page == 1:
            self.stack_container.setCurrentWidget(self.add_page)
            self.add_btn.setObjectName('grades_btn_active')
            self.add_btn.setStyleSheet('styles.css')
            self.del_btn.setObjectName('grades_btn')
            self.del_btn.setStyleSheet('styles.css')
            self.mod_btn.setObjectName('grades_btn')
            self.mod_btn.setStyleSheet('styles.css')
        elif page == 3:
            self.stack_container.setCurrentWidget(self.mod_page)
            self.add_btn.setObjectName('grades_btn')
            self.add_btn.setStyleSheet('styles.css')
            self.del_btn.setObjectName('grades_btn')
            self.del_btn.setStyleSheet('styles.css')
            self.mod_btn.setObjectName('grades_btn_active')
            self.mod_btn.setStyleSheet('styles.css')
        else:
            print('error, page not found!')

class AddPage(QtWidgets.QWidget):
    def __init__(self):
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
        #Create a function to put object name and geometry!
        he = 220
        input_list = [self.fname_inp, self.lname_inp, self.group_inp, self.disci_inp, self.grade_inp]
        texts = [f_name, l_name, group, grade, discipline]
        for item in input_list:
            item.setObjectName('frame_input')
            item.setGeometry(350, he, 200, 20)
            he += 60
        for item in texts:
            item.setObjectName('frame_text')

class DelPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #labels
        title = QtWidgets.QLabel('DELETE GRADES', self)
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
        self.send_add = QtWidgets.QPushButton('DEL', self)
        self.send_add.setGeometry(450, 520, 150, 40)
        self.send_add.setObjectName('grades_btn')
        #Create a function to put object name and geometry!
        he = 220
        input_list = [self.fname_inp, self.lname_inp, self.group_inp, self.disci_inp, self.grade_inp]
        texts = [f_name, l_name, group, grade, discipline]
        for item in input_list:
            item.setObjectName('frame_input')
            item.setGeometry(350, he, 200, 20)
            he += 60
        for item in texts:
            item.setObjectName('frame_text')
        
class ModPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        #labels
        title = QtWidgets.QLabel('MODIFY GRADES', self)
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
        self.send_add = QtWidgets.QPushButton('MOD', self)
        self.send_add.setGeometry(450, 520, 150, 40)
        self.send_add.setObjectName('grades_btn')
        #Create a function to put object name and geometry!
        he = 220
        input_list = [self.fname_inp, self.lname_inp, self.group_inp, self.disci_inp, self.grade_inp]
        texts = [f_name, l_name, group, grade, discipline]
        for item in input_list:
            item.setObjectName('frame_input')
            item.setGeometry(350, he, 200, 20)
            he += 60
        for item in texts:
            item.setObjectName('frame_text')
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = Main()
    window.show()
    sys.exit(app.exec())
