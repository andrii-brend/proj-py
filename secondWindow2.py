# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow2.ui',
# licensing of 'secondWindow2.ui' applies.
#
# Created: Fri Dec  4 09:36:00 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Menu_oop2(object):
    def setupUi(self, Menu_oop2):
        Menu_oop2.setObjectName("Menu_oop2")
        Menu_oop2.setFixedSize(1000, 700)
        font = QtGui.QFont()
        font.setPointSize(10)
        Menu_oop2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Menu_oop2.setWindowIcon(icon)
        Menu_oop2.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(Menu_oop2)
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
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 70, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 110, 771, 221))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
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
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(810, 640, 181, 51))
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 350, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 390, 771, 161))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        Menu_oop2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu_oop2)
        QtCore.QMetaObject.connectSlotsByName(Menu_oop2)

    def retranslateUi(self, Menu_oop2):
        Menu_oop2.setWindowTitle(QtWidgets.QApplication.translate("Menu_oop2", "Objects and classes", None, -1))
        self.version.setText(QtWidgets.QApplication.translate("Menu_oop2", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Menu_oop2", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("Menu_oop2", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("Menu_oop2", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Menu_oop2", "#Класи і об\'єкти в Python", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Menu_oop2", "Успадкування", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Menu_oop2", "Під спадкуванням розуміється можливість створення нового класу на базі існуючого.\n"
"Спадкування передбачає наявність відносини \"є\" між класом спадкоємцем і класом батьком.\n"
"При цьому клас нащадок буде містити ті ж атрибути і методи, що і базовий клас, але при цьому\n"
"його можна (і потрібно) розширювати через додавання нових методів і атрибутів.\n"
"\n"
"Прикладом базового класу, який демонструє спадкування, можна визначити клас \"автомобіль\",\n"
"що має атрибути: маса, потужність двигуна, об\'єм паливного бака і методи: завести і заглушити.\n"
"У такого класу може бути нащадок - \"вантажний автомобіль\", він буде містити ті ж атрибути і\n"
"методи, що і клас \"автомобіль\", і додаткові властивості: кількість осей, потужність компресора і\n"
"т.п.", None, -1))
        self.wikipedia.setText(QtWidgets.QApplication.translate("Menu_oop2", "Читати на Wikipedia", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("Menu_oop2", "Назад", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Menu_oop2", "Поліморфізм", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("Menu_oop2", "Поліморфізм дозволяє однаково поводитися з об\'єктами, що мають однотипний інтерфейс,\n"
"незалежно від внутрішньої реалізації об\'єкта. Наприклад, з об\'єктом класу\n"
"\"вантажний автомобіль\" можна робити ті ж операції, що і з об\'єктом класу \"автомобіль\", тому що\n"
"перший є спадкоємцем другого, при цьому зворотне твердження не так\n"
"(у всякому разі не завжди). Іншими словами поліморфізм передбачає різну реалізацію методів з\n"
"однаковими іменами. Це дуже корисно при спадкуванні, коли в класі спадкоємця можна\n"
"перевизначити методи класу батька.", None, -1))