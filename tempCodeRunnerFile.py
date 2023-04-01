from PyQt6 import QtWidgets, QtCore, QtGui
import screeninfo
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
        self.resize(900, 650)
        self.setMinimumSize(800, 650)
        self.setMaximumSize(800, 650)

        #-----------SING IN-----------

        # labels
        self.log_title = QtWidgets.QLabel('SING IN', self)
        self.log_title.setGeometry(305, 70, 190, 90)
        self.log_title.setObjectName('log_title')
        self.inp_text_name = QtWidgets.QLabel('USERNAME', self)
        self.inp_text_name.setGeometry(150, 245, 130, 50)
        self.inp_text_name.setObjectName('input_text')
        self.inp_text_pass = QtWidgets.QLabel('PASSWORD', self)
        self.inp_text_pass.setGeometry(150, 285, 130, 50)
        self.inp_text_pass.setObjectName('input_text')
        self.vers_text = QtWidgets.QLabel('version 0.1', self)
        self.vers_text.setGeometry(735, 630, 70, 20)
        self.vers_text.setObjectName('version_text')
        # intputs
        self.inp_name = QtWidgets.QLineEdit(self)
        self.inp_name.setGeometry(280, 260, 130, 20)
        self.inp_name.setObjectName('input_logpg')
        self.inp_pass = QtWidgets.QLineEdit(self)
        self.inp_pass.setGeometry(280, 300, 130, 20)
        self.inp_pass.setObjectName('input_logpg')
        self.inp_pass.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        #buttons
        self.btn_log = QtWidgets.QPushButton(self)
        self.btn_log.setText('LOGIN')
        self.btn_log.setGeometry(405, 340, 100, 40)
        self.btn_log.setObjectName('btn_log')




#Running App

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    with open('styles/style.css', 'r') as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MyApp()
    window.show()
    sys.exit(app.exec())