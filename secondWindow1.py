# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow1.ui',
# licensing of 'secondWindow1.ui' applies.
#
# Created: Fri Dec  4 09:35:54 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Menu_oop1(object):
    def setupUi(self, Menu_oop1):
        Menu_oop1.setObjectName("Menu_oop1")
        Menu_oop1.setFixedSize(1000, 700)
        font = QtGui.QFont()
        font.setPointSize(10)
        Menu_oop1.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Menu_oop1.setWindowIcon(icon)
        Menu_oop1.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(Menu_oop1)
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
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 80, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 120, 411, 16))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 140, 771, 171))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 320, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 370, 771, 181))
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
        Menu_oop1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu_oop1)
        QtCore.QMetaObject.connectSlotsByName(Menu_oop1)

    def retranslateUi(self, Menu_oop1):
        Menu_oop1.setWindowTitle(QtWidgets.QApplication.translate("Menu_oop1", "Objects and classes", None, -1))
        self.version.setText(QtWidgets.QApplication.translate("Menu_oop1", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Menu_oop1", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("Menu_oop1", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("Menu_oop1", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Menu_oop1", "#Класи і об\'єкти в Python", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Menu_oop1", "Основні поняття ООП", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Menu_oop1", "__________________________________________________________", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Menu_oop1", "Об\'єктно-орієнтоване програмування (ООП) є методологією розробки програмного забезпечення,\n"
"в основі якої лежить поняття класу і об\'єкту, при цьому сама програма створюється \n"
"як деяка сукупність об\'єктів, які взаємодію один з одним і з зовнішнім світом.\n"
"Кожен об\'єкт є екземпляром деякого класу. Класи утворюють ієрархії.\n"
"Більш детально про поняття ООП можна прочитати на вікіпедії.\n"
"\n"
"Виділяють три основних \"стовпи\" ООП- це інкапсуляція, успадкування і поліморфізм.", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Menu_oop1", "Інкапсуляція", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Menu_oop1", "Під інкапсуляцією розуміється приховування деталей реалізації, даних і т.п. від зовнішньої\n"
"сторони. Наприклад, можна визначити клас \"холодильник\", який буде містити наступні дані:\n"
"виробник, обсяг, кількість камер зберігання, споживана потужність і т.п., і методи:\n"
"відкрити / закрити холодильник, включити / виключити, але при цьому реалізація того,\n"
"як відбувається безпосередньо включення і виключення користувачеві вашого класу не\n"
"доступна, що дозволяє її міняти без побоювання, що це може відбитися на використовує\n"
"клас «холодильник» програмою. При цьому клас стає новим типом даних в рамках\n"
"розроблюваної програми. Можна створювати змінні цього нового типу, такі змінні називаються\n"
"об\'єкти.", None, -1))
        self.wikipedia.setText(QtWidgets.QApplication.translate("Menu_oop1", "Читати на Wikipedia", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("Menu_oop1", "Далі", None, -1))
