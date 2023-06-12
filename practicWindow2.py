# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practicWindow2.ui',
# licensing of 'practicWindow2.ui' applies.
#
# Created: Fri Dec  4 12:15:51 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_practicWin2(object):
    def setupUi(self, practicWin2):
        practicWin2.setObjectName("practicWin2")
        practicWin2.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        practicWin2.setWindowIcon(icon)
        practicWin2.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(practicWin2)
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
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:rgb(255, 139, 124)}")
        self.exit.setObjectName("exit")
        self.back_to_menu = QtWidgets.QPushButton(self.widget)
        self.back_to_menu.setGeometry(QtCore.QRect(20, 570, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.back_to_menu.setFont(font)
        self.back_to_menu.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.back_to_menu.setObjectName("back_to_menu")
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
        self.label_5.setGeometry(QtCore.QRect(510, 90, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 170, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(800, 180, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.bals = QtWidgets.QLabel(self.centralwidget)
        self.bals.setGeometry(QtCore.QRect(810, 230, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.bals.setFont(font)
        self.bals.setObjectName("bals")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(850, 230, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verify = QtWidgets.QPushButton(self.centralwidget)
        self.verify.setGeometry(QtCore.QRect(760, 290, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.verify.setFont(font)
        self.verify.setStyleSheet("QPushButton{\n"
"    background:#FFFFFF;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background:#c2c2ff\n"
"}")
        self.verify.setObjectName("verify")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(790, 230, 16, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setObjectName("result")
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
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 330, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 390, 271, 22))
        self.lineEdit.setStyleSheet("background:#FFFFFF")
        self.lineEdit.setObjectName("lineEdit")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(240, 440, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 500, 314, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.one_2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.one_2.setFont(font)
        self.one_2.setObjectName("one_2")
        self.verticalLayout_5.addWidget(self.one_2)
        self.two_2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.two_2.setFont(font)
        self.two_2.setObjectName("two_2")
        self.verticalLayout_5.addWidget(self.two_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(240, 220, 314, 82))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.one = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.verticalLayout_4.addWidget(self.one)
        self.two = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.verticalLayout_4.addWidget(self.two)
        self.three = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.verticalLayout_4.addWidget(self.three)
        practicWin2.setCentralWidget(self.centralwidget)

        self.retranslateUi(practicWin2)
        QtCore.QMetaObject.connectSlotsByName(practicWin2)

        def check_r():
                balls = 0
                if self.three.isChecked():
                        balls = balls + 1
                if self.two_2.isChecked():
                        balls = balls + 1
                if self.lineEdit.text() == "@staticmethod":
                        balls = balls + 1

                else:
                        balls = balls

                self.result.setText(str(balls))

        self.verify.clicked.connect(check_r)

    def retranslateUi(self, practicWin2):
        practicWin2.setWindowTitle(QtWidgets.QApplication.translate("practicWin2", "Objects and classes", None, -1))
        self.version.setText(QtWidgets.QApplication.translate("practicWin2", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("practicWin2", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("practicWin2", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("practicWin2", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("practicWin2", "#Класи і об\'єкти в Python", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("practicWin2", "Практика", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("practicWin2", "З якого слова починається створення класу?", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("practicWin2", "Ви набрали:", None, -1))
        self.bals.setText(QtWidgets.QApplication.translate("practicWin2", "/ 3", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("practicWin2", "Балів", None, -1))
        self.verify.setText(QtWidgets.QApplication.translate("practicWin2", "Перевірити", None, -1))
        self.next.setText(QtWidgets.QApplication.translate("practicWin2", "Далі", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("practicWin2", "Назад", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("practicWin2", "Впишіть декоратор для створення\n"
"статичного методу:", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("practicWin2", "Для ініціалізації екземпляра класу\n"
"використовується:", None, -1))
        self.one_2.setText(QtWidgets.QApplication.translate("practicWin2", "__new__", None, -1))
        self.two_2.setText(QtWidgets.QApplication.translate("practicWin2", "__init__", None, -1))
        self.one.setText(QtWidgets.QApplication.translate("practicWin2", "method", None, -1))
        self.two.setText(QtWidgets.QApplication.translate("practicWin2", "def", None, -1))
        self.three.setText(QtWidgets.QApplication.translate("practicWin2", "class", None, -1))