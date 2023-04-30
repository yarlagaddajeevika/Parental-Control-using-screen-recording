import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import screen_recording as sr
import load_model as lm
import sys
sys.path.append('database')
import databaseConnection as db

import sqlite3


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("./UI/welcomescreen.ui",self)
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotocreate(self):
        create = CreateAccScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("./UI/login.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
    
    def gotohome(self):
        home = HomeScreen()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields.")

        else:
            result_pass = db.authenticateUser(user)
            if result_pass == password:
                print("Successfully logged in.")
                self.error.setText("")
                self.login.clicked.connect(self.gotohome)
            else:
                self.error.setText("Invalid username or password")

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("./UI/createacc.ui",self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)

    def signupfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(user)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            result_pass = db.CreateUser(user,password)

            if result_pass:
                print("Successfully signed up.")
                self.error.setText("")
                self.signup.clicked.connect(self.gotologin)
            else:
                self.error.setText("Unable to create user")

            # fillprofile = FillProfileScreen()
            # widget.addWidget(fillprofile)
            # widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class HomeScreen(QDialog):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi("./UI/home.ui",self)
        self.start.clicked.connect(self.gotologin)
        self.stop.clicked.connect(self.gotocreate)

    def gotologin(self):
        print("start")
        sr.record_screen_and_audio("recording.mp4")

    def gotocreate(self):
        print("stop")
        lm.model()

class FillProfileScreen(QDialog):
    def __init__(self):
        super(FillProfileScreen, self).__init__()
        loadUi("fillprofile.ui",self)
        self.image.setPixmap(QPixmap('placeholder.png'))



# main
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
