from PyQt6 import QtWidgets, QtCore
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

        #-----------SING IN-----------

        # title
        self.log_title = QtWidgets.QLabel('SING IN', self)
        self.log_title.setGeometry(385, 70, 130, 50)
        self.log_title.setObjectName('log_title')
        self.inp_text_name = QtWidgets.QLabel('USERNAME', self)
        self.inp_text_name.setGeometry(280, 165, 100, 50)
        self.inp_text_name.setObjectName('input_text')
        self.inp_text_pass = QtWidgets.QLabel('PASSWORD', self)
        self.inp_text_pass.setGeometry(280, 195, 100, 50)
        self.inp_text_pass.setObjectName('input_text')
        # intputs
        self.inp_name = QtWidgets.QLineEdit(self)
        self.inp_name.setGeometry(390, 180, 130, 20)
        self.inp_name.setObjectName('input_logpg')
        self.inp_pass = QtWidgets.QLineEdit(self)
        self.inp_pass.setGeometry(390, 210, 130, 20)
        self.inp_pass.setObjectName('input_logpg')
        self.inp_pass.password



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