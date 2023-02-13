import sqlite3
import sys,res,menu,time,os
import webbrowser

import ui_imagedialog
from PyQt6.QtWidgets import QApplication, QDialog,QFileDialog,QMainWindow,QLabel,QLineEdit,QPushButton,QGridLayout,QSizePolicy
from PyQt6 import QtWidgets,QtCore
from ui_imagedialog import Ui_ImageDialog
from AboutTheProgram import Ui_AboutTheProgram
from PyQt6.QtCore import Qt,QPoint
from PyQt6.QtSql import QSqlDatabase


class MainWindows(QDialog,Ui_ImageDialog):
    homeAction = None

    oldPos = QPoint()

    def __init__(self):
        super().__init__()
        self.MainMenu = Ui_ImageDialog
        self.setupUi(self)
        #Кнопки
        self.pushClose.clicked.connect(self.CloseWindow)# При нажатии на кнопку login перейти на новую страницу
        self.pushUrlYouTube.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/'))
        self.pushUrlDiscord.clicked.connect(lambda: webbrowser.open('https://discord.gg/JWTcSq3Y'))
        self.pushUrlFacebook.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/rrarrkfacit'))
        self.pushUrlGitHub.clicked.connect(lambda: webbrowser.open('https://github.com/'))
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

        #bd
        self.pushLogin.clicked.connect(self.login)

    def login(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        if len(username)==0 or len(password)==0:
            return
        db = sqlite3.connect('database\contacts.db')
        coursor = db.cursor()
        coursor.execute(f'SELECT * FROM users WHERE username like \"{username}\" and password like \"{password}\";')
        result_pass = coursor.fetchone()

        if not result_pass:
            print('Логин и пароль указаны не верно')
        else:
            self.TransitionAboutTheProgram()

    def CloseWindow(self):
        sys.exit()
    def TransitionAboutTheProgram(self):
        abouttheprogram=AboutTheProgram()
        window.addWidget(abouttheprogram)
        window.setCurrentIndex(window.currentIndex()+1)




class AboutTheProgram(QDialog,Ui_AboutTheProgram):
    def __init__(self):
        super().__init__()
        self.abouttheprogram = Ui_AboutTheProgram
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QStackedWidget()
    window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
    mainwindow=MainWindows()
    window.addWidget(mainwindow)
    window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
    window.resize(1280,720)
    window.show()
    sys.exit(app.exec())