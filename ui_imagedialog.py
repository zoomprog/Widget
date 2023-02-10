# Form implementation generated from reading ui file 'ui_imagedialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        ImageDialog.setObjectName("ImageDialog")
        ImageDialog.resize(412, 419)
        font = QtGui.QFont()
        font.setPointSize(9)
        ImageDialog.setFont(font)
        ImageDialog.setStyleSheet("border-radius:25px;")
        self.widget = QtWidgets.QWidget(parent=ImageDialog)
        self.widget.setGeometry(QtCore.QRect(-40, -30, 370, 480))
        self.widget.setStyleSheet("QPushButton#pushLogin{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border_radius:5px;\n"
"}\n"
"QPushButton#pushLogin:hover{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushLogin:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105,118,132,200);\n"
"}\n"
"QPushButton#pushUrlDiscord{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#pushUrlDiscord:hover{\n"
"    color:rgba(155,168,182,220);\n"
"}\n"
"QPushButton#pushUrlDiscord:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115,128,142,255)\n"
"}\n"
"QPushButton#pushUrlGitHub{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#pushUrlGitHub:hover{\n"
"    color:rgba(155,168,182,220);\n"
"}\n"
"QPushButton#pushUrlGitHub:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115,128,142,255)\n"
"}\n"
"QPushButton#pushUrlFacebook{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#pushUrlFacebook:hover{\n"
"    color:rgba(155,168,182,220);\n"
"}\n"
"QPushButton#pushUrlFacebook:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115,128,142,255)\n"
"}\n"
"QPushButton#pushUrlYouTube{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#pushUrlYouTube:hover{\n"
"    color:rgba(155,168,182,220);\n"
"}\n"
"QPushButton#pushUrlYouTubek:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115,128,142,255)\n"
"}\n"
"QPushButton#pushClose{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgba(85,98,112,255);\n"
"}\n"
"QPushButton#pushClose:hover{\n"
"    color:rgba(155,168,182,220);\n"
"}\n"
"QPushButton#pushClose:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115,128,142,255)\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 300, 420))
        self.label.setStyleSheet("border-image: url(:/image/1618615593_15-phonoteka_org-p-temno-sinii-tsvet-fon-16.jpg);\n"
"border-radius:20px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 280, 390))
        font = QtGui.QFont()
        font.setPointSize(3)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border-radius:25px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(135, 90, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(255,255,255,210)")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 150, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(108,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"pading-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 220, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(108,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"pading-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushLogin = QtWidgets.QPushButton(parent=self.widget)
        self.pushLogin.setGeometry(QtCore.QRect(90, 290, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushLogin.setFont(font)
        self.pushLogin.setObjectName("pushLogin")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(110, 350, 201, 21))
        self.label_4.setStyleSheet("color:rgba(255,255,255,140);")
        self.label_4.setObjectName("label_4")
        self.pushUrlDiscord = QtWidgets.QPushButton(parent=self.widget)
        self.pushUrlDiscord.setGeometry(QtCore.QRect(90, 400, 30, 30))
        self.pushUrlDiscord.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushUrlDiscord.setFont(font)
        self.pushUrlDiscord.setObjectName("pushUrlDiscord")
        self.pushUrlGitHub = QtWidgets.QPushButton(parent=self.widget)
        self.pushUrlGitHub.setGeometry(QtCore.QRect(140, 400, 30, 30))
        self.pushUrlGitHub.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushUrlGitHub.setFont(font)
        self.pushUrlGitHub.setObjectName("pushUrlGitHub")
        self.pushUrlFacebook = QtWidgets.QPushButton(parent=self.widget)
        self.pushUrlFacebook.setGeometry(QtCore.QRect(190, 400, 30, 30))
        self.pushUrlFacebook.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushUrlFacebook.setFont(font)
        self.pushUrlFacebook.setObjectName("pushUrlFacebook")
        self.pushUrlYouTube = QtWidgets.QPushButton(parent=self.widget)
        self.pushUrlYouTube.setGeometry(QtCore.QRect(240, 400, 30, 30))
        self.pushUrlYouTube.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushUrlYouTube.setFont(font)
        self.pushUrlYouTube.setObjectName("pushUrlYouTube")
        self.pushClose = QtWidgets.QPushButton(parent=self.widget)
        self.pushClose.setGeometry(QtCore.QRect(300, 40, 30, 30))
        self.pushClose.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(22)
        self.pushClose.setFont(font)
        self.pushClose.setObjectName("pushClose")

        self.retranslateUi(ImageDialog)
        QtCore.QMetaObject.connectSlotsByName(ImageDialog)

    def retranslateUi(self, ImageDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageDialog.setWindowTitle(_translate("ImageDialog", "Dialog"))
        self.label_3.setText(_translate("ImageDialog", "Login in"))
        self.lineEdit.setPlaceholderText(_translate("ImageDialog", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("ImageDialog", "Password"))
        self.pushLogin.setText(_translate("ImageDialog", "L o g i n"))
        self.label_4.setText(_translate("ImageDialog", "Введите ваш логин и пароль!"))
        self.pushUrlDiscord.setText(_translate("ImageDialog", "Y"))
        self.pushUrlGitHub.setText(_translate("ImageDialog", ")"))
        self.pushUrlFacebook.setText(_translate("ImageDialog", "E"))
        self.pushUrlYouTube.setText(_translate("ImageDialog", "P"))
        self.pushClose.setText(_translate("ImageDialog", "´"))
