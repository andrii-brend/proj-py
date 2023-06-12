# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow_class2.ui',
# licensing of 'secondWindow_class2.ui' applies.
#
# Created: Fri Dec  4 09:34:56 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_class_2(object):
    def setupUi(self, class_2):
        class_2.setObjectName("class_2")
        class_2.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        class_2.setWindowIcon(icon)
        class_2.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(class_2)
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
        self.wikipedia_class = QtWidgets.QPushButton(self.centralwidget)
        self.wikipedia_class.setGeometry(QtCore.QRect(200, 660, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.wikipedia_class.setFont(font)
        self.wikipedia_class.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:rgb(255, 249, 71)}")
        self.wikipedia_class.setObjectName("wikipedia_class")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 80, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 120, 771, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(200, 200, 451, 121))
        self.widget_2.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(390, 80, 451, 121))
        self.widget_3.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_3.setObjectName("widget_3")
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
        self.label_10.setGeometry(QtCore.QRect(200, 330, 771, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(200, 400, 451, 61))
        self.widget_4.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_4.setObjectName("widget_4")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(390, 80, 451, 121))
        self.widget_5.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_5.setObjectName("widget_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 470, 771, 101))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        class_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(class_2)
        QtCore.QMetaObject.connectSlotsByName(class_2)

    def retranslateUi(self, class_2):
        class_2.setWindowTitle(QtWidgets.QApplication.translate("class_2", "Objects and classes", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("class_2", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("class_2", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("class_2", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("class_2", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("class_2", "#Класи і об\'єкти в Python", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("class_2", "Далі", None, -1))
        self.wikipedia_class.setText(QtWidgets.QApplication.translate("class_2", "Читати на Wikipedia", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("class_2", "Статичні і динамічні атрибути класа", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("class_2", "Як вже було сказано вище, клас може містити атрибути і методи. Атрибут може бути статичним\n"
"і динамічним (рівня об\'єкта класу). Суть в тому, що для роботи зі статичним атрибутом, вам не\n"
"потрібно створювати екземпляр класу, а для роботи з динамічним - потрібно. приклад:", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("class_2", "class Rectangle:\n"
"    default_color = \"green\"\n"
"\n"
"    def __init__(self, width, height):\n"
"        self.width = width\n"
"        self.height = height", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("class_2", "Назад", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("class_2", "У представленому вище класі, атрибут default_color - це статичний атрибут, і доступ до нього,\n"
"як було сказано вище, можна отримати не створюючи об\'єкт класу Rectangle.", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("class_2", ">>> Rectangle.default_color\n"
"\'green\'", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("class_2", "width і height - це динамічні атрибути, при їх створенні було використано ключове слово self.\n"
"Поки просто прийміть це як належне, більш детально про self буде розказано нижче.\n"
"Для доступу до width і height попередньо потрібно створити об\'єкт класу Rectangle:\n"
"(Продовження на наступній сторінці)", None, -1))
