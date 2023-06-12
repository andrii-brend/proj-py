# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow_class5.ui',
# licensing of 'secondWindow_class5.ui' applies.
#
# Created: Fri Dec  4 09:35:24 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_class_5(object):
    def setupUi(self, class_5):
        class_5.setObjectName("class_5")
        class_5.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        class_5.setWindowIcon(icon)
        class_5.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(class_5)
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
"    background:rgb(255, 249, 71)}\n"
"")
        self.wikipedia.setObjectName("wikipedia")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 80, 391, 31))
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
        self.label_10.setGeometry(QtCore.QRect(200, 110, 781, 131))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(200, 250, 571, 211))
        self.widget_3.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_3.setObjectName("widget_3")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 451, 171))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 480, 781, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        class_5.setCentralWidget(self.centralwidget)

        self.retranslateUi(class_5)
        QtCore.QMetaObject.connectSlotsByName(class_5)

    def retranslateUi(self, class_5):
        class_5.setWindowTitle(QtWidgets.QApplication.translate("class_5", "Objects and classes", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("class_5", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("class_5", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("class_5", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("class_5", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("class_5", "#Класи і об\'єкти в Python", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("class_5", "Далі", None, -1))
        self.wikipedia.setText(QtWidgets.QApplication.translate("class_5", "Читати на Wikipedia", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("class_5", "Методи класа", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("class_5", "Назад", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("class_5", "Додамо до нашого класу метод. Метод - це функція, яка перебуває всередині класу і виконує\n"
"певну роботу. Методи бувають статичними, класовими (середнє між статичними і звичайними) і\n"
"рівня класу (будемо їх називати просто словом метод). Статичний метод створюється з\n"
"декоратором @staticmethod, класовий - з декоратором @classmethod, першим аргументом в нього\n"
"передається cls, звичайний метод створюється без спеціального декоратора, йому першим\n"
"аргументом передається self:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("class_5", "class MyClass:\n"
"    @staticmethod\n"
"    def ex_static_method():\n"
"        print(\"static method\")\n"
"    @classmethod\n"
"    def ex_class_method(cls):\n"
"        print(\"class method\")\n"
"    def ex_method(self):\n"
"        print(\"method\")", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("class_5", "Статичний і класовий метод можна викликати, не створюючи екземпляр класу, а для виклику\n"
"ex_method () потрібен об\'єкт", None, -1))