from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("login_icon.png"))

        # set background color
        self.setStyleSheet("background-color: #F7CA18")

        # create username and password labels and entry fields
        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()
        self.username_entry.setStyleSheet("background-color: white")

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setStyleSheet("background-color: white")
        self.password_entry.setEchoMode(QLineEdit.Password)

        # create login and create account buttons
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background-color: #34495E; color: white")
        self.login_button.clicked.connect(self.login)

        self.create_account_button = QPushButton("Create Account")
        self.create_account_button.setStyleSheet("background-color: #34495E; color: white")
        self.create_account_button.clicked.connect(self.create_account)

        # create layout and add widgets
        layout = QVBoxLayout()
        login_layout = QHBoxLayout()
        login_layout.addWidget(self.username_label)
        login_layout.addWidget(self.username_entry)
        layout.addLayout(login_layout)
        login_layout = QHBoxLayout()
        login_layout.addWidget(self.password_label)
        login_layout.addWidget(self.password_entry)
        layout.addLayout(login_layout)
        layout.addWidget(self.login_button)
        layout.addWidget(self.create_account_button)

        self.setLayout(layout)
        self.show()

    def login(self):
        # handle login functionality here
        username = self.username_entry.text()
        password = self.password_entry.text()
        # perform login validation

    def create_account(self):
        # handle create account functionality here
        CreateAccountApp()

class CreateAccountApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Account")
        self.setWindowIcon(QIcon("create_account_icon.png"))

        # set background color
        self.setStyleSheet("background-color: #2ECC71")

        # create username, password and email labels and entry fields
        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()
        self.username_entry.setStyleSheet("background-color: white")

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setStyleSheet("background-color: white")
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.email_label = QLabel("Email:")
        self.email_entry = QLineEdit()
        self.email_entry.setStyleSheet("background-color: white")

        # create create account and cancel buttons
        self.create_account_button = QPushButton("Create Account")
        self.create_account_button.setStyleSheet("background-color: #34495E; color: white")
        self.create_account_button.clicked.connect(self.create_account)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.setStyleSheet("background-color: #34495E; color: white")
        self.cancel_button.clicked.connect(self.cancel)

        # create layout and add widgets
        layout = QVBoxLayout()
        login_layout = QHBoxLayout()
        login_layout.addWidget(self.username_label)
        login_layout.addWidget(self.username_entry)
        layout.addLayout(login_layout)
        login_layout = QHBoxLayout()
        login_layout.addWidget(self.password_label)
        login_layout.addWidget(self.password_entry)
        layout.addLayout(login_layout)
        login_layout = QHBoxLayout()
        login_layout.addWidget(self.email_label)
        login_layout.addWidget(self.email)
