import main
from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3

class AppWindow(QtWidgets.QMainWindow):
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
        self.vers_text = QtWidgets.QLabel('version 0.1', self.centralwidget)
        self.vers_text.setGeometry(935, 680, 70, 20)
        self.vers_text.setObjectName('version_text')
        self.fac_logo = QtWidgets.QLabel(self.centralwidget)
        self.fac_logo.setGeometry(0, 0, 80, 60)
        self.semester = QtWidgets.QLabel(self.centralwidget)
        self.semester.setGeometry(500, 670, 60, 24)
        self.semester.setObjectName('semester_text')
        self.put_logo(get_group) #put logo of your faculty
        #buttons
        self.make_buttons(get_cnp, get_group)
        #semester buttons
        self.left_switch = QtWidgets.QPushButton(self.centralwidget)
        self.left_switch.setGeometry(250, 670, 30, 24)
        self.left_switch.setText('<<')
        self.left_switch.setObjectName('switch_sem')
        self.left_switch.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.left_switch.clicked.connect(lambda: self.fill_table(self.current_year, get_cnp, get_group, '1'))
        self.right_switch = QtWidgets.QPushButton(self.centralwidget)
        self.right_switch.setGeometry(750, 670, 30, 24)
        self.right_switch.setText('>>')
        self.right_switch.setObjectName('switch_sem')
        self.right_switch.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.right_switch.clicked.connect(lambda: self.fill_table(self.current_year, get_cnp, get_group, '2'))
        
        #Table
        self.main_table = QtWidgets.QTableWidget(5, 4, self.centralwidget)
        self.main_table.setObjectName('table')
        self.main_table.setGeometry(100, 100, 880, 560)
        self.main_table.verticalHeader().setVisible(False)
        self.main_table.horizontalHeader().setVisible(False)
        self.main_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.main_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.main_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.main_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
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
        self.fill_table(self.current_year, get_cnp, get_group, '1')
    
    def make_buttons(self, cnp, group):
        self.year1 = QtWidgets.QPushButton(self.centralwidget)
        self.year1.setText('YEAR I')
        self.year1.setGeometry(130,0, 110, 60)
        self.year1.setObjectName('year_btn')
        self.year1.clicked.connect(lambda: self.fill_table('1', cnp, group, '1'))
        self.year1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year2 = QtWidgets.QPushButton(self.centralwidget)
        self.year2.setText('YEAR II')
        self.year2.setGeometry(250,0, 110, 60)
        self.year2.setObjectName('year_btn')
        self.year2.clicked.connect(lambda: self.fill_table('2', cnp, group, '1'))
        self.year2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year3 = QtWidgets.QPushButton(self.centralwidget)
        self.year3.setText('YEAR III')
        self.year3.setGeometry(370,0, 110, 60)
        self.year3.setObjectName('year_btn')
        self.year3.clicked.connect(lambda: self.fill_table('3', cnp, group, '1'))
        self.year3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year4 = QtWidgets.QPushButton(self.centralwidget)
        self.year4.setText('YEAR IV')
        self.year4.setGeometry(490,0, 110, 60)
        self.year4.setObjectName('year_btn')
        self.year4.clicked.connect(lambda: self.fill_table('4', cnp, group, '1'))
        self.year4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        #Today you can't use Year 5,6 and All Years, focus to develop for 4 year app.
        self.year5 = QtWidgets.QPushButton(self.centralwidget)
        self.year5.setText('YEAR V')
        self.year5.setGeometry(610,0, 110, 60)
        self.year5.setObjectName('year_btn')
        self.year5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year6 = QtWidgets.QPushButton(self.centralwidget)
        self.year6.setText('YEAR VI')
        self.year6.setGeometry(730,0, 110, 60)
        self.year6.setObjectName('year_btn')
        self.year6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.year7 = QtWidgets.QPushButton(self.centralwidget)
        self.year7.setText('ALL YEARS')
        self.year7.setGeometry(850,0, 110, 60)
        self.year7.setObjectName('year_btn')
        self.year7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        #vertical buttons
        self.grades = QtWidgets.QPushButton(self.centralwidget)
        self.grades.setGeometry(10, 230, 80, 80)
        self.grades.setText('GRADES')
        self.grades.setObjectName('year_btn')
        self.grades.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.average = QtWidgets.QPushButton(self.centralwidget)
        self.average.setText('AVERAGE')
        self.average.setGeometry(10, 455, 80, 80)
        self.average.setObjectName('year_btn')
        #self.average.clicked.connect(lambda: self.switch_frame(cnp, group))
        self.average.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
    
    #Fill table with grades, discipline, teach and logo in corner.
    # Here rebuild function, bsc you can't switch great year.
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

    #Function to put discipline details
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
        
    #Function to put grades in table
    def put_grade(self, year, fac, cnp, sem):
        z = 0
        dis_names = []
        grades = []
        #connect to table for disciplines
        conn = sqlite3.connect('data/discipline.db')
        cursor = conn.cursor()
        for name in cursor.execute('SELECT "Name" FROM disciplines WHERE "YEAR" = (?) AND "SEM" = (?) AND Fac = (?)',(str(year), sem, fac)):
            dis_names.append(name[0].replace(' ', '_'))
        conn.commit()
        cursor.close()
        conn.close()
        #connect to table for grades
        conn = sqlite3.connect('data/grades.db')
        cursor = conn.cursor()
        for grade in cursor.execute('SELECT "{}", "{}", "{}", "{}", "{}" FROM grades WHERE CNP = ? AND Fac =?'.format(dis_names[0], dis_names[1], dis_names[2], dis_names[3], dis_names[4]), (cnp,fac, )):
                grades.append(grade)
        for grade in grades:
            for grd in grade:
                self.main_table.setItem(z, 3, QtWidgets.QTableWidgetItem(grd))
                z +=1
        conn.commit()
        cursor.close()
        conn.close()

    #Function to put logo in left corner of window, with faculty.
    def put_logo(self, group):
        faculty_map = {'1': 'CH', '2': 'MEC', '3': 'CI', '4': 'DIMA', '5': 'ETTI', '6': 'IEEIA', '7': 'AC'}
        faculty = faculty_map.get(group[0], None)
        self.fac_logo.setObjectName(faculty)

    #Check if buttons is active
    def btn_check(self, year):
        btns = [self.year1, self.year2, self.year3, self.year4]
        for i in range(4):
            if year == str(i+1):
                btns[i].setObjectName('year_btn_active')
                self.current_year = year
            else:
                btns[i].setObjectName('year_btn')
            btns[i].setStyleSheet('styles.css')
    
    def switch_frame(self,cnp,group):
        pass
