from PyQt6 import QtWidgets, QtCore, QtGui
import sqlite3, sys

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('STD-Manager')
        self.resize(1000,850)
        self.setMinimumSize(QtCore.QSize(1000, 700))
        self.setMaximumSize(QtCore.QSize(1000, 700))
        self.page1 = AddPage()
        self.page2 = DelPage()
        self.stack_container = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stack_container)
        self.stack_container.addWidget(self.page1)
        self.stack_container.addWidget(self.page2)
        self.stack_container.setCurrentWidget(self.page1)
        #labels
        self.add_btn = QtWidgets.QPushButton('ADD', self)
        self.add_btn.move(20, 80)
        self.add_btn.clicked.connect(lambda: self.switch_frame(2))
        self.del_btn = QtWidgets.QPushButton('DEL', self)
        self.del_btn.move(20, 20)
        self.del_btn.clicked.connect(lambda: self.switch_frame(1))

    def switch_frame(self, page):
        if page == 2:
            self.stack_container.setCurrentWidget(self.page2)
        elif page == 1:
            self.stack_container.setCurrentWidget(self.page1)
        else:
            print('error 212')
        
class AddPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel('TEST 1', self)
        label.move(300, 100)
        label.setObjectName('a')

class DelPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel('TEST 2', self)
        label.move(400, 100)
        label.setObjectName('a')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = Main()
    window.show()
    sys.exit(app.exec())
