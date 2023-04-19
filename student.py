from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3
from fast_func import *
class GradesPage(QtWidgets.QMainWindow):
    def __init__(self, get_cnp, get_group, get_year):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,850)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.current_year = get_year
        #labels
        self.vers_text = QtWidgets.QLabel('v0.2.0', self.centralwidget)
        self.vers_text.setGeometry(965, 680, 70, 20)
        self.vers_text.setObjectName('version_text')
        self.fac_logo = QtWidgets.QLabel(self.centralwidget)
        self.fac_logo.setGeometry(0, 0, 80, 60)
        self.semester = QtWidgets.QLabel(self.centralwidget)
        self.semester.setGeometry(500, 670, 60, 24)
        self.semester.setObjectName('semester_text')
        self.put_logo(get_group) #put logo of your faculty
        #buttons
        self.make_buttons(get_cnp, get_group, get_year)
          #semester buttons
        self.left_switch = QtWidgets.QPushButton('<<', self.centralwidget)
        self.left_switch.setGeometry(250, 670, 30, 24)
        self.left_switch.setObjectName('switch_sem')
        self.left_switch.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.left_switch.clicked.connect(lambda: self.fill_table(self.current_year, get_cnp, get_group, '1'))
        self.right_switch = QtWidgets.QPushButton('>>', self.centralwidget)
        self.right_switch.setGeometry(750, 670, 30, 24)
        self.right_switch.setObjectName('switch_sem')
        self.right_switch.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.right_switch.clicked.connect(lambda: self.fill_table(self.current_year, get_cnp, get_group, '2'))      
        #Table
        self.create_table()
        self.fill_table(self.current_year, get_cnp, get_group, '1')
    #Steps to create basic table for grades/name of discipline/ teacher name & e-mail.
    def create_table(self):
        self.main_table = QtWidgets.QTableWidget(5, 4, self.centralwidget)
        self.main_table.setObjectName('table')
        self.main_table.setGeometry(100, 100, 880, 560)
        self.main_table.verticalHeader().setVisible(False)
        self.main_table.horizontalHeader().setVisible(False)
        self.main_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.main_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.main_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.main_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.main_table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.header_name = QtWidgets.QLabel('Name',self.centralwidget)
        self.header_name.setGeometry(110, 65, 200, 30)
        self.header_name.setObjectName('table_header')
        self.header_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_grade = QtWidgets.QLabel('Teacher',self.centralwidget)
        self.header_grade.setGeometry(330, 65, 200, 30)
        self.header_grade.setObjectName('table_header')
        self.header_grade.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_teach = QtWidgets.QLabel('Email',self.centralwidget)
        self.header_teach.setGeometry(550, 65, 200, 30)
        self.header_teach.setObjectName('table_header')
        self.header_teach.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_email = QtWidgets.QLabel('Grade',self.centralwidget)    
        self.header_email.setGeometry(770, 65, 200, 30)
        self.header_email.setObjectName('table_header')
        self.header_email.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    #Function to make buttons to switch years and 'average page' to 'main page'.
    def make_buttons(self, cnp, group, year):
        self.year1 = QtWidgets.QPushButton('YEAR I', self.centralwidget)
        self.year1.setGeometry(130,0, 110, 60)
        self.year1.clicked.connect(lambda: self.fill_table('1', cnp, group, '1'))
        self.year2 = QtWidgets.QPushButton('YEAR II', self.centralwidget)
        self.year2.setGeometry(250,0, 110, 60)
        self.year2.clicked.connect(lambda: self.fill_table('2', cnp, group, '1'))
        self.year3 = QtWidgets.QPushButton('YEAR III', self.centralwidget)
        self.year3.setGeometry(370,0, 110, 60)
        self.year3.clicked.connect(lambda: self.fill_table('3', cnp, group, '1'))
        self.year4 = QtWidgets.QPushButton('YEAR IV', self.centralwidget)
        self.year4.setGeometry(490,0, 110, 60)
        self.year4.clicked.connect(lambda: self.fill_table('4', cnp, group, '1'))
        #Today you can't use Year 5,6 and All Years, focus to develop for 4 year app.
        self.year5 = QtWidgets.QPushButton('YEAR V', self.centralwidget)
        self.year5.setGeometry(610,0, 110, 60)
        self.year6 = QtWidgets.QPushButton('YEAR VI', self.centralwidget)
        self.year6.setGeometry(730,0, 110, 60)
        self.year7 = QtWidgets.QPushButton('ALL YEARS', self.centralwidget)
        self.year7.setGeometry(850,0, 110, 60)     
        #vertical buttons
        self.grades = QtWidgets.QPushButton('GRADES', self.centralwidget)
        self.grades.setGeometry(10, 230, 80, 80)
        self.grades.setObjectName('year_btn_active')
        self.grades.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.average = QtWidgets.QPushButton('AVERAGE', self.centralwidget)
        self.average.setGeometry(10, 455, 80, 80)
        self.average.clicked.connect(lambda: self.show_frame(cnp, group, year))
        btns = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6, self.year7, self.average]
        for btn in btns:
            btn.setObjectName('year_btn')
            btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    
    #Fill table with grades, discipline, teach and logo in corner.
    def fill_table(self, year, cnp, group, sem):
        faculty_map = {'1': 'CH', '2': 'MEC', '3': 'CI', '4': 'DIMA', '5': 'ETTI', '6': 'IEEIA', '7': 'AC'}
        faculty = faculty_map.get(group[0], None)
        if sem == '2':
            self.semester.setText('SEM II')
        else:
            self.semester.setText('SEM I')
        self.btn_check(year)
        self.put_teach(year, faculty, sem)       
        self.put_grade(year, faculty, cnp, sem)

    #Function to put discipline details.
    def put_teach(self, year, fac, sem):
        table_data = []
        j = 0
        i = 0
        conn = sqlite3.connect('data/discipline.db')
        cursor = conn.cursor()
        for name in cursor.execute('SELECT "Name", "Teacher", "E-mail" FROM disciplines WHERE "Year" = (?) AND "SEM" = (?) AND Fac = (?)',(str(year), sem, fac)):
            table_data.append(name)
        for row in table_data:
            for item in row:
                self.main_table.setItem(i, j, QtWidgets.QTableWidgetItem(item))
                j += 1
                if j == 3:
                    j = 0
                    i += 1
        conn.commit()
        cursor.close()
        conn.close()
        
    #Function to put grades in table.
    def put_grade(self, year, fac, cnp, sem):
        #A function to close sqlite connection.
        def c_close():
            conn.commit()
            cursor.close()
            conn.close()
        dis_names = []
        #connect to table for disciplines
        conn = sqlite3.connect('data/discipline.db')
        cursor = conn.cursor()
        for name in cursor.execute('SELECT "Name" FROM disciplines WHERE "YEAR" = (?) AND "SEM" = (?) AND Fac = (?)',(str(year), sem, fac)):
            dis_names.append(name[0].replace(' ', '_'))
        c_close()
        #connect to table for grades
        if len(dis_names) == 5:
            grades = []
            z = 0
            conn = sqlite3.connect('data/grades.db')
            cursor = conn.cursor()
            for grade in cursor.execute('SELECT "{}", "{}", "{}", "{}", "{}" FROM grades WHERE CNP = ? AND Fac =?'.format(dis_names[0], dis_names[1], dis_names[2], dis_names[3], dis_names[4]), (cnp,fac, )):
                    grades.append(grade)
            for grade in grades:
                for grd in grade:
                    self.main_table.setItem(z, 3, QtWidgets.QTableWidgetItem(grd))
                    z +=1
            c_close()
        else:
            print('Your dis_names list is incomplete!')
    #Function to put logo in left corner of window, with faculty.
    def put_logo(self, group):
        faculty_map = {'1': 'CH', '2': 'MEC', '3': 'CI', '4': 'DIMA', '5': 'ETTI', '6': 'IEEIA', '7': 'AC'}
        faculty = faculty_map.get(group[0], None)
        self.fac_logo.setObjectName(faculty)
    #Check if buttons is active.
    def btn_check(self, year):
        btns = [self.year1, self.year2, self.year3, self.year4]
        for i in range(4):
            if year == str(i+1):
                btns[i].setObjectName('year_btn_active')
                self.current_year = year
            else:
                btns[i].setObjectName('year_btn')
            btns[i].setStyleSheet('styles.css')
    #This functions show AveragePage
    def show_frame(self, get_cnp, get_group, get_year):
            self.close()
            average_frame = AveragePage(get_cnp, get_group, get_year)
            with open('styles/style.css', 'r') as f:
                stylesheet = f.read()
            average_frame.setStyleSheet(stylesheet)
            average_frame.show()

#Probably rebuild this class in future, but now i can't find a method to solve.
class AveragePage(QtWidgets.QFrame):
    def __init__(self, get_cnp, get_group, get_year):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.setObjectName('AVG')
        self.resize(1000,700)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.current_year = get_year
        #Labels
        self.vers_text = QtWidgets.QLabel('v0.2.0', self)
        self.vers_text.setGeometry(965, 680, 70, 20)
        self.vers_text.setObjectName('version_text')
        self.fac_logo = QtWidgets.QLabel(self)
        self.fac_logo.setGeometry(0, 0, 80, 60)
        self.put_logo(get_group)
        #Buttons
        self.year1 = QtWidgets.QPushButton('YEAR I', self)
        self.year1.clicked.connect(lambda: self.fill_table(get_cnp, '1', get_group))
        self.year2 = QtWidgets.QPushButton('YEAR II', self)
        self.year2.clicked.connect(lambda: self.fill_table(get_cnp, '2', get_group))
        self.year3 = QtWidgets.QPushButton('YEAR III', self)
        self.year3.clicked.connect(lambda: self.fill_table(get_cnp, '3', get_group))
        self.year4 = QtWidgets.QPushButton('YEAR IV', self)
        self.year4.clicked.connect(lambda: self.fill_table(get_cnp, '4', get_group))
        self.year5 = QtWidgets.QPushButton('YEAR V', self)
        self.year6 = QtWidgets.QPushButton('YEAR VI', self)
        self.year7 = QtWidgets.QPushButton('ALL YEARS', self)
        he = 130
        for item in [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6, self.year7]:
            item.setGeometry(he, 0, 110, 60)
            he += 120
        #vertical buttons
        self.grades = QtWidgets.QPushButton('GRADES', self)
        self.grades.setGeometry(10, 230, 80, 80)
        self.grades.clicked.connect(lambda: self.move_page(get_cnp, get_group, get_year))
        self.average = QtWidgets.QPushButton('AVERAGE', self)
        self.average.setGeometry(10, 455, 80, 80)
        self.average.setObjectName('year_btn_active')
        self.average.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_check(str(get_year))
        #Create a func to put ObjectName and setCursor
        btns = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6, self.year7, self.grades]
        for btn in btns:
            btn.setObjectName('year_btn')
            btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        #table
        self.header_sem1 = QtWidgets.QLabel('Semester I',self)
        self.header_sem1.setGeometry(140, 120, 200, 30)
        self.header_sem1.setObjectName('table_header')
        self.header_sem1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_sem2 = QtWidgets.QLabel('Semester II',self)
        self.header_sem2.setGeometry(430, 120, 200, 30)
        self.header_sem2.setObjectName('table_header')
        self.header_sem2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header_year = QtWidgets.QLabel('Year',self)
        self.header_year.setGeometry(750, 120, 200, 30)
        self.header_year.setObjectName('table_header')
        self.header_year.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.avg_table = QtWidgets.QTableWidget(1, 3, self)
        self.avg_table.setObjectName('table')
        self.avg_table.setGeometry(100, 325, 880, 100)
        self.avg_table.verticalHeader().setVisible(False)
        self.avg_table.horizontalHeader().setVisible(False)
        self.avg_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.avg_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.avg_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.avg_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.avg_table.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.fill_table(get_cnp, self.current_year, get_group)
    
    #Function to switch to GradesPage.
    def move_page(self, cnp, group, year):
        self.close()
        app = GradesPage(cnp, group, year)
        app.show()
    #Same functions from class GradesPage.
    def put_logo(self, group):
        faculty_map = {'1': 'CH', '2': 'MEC', '3': 'CI', '4': 'DIMA', '5': 'ETTI', '6': 'IEEIA', '7': 'AC'}
        faculty = faculty_map.get(group[0], None)
        self.fac_logo.setObjectName(faculty)
    def btn_check(self, year):
        btns = [self.year1, self.year2, self.year3, self.year4]
        for i in range(4):
            if year == str(i+1):
                btns[i].setObjectName('year_btn_active')
                
                self.current_year = year
            else:
                btns[i].setObjectName('year_btn')
            btns[i].setStyleSheet('styles/style.css')
    #Create fuunction to put average in table row & columns.
    def fill_table(self, cnp, year, group):
        faculty_map = {'1': 'CH', '2': 'MEC', '3': 'CI', '4': 'DIMA', '5': 'ETTI', '6': 'IEEIA', '7': 'AC'}
        faculty = faculty_map.get(group[0], None)
        self.btn_check(year)
        grades_sem1 = self.check_grades(cnp, year, '1', faculty)
        grades_sem2 = self.check_grades(cnp, year, '2', faculty)
        avg_s1 = self.check_average(grades_sem1)
        self.avg_table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(avg_s1)))
        avg_s2 = self.check_average(grades_sem2)
        self.avg_table.setItem(0, 1, QtWidgets.QTableWidgetItem(str(avg_s2)))
        avg_y = avg_s1+avg_s2/2
        self.avg_table.setItem(0, 2, QtWidgets.QTableWidgetItem(str(avg_y)))
    #Return grades for disciplines where you give sem, year, fac and cnp.
    def check_grades(self, cnp, year, sem, fac):
        #A function to close sqlite connection.
        dis_names = []
        conn = sqlite3.connect('data/discipline.db')
        cursor = conn.cursor()
        for name in cursor.execute('SELECT "Name" FROM disciplines WHERE "YEAR" = (?) AND "SEM" = (?) AND Fac = (?)',(str(year), sem, fac)):
            dis_names.append(name[0].replace(' ', '_'))
        close_db(conn, cursor)
        if len(dis_names) == 5:
            grades = []
            conn = sqlite3.connect('data/grades.db')
            cursor = conn.cursor()
            for grade in cursor.execute('SELECT "{}", "{}", "{}", "{}", "{}" FROM grades WHERE CNP = ? AND Fac =?'.format(dis_names[0], dis_names[1], dis_names[2], dis_names[3], dis_names[4]), (cnp,fac, )):
                    grades.append(grade)
            close_db(conn, cursor)
            return grades
        else:
            print('Your dis_names list is incomplete!')
    #Return Average for grades you give.
    def check_average(self,grades_sem):
        average = 0
        for grade in grades_sem[0]:
            average += int(grade)
        average = average/5
        return average
