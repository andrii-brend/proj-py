# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow_class7.ui',
# licensing of 'secondWindow_class7.ui' applies.
#
# Created: Fri Dec  4 09:35:40 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_class_7(object):
    def setupUi(self, class_7):
        class_7.setObjectName("class_7")
        class_7.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        class_7.setWindowIcon(icon)
        class_7.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(class_7)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-10, -40, 201, 851))
        self.widget.setStyleSheet("background:#FFFFFF")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 720, 71, 16))
        self.label_2.setObjectName("label_2")
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
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 121, 111))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/python logo.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.back_to_menu = QtWidgets.QPushButton(self.widget)
        self.back_to_menu.setGeometry(QtCore.QRect(20, 570, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.back_to_menu.setFont(font)
        self.back_to_menu.setStyleSheet("QPushButton{\n"
"    background:#F9F9F9;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.back_to_menu.setObjectName("back_to_menu")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.back_2 = QtWidgets.QPushButton(self.centralwidget)
        self.back_2.setGeometry(QtCore.QRect(810, 640, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.back_2.setFont(font)
        self.back_2.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.back_2.setObjectName("back_2")
        self.wikipedia = QtWidgets.QPushButton(self.centralwidget)
        self.wikipedia.setGeometry(QtCore.QRect(200, 660, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.wikipedia.setFont(font)
        self.wikipedia.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:rgb(255, 249, 71)}")
        self.wikipedia.setObjectName("wikipedia")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 80, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 120, 791, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(200, 200, 571, 151))
        self.widget_3.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_3.setObjectName("widget_3")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 451, 111))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 360, 801, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        class_7.setCentralWidget(self.centralwidget)

        self.retranslateUi(class_7)
        QtCore.QMetaObject.connectSlotsByName(class_7)

    def retranslateUi(self, class_7):
        class_7.setWindowTitle(QtWidgets.QApplication.translate("class_7", "Objects and classes", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("class_7", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("class_7", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("class_7", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("class_7", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("class_7", "#Класи і об\'єкти в Python", None, -1))
        self.back_2.setText(QtWidgets.QApplication.translate("class_7", "Назад", None, -1))
        self.wikipedia.setText(QtWidgets.QApplication.translate("class_7", "Читати на Wikipedia", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("class_7", "Що таке self?", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("class_7", "До цього моменту ви вже встигли познайомитися з ключовим словом self. self - це посилання на\n"
"поточний екземпляр класу, в таких мовах як Java, C # аналогом є ключове слово this. Через self\n"
"ви отримуєте доступ до атрибутів і методів класу всередині нього:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("class_7", "class Rectangle:\n"
"    def __init__(self, width, height):\n"
"        self.width = width\n"
"        self.height = height\n"
"    def area(self):\n"
"        return self.width * self.height", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("class_7", "У наведеній реалізації метод area отримує доступ до атрибутів width і height для розрахунку площі.\n"
"Якби в якості першого параметра не було вказано self, то при спробі викликати area програма була\n"
"б зупинена з помилкою.", None, -1))