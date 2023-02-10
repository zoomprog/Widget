import sys,res
from PyQt6.QtWidgets import QApplication, QDialog,QFileDialog
from PyQt6 import QtWidgets,QtCore
from ui_imagedialog import Ui_ImageDialog
from AboutTheProgram import Ui_AboutTheProgram
from PyQt6.QtCore import Qt

class MainWindows(QDialog,Ui_ImageDialog):
    def __init__(self):
        super().__init__()

        self.MainMenu = Ui_ImageDialog
        self.setupUi(self)

        self.pushClose.clicked.connect(self.CloseWindow)# При нажатии на кнопку login перейти на новую страницу

        self.pushLogin.clicked.connect(self.TransitionAboutTheProgram)


    def CloseWindow(self):
        self.close()

    def TransitionAboutTheProgram(self):
        abouttheprogram=AboutTheProgram()
        window.addWidget(abouttheprogram)
        window.setCurrentIndex(window.currentIndex()+1)




class AboutTheProgram(QDialog,Ui_AboutTheProgram):
    def __init__(self):
        super().__init__()
        self.abouttheprogram = Ui_AboutTheProgram
        self.setupUi(self)



app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QStackedWidget()
window.setWindowFlags(Qt.WindowType.FramelessWindowHint)
mainwindow=MainWindows()
window.addWidget(mainwindow)
window.resize(370,480)
window.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)




window.show()
sys.exit(app.exec())