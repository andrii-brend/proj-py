# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow_class6.ui',
# licensing of 'secondWindow_class6.ui' applies.
#
# Created: Fri Dec  4 09:35:31 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_class_6(object):
    def setupUi(self, class_6):
        class_6.setObjectName("class_6")
        class_6.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        class_6.setWindowIcon(icon)
        class_6.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(class_6)
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
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(810, 640, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.next.setFont(font)
        self.next.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.next.setObjectName("next")
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
        self.label_7.setGeometry(QtCore.QRect(200, 80, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(620, 640, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.back.setObjectName("back")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 110, 791, 191))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(200, 310, 571, 291))
        self.widget_3.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_3.setObjectName("widget_3")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 451, 251))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        class_6.setCentralWidget(self.centralwidget)

        self.retranslateUi(class_6)
        QtCore.QMetaObject.connectSlotsByName(class_6)

    def retranslateUi(self, class_6):
        class_6.setWindowTitle(QtWidgets.QApplication.translate("class_6", "Objects and classes", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("class_6", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("class_6", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("class_6", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("class_6", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("class_6", "#Класи і об\'єкти в Python", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("class_6", "Далі", None, -1))
        self.wikipedia.setText(QtWidgets.QApplication.translate("class_6", "Читати на Wikipedia", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("class_6", "Конструктор класу і ініціалізація екземпляра класу", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("class_6", "Назад", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("class_6", "В Python поділяють конструктор класу і метод для ініціалізації екземпляра класу. Конструктор\n"
"класу це метод __new __ (cls, * args, ** kwargs) для ініціалізації екземпляра класу використовується\n"
"метод __init __ (self). При цьому, як ви могли помітити __new__ - це класовий метод, а __init__ таким\n"
"не є. Метод __new__ рідко переопределяется, частіше використовується реалізація від базового\n"
"класу object (див. Розділ Спадкування), __init__ ж навпаки є дуже зручним способом задати\n"
"параметри об\'єкта при його створенні.\n"
"\n"
"Створимо реалізацію класу Rectangle зі зміненим конструктором і ініціалізатор, через який\n"
"задається ширина і висота прямокутника:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("class_6", "class Rectangle:\n"
"    def __new__(cls, *args, **kwargs):\n"
"        print(\"Hello from __new__\")\n"
"        return super().__new__(cls)\n"
"    def __init__(self, width, height):\n"
"        print(\"Hello from __init__\")\n"
"        self.width = width\n"
"        self.height = height\n"
">>> rect = Rectangle(10, 20)\n"
"Hello from __new__\n"
"Hello from __init__\n"
">>> rect.width\n"
"10\n"
">>> rect.height\n"
"20", None, -1))