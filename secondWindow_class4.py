# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow_class4.ui',
# licensing of 'secondWindow_class4.ui' applies.
#
# Created: Fri Dec  4 09:35:17 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_class_4(object):
    def setupUi(self, class_4):
        class_4.setObjectName("class_4")
        class_4.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        class_4.setWindowIcon(icon)
        class_4.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(class_4)
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
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(200, 80, 571, 81))
        self.widget_2.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 160, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(200, 200, 571, 101))
        self.widget_3.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_3.setObjectName("widget_3")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 271, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 300, 781, 101))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(200, 410, 571, 81))
        self.widget_4.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_4.setObjectName("widget_4")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 500, 771, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        class_4.setCentralWidget(self.centralwidget)

        self.retranslateUi(class_4)
        QtCore.QMetaObject.connectSlotsByName(class_4)

    def retranslateUi(self, class_4):
        class_4.setWindowTitle(QtWidgets.QApplication.translate("class_4", "Objects and classes", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("class_4", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("class_4", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("class_4", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("class_4", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("class_4", "#Класи і об\'єкти в Python", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("class_4", "Далі", None, -1))
        self.wikipedia.setText(QtWidgets.QApplication.translate("class_4", "Читати на Wikipedia", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("class_4", "Назад", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("class_4", ">>> Rectangle.default_color = \"red\"\n"
">>> Rectangle.default_color\n"
"\'red\'", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("class_4", "Створимо два об\'єкти класу Rectangle і перевіримо, що default_color у них збігається:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("class_4", ">>> r1 = Rectangle(1,2)\n"
">>> r2 = Rectangle(10, 20)\n"
">>> r1.default_color\n"
"\'red\'\n"
">>> r2.default_color\n"
"\'red\'", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("class_4", "Якщо поміняти значення default_color через ім\'я класу Rectangle, то все буде очікувано:\n"
"у об\'єктів r1 і r2 це значення зміниться, але якщо поміняти його через екземпляр класу, то у\n"
"примірника буде створено атрибут з таким же ім\'ям як статичний, а доступ до останнього буде\n"
"втрачено : Міняємо default_color через r1:", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("class_4", ">>> r1.default_color = \"blue\"\n"
">>> r1.default_color\n"
"\'blue\'", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("class_4", "При цьому у r2 залишається значення статичного атрибута. Взагалі безпосередньо працювати з\n"
"атрибутами - не дуже хороша ідея, краще для цього використовувати властивості.", None, -1))