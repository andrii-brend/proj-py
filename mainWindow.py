# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui',
# licensing of 'mainWindow.ui' applies.
#
# Created: Fri Dec  4 09:34:16 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Menu.setWindowIcon(icon)
        Menu.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, -40, 201, 851))
        self.widget.setStyleSheet("background:#FFFFFF")
        self.widget.setObjectName("widget")
        self.version = QtWidgets.QLabel(self.widget)
        self.version.setGeometry(QtCore.QRect(20, 720, 71, 16))
        self.version.setObjectName("version")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.exit = QtWidgets.QPushButton(self.widget)
        self.exit.setGeometry(QtCore.QRect(20, 640, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.exit.setFont(font)
        self.exit.setStyleSheet("QPushButton{\n"
"    background:#F9F9F9;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:rgb(255, 139, 124)}")
        self.exit.setObjectName("exit")
        self.about_pr = QtWidgets.QPushButton(self.widget)
        self.about_pr.setGeometry(QtCore.QRect(20, 570, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.about_pr.setFont(font)
        self.about_pr.setStyleSheet("QPushButton{\n"
"    background:#F9F9F9;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.about_pr.setObjectName("about_pr")
        self.bonus = QtWidgets.QPushButton(self.widget)
        self.bonus.setGeometry(QtCore.QRect(20, 500, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.bonus.setFont(font)
        self.bonus.setStyleSheet("QPushButton{\n"
"    background:#F9F9F9;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.bonus.setObjectName("bonus")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 121, 111))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/python logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 80, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 270, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 140, 711, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 120, 411, 16))
        self.label_8.setObjectName("label_8")
        self.main_oop = QtWidgets.QPushButton(self.centralwidget)
        self.main_oop.setGeometry(QtCore.QRect(200, 190, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.main_oop.setFont(font)
        self.main_oop.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.main_oop.setObjectName("main_oop")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 320, 711, 51))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 296, 411, 20))
        self.label_10.setObjectName("label_10")
        self.main_classes = QtWidgets.QPushButton(self.centralwidget)
        self.main_classes.setGeometry(QtCore.QRect(200, 380, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.main_classes.setFont(font)
        self.main_classes.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.main_classes.setObjectName("main_classes")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 450, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 480, 411, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(200, 510, 221, 21))
        self.label_13.setObjectName("label_13")
        self.practic = QtWidgets.QPushButton(self.centralwidget)
        self.practic.setGeometry(QtCore.QRect(200, 540, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.practic.setFont(font)
        self.practic.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.practic.setObjectName("practic")
        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QtWidgets.QApplication.translate("Menu", "Objects and classes", None, -1))
        self.version.setText(QtWidgets.QApplication.translate("Menu", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Menu", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("Menu", "Вихід", None, -1))
        self.about_pr.setText(QtWidgets.QApplication.translate("Menu", "Про програму", None, -1))
        self.bonus.setText(QtWidgets.QApplication.translate("Menu", "Бонус", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Menu", "#Класи і об\'єкти в Python", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Menu", "Основні поняття ООП", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Menu", "Класи в Python", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Menu", "Об\'єктно-орієнтоване програмування (ООП) є методологією розробки програмного забезпечення, в основі якої лежить\n"
" поняття класу і об\'єкту, при цьому сама...", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Menu", "__________________________________________________________", None, -1))
        self.main_oop.setText(QtWidgets.QApplication.translate("Menu", "Перейти до \n"
"вивчення", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Menu", "Клас складається з оголошення (інструкція class), імені класу (нашому випадку це ім\'я C)\n"
" і тіла класу, яке містить...", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Menu", "__________________________________________________________", None, -1))
        self.main_classes.setText(QtWidgets.QApplication.translate("Menu", "Перейти до \n"
"вивчення", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("Menu", "Практика", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("Menu", "__________________________________________________________", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate("Menu", "Практика по пройденому матеріалу", None, -1))
        self.practic.setText(QtWidgets.QApplication.translate("Menu", "Перейти до\n"
"практики", None, -1))