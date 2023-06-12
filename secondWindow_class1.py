# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow_class1.ui',
# licensing of 'secondWindow_class1.ui' applies.
#
# Created: Fri Dec  4 09:34:46 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_class_1(object):
    def setupUi(self, class_1):
        class_1.setObjectName("class_1")
        class_1.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        class_1.setWindowIcon(icon)
        class_1.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(class_1)
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
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 70, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 100, 411, 20))
        self.label_10.setObjectName("label_10")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 120, 771, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(200, 170, 451, 51))
        self.widget_2.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 220, 781, 101))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 320, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
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
        class_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(class_1)
        QtCore.QMetaObject.connectSlotsByName(class_1)

    def retranslateUi(self, class_1):
        class_1.setWindowTitle(QtWidgets.QApplication.translate("class_1", "Objects and classes", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("class_1", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("class_1", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("class_1", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("class_1", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("class_1", "#Класи і об\'єкти в Python", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("class_1", "Класи в Python", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("class_1", "__________________________________________________________", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("class_1", "Створення класу в Python починається з інструкції class. Ось так буде виглядати\n"
"мінімальний клас.", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("class_1", "class C: \n"
"    pass", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("class_1", "Клас складається з оголошення (інструкція class), імені класу (нашому випадку це ім\'я C) і тіла\n"
"класу, яке містить атрибути і методи (в нашому мінімальному класі є тільки одна інструкція pass)\n"
"\n"
"Для того щоб створити об\'єкт класу необхідно скористатися наступним синтаксисом:", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("class_1", "імя_об\'єкта = ім\'я_класу ()", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("class_1", "Далі", None, -1))
        self.wikipedia_class.setText(QtWidgets.QApplication.translate("class_1", "Читати на Wikipedia", None, -1))