# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_pr.ui',
# licensing of 'about_pr.ui' applies.
#
# Created: Fri Dec  4 09:33:21 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_About_pr(object):
    def setupUi(self, About_pr):
        About_pr.setObjectName("About_pr")
        About_pr.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        About_pr.setWindowIcon(icon)
        About_pr.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(About_pr)
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 80, 161, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(46, 107, 155)")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(460, 160, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#000000")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 290, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgb(225, 173, 52)")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 370, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#000000")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 640, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#000000")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 460, 191, 161))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("img/kpik.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        About_pr.setCentralWidget(self.centralwidget)

        self.retranslateUi(About_pr)
        QtCore.QMetaObject.connectSlotsByName(About_pr)

    def retranslateUi(self, About_pr):
        About_pr.setWindowTitle(QtWidgets.QApplication.translate("About_pr", "Objects and classes", None, -1))
        self.version.setText(QtWidgets.QApplication.translate("About_pr", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("About_pr", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("About_pr", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("About_pr", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("About_pr", "#Класи і об\'єкти в Python", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("About_pr", "[Розробник]", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("About_pr", "Брендак Андрій", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("About_pr", "[Спеціальна подяка]", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("About_pr", "Кузьмичу Василю Степановичу", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("About_pr", "Спеціально для Кам’янець-Подільського індустріального коледжу", None, -1))