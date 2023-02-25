import sqlite3
import sys
import webbrowser
import re
import login
import menu
from PyQt6.QtWidgets import QDialog
from PyQt6 import QtWidgets, QtCore
from ui_login import Ui_ImageDialog
from ui_AboutTheProgram import Ui_AboutTheProgram
from ui_reg import Ui_Reg

from PyQt6.QtCore import Qt, QPoint




class MainWindows(QDialog, Ui_ImageDialog):
    homeAction = None

    oldPos = QPoint()

    def __init__(self):
        super().__init__()
        self.MainMenu = Ui_ImageDialog
        self.setupUi(self)

        # Кнопки
        self.pushClose.clicked.connect(self.CloseWindow)  # При нажатии на кнопку login перейти на новую страницу
        self.pushUrlYouTube.clicked.connect(lambda: webbrowser.open('https://www.youtube.com/'))
        self.pushUrlDiscord.clicked.connect(lambda: webbrowser.open('https://discord.gg/JWTcSq3Y'))
        self.pushUrlFacebook.clicked.connect(lambda: webbrowser.open('https://www.facebook.com/rrarrkfacit'))
        self.pushUrlGitHub.clicked.connect(lambda: webbrowser.open('https://github.com/'))
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.pushLogin.clicked.connect(self.login)
        self.status = self.label_4
        self.status.setStyleSheet('font-size:10px; color: red;text-align: center;')
        self.pushReg.clicked.connect(self.WindowReg)
        self.RemoveWindowsMenu()

    def login(self):
        # создание бд и проверка ввода логина и пароля
        db = sqlite3.connect('database\contacts.db')
        coursor = db.cursor()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        coursor.execute(f'SELECT * FROM users WHERE firstname like \"{username}\" and password like \"{password}\";')
        result_pass = coursor.fetchone()
        db.close()
        # проверка ввода
        if len(username) == 0 or len(password) == 0:
            self.status.setText('Данные не введены')
        else:
            if not result_pass:
                self.status.setText('Логин или пароль указаны не верно')
            else:
                self.TransitionAboutTheProgram()

    def CloseWindow(self):
        sys.exit()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def TransitionAboutTheProgram(self):
        self.abouttheprogram = AboutTheProgram()
        self.abouttheprogram.show()
        self.hide()


    def WindowReg(self):
        self.reg = Refistration()
        self.reg.show()
        self.hide()
    def RemoveWindowsMenu(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)


class AboutTheProgram(QDialog, Ui_AboutTheProgram):
    def __init__(self):
        super().__init__()
        self.abouttheprogram = Ui_AboutTheProgram
        self.setupUi(self)
        self.importmainclass = MainWindows
        self.pushClose.clicked.connect(self.importmainclass.CloseWindow)
        #Импорт основных методов передвижение окна windows и убарать windows элименты из виджета
        self.importmainclass.RemoveWindowsMenu(self)

class Refistration(QDialog, Ui_Reg):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Reg
        self.setupUi(self)
        self.importmainclass = MainWindows
        self.pushClose.clicked.connect(self.importmainclass.CloseWindow)
        self.pushReg.clicked.connect(self.register)
        self.importmainclass.RemoveWindowsMenu(self)
        self.status = self.label_2
        self.status.setStyleSheet('font-size:10px; color: red;text-align: center;')
        self.pushBack.clicked.connect(self.PushBack)

    def PushBack(self):
        self.ui = MainWindows()
        self.ui.show()
        self.hide()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPosition()

    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.oldPos
        self.move(int(self.x() + delta.x()), int(self.y() + delta.y()))
        self.oldPos = event.globalPosition()

    def register(self):
        db = sqlite3.connect('database\contacts.db')
        coursor = db.cursor()
        firstname = self.FirstName.text()
        lastname = self.LastName.text()
        email = self.Email.text()
        password = self.Password.text()
        confirmpassword = self.ConfirmPassword.text()

        #Проверка пароля
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        count_digit = 0
        count_upper = 0
        count_spec=0
        spec_simvol = '!@#$%&'
        for s in password:
            if s.isdigit():
                count_digit += 1
            if s.isupper():
                count_upper+=1
            if s in spec_simvol:
                count_spec+=1
        if count_digit >= 3 and count_upper > 0 and count_spec > 0 and 6 <= len(password) <= 20 and len(firstname) > 0:
            coursor.execute('INSERT INTO  users VALUES(?,?,?,?,?,?);',(firstname, lastname, email, password, confirmpassword,None))
            self.abouttheprogram = AboutTheProgram()
            self.abouttheprogram.show()
            self.hide()
            db.commit()
            db.close()

        else:
            if password != confirmpassword:
                self.status.setText('Пароли не верны')
            else:
                if len(password) < 4:
                    self.status.setText('Пароль слишком короткий')
                else:
                    if len(password) > 20:
                        self.status.setText('Пароль слишком длинный')
                    else:
                        if count_spec == 0:
                            self.status.setText('Нет специальных символов')
                        else:
                            if count_upper == 0:
                                self.status.setText('Нет заглавных букв')
                            else:
                                if count_digit < 3:
                                    self.status.setText('Нет строчных букв')
                                else:
                                    if len(firstname) < 5:
                                        self.status.setText('Ник нейм короткий')
                                    else:
                                        pass





        







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QStackedWidget()
    maindow = MainWindows()
    maindow.show()
    sys.exit(app.exec())
