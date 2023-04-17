from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3, sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,850)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.page1 = AddNew()
        self.stack_container = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack_container)
        self.stack_container.addWidget(self.page1)
        self.stack_container.setCurrentWidget(self.page1)
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
