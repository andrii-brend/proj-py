# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow_class3.ui',
# licensing of 'secondWindow_class3.ui' applies.
#
# Created: Fri Dec  4 09:35:02 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_class_3(object):
    def setupUi(self, class_3):
        class_3.setObjectName("class_3")
        class_3.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        class_3.setWindowIcon(icon)
        class_3.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(class_3)
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
        self.widget_2.setGeometry(QtCore.QRect(200, 80, 571, 121))
        self.widget_2.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 210, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(200, 250, 571, 121))
        self.widget_3.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_3.setObjectName("widget_3")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 451, 101))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(200, 380, 761, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(200, 470, 571, 61))
        self.widget_4.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_4.setObjectName("widget_4")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setGeometry(QtCore.QRect(20, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setGeometry(QtCore.QRect(390, 80, 451, 121))
        self.widget_6.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_6.setObjectName("widget_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(200, 530, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        class_3.setCentralWidget(self.centralwidget)

        self.retranslateUi(class_3)
        QtCore.QMetaObject.connectSlotsByName(class_3)

    def retranslateUi(self, class_3):
        class_3.setWindowTitle(QtWidgets.QApplication.translate("class_3", "Objects and classes", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("class_3", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("class_3", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("class_3", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("class_3", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("class_3", "#Класи і об\'єкти в Python", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("class_3", "Далі", None, -1))
        self.wikipedia.setText(QtWidgets.QApplication.translate("class_3", "Читати на Wikipedia", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("class_3", "Назад", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("class_3", ">>> rect = Rectangle(10, 20)\n"
">>> rect.width\n"
"10\n"
">>> rect.height\n"
"20", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("class_3", "Якщо звернутися через клас, то отримаємо помилку:", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("class_3", ">>> Rectangle.width\n"
"Traceback (most recent call last):\n"
"  File \"<stdin>\", line 1, in <module>\n"
"AttributeError: type object \'Rectangle\' has no attribute \'width\'", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("class_3", "При цьому, якщо ви звернетеся до статичного атрибуту через екземпляр класу, то все буде ОК,\n"
"до тих пір, поки ви не спробуєте його поміняти.\n"
"\n"
"Перевіримо ще раз значення атрибута default_color:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("class_3", ">>> Rectangle.default_color\n"
"\'green\'", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("class_3", "Присвоємо йому нове значення:\n"
"(Продовження на наступній сторінці)", None, -1))