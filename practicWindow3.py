# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practicWindow3.ui',
# licensing of 'practicWindow3.ui' applies.
#
# Created: Fri Dec  4 17:28:20 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_practicWin3(object):
    def setupUi(self, practicWin3):
        practicWin3.setObjectName("practicWin3")
        practicWin3.setFixedSize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        practicWin3.setWindowIcon(icon)
        practicWin3.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(practicWin3)
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
        self.label_8.setGeometry(QtCore.QRect(240, 440, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 480, 314, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.one = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.verticalLayout_4.addWidget(self.one)
        self.two = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.verticalLayout_4.addWidget(self.two)
        self.three = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.verticalLayout_4.addWidget(self.three)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(240, 220, 451, 211))
        self.widget_2.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_2.setObjectName("widget_2")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(390, 80, 451, 121))
        self.widget_3.setStyleSheet("border-radius: 10px;\n"
"background: #FFFFFF")
        self.widget_3.setObjectName("widget_3")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(20, 150, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        practicWin3.setCentralWidget(self.centralwidget)

        self.retranslateUi(practicWin3)
        QtCore.QMetaObject.connectSlotsByName(practicWin3)

    def retranslateUi(self, practicWin3):
        practicWin3.setWindowTitle(QtWidgets.QApplication.translate("practicWin3", "Objects and classes", None, -1))
        self.version.setText(QtWidgets.QApplication.translate("practicWin3", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("practicWin3", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("practicWin3", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("practicWin3", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("practicWin3", "#Класи і об\'єкти в Python", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("practicWin3", "Практика", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("practicWin3", "Проаналізуйте код:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("practicWin3", "Ви набрали:", None, -1))
        self.bals.setText(QtWidgets.QApplication.translate("practicWin3", "/ 1", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("practicWin3", "Балів", None, -1))
        self.verify.setText(QtWidgets.QApplication.translate("practicWin3", "Перевірити", None, -1))
        self.back.setText(QtWidgets.QApplication.translate("practicWin3", "Завершити", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("practicWin3", "Що відбудеться при виклику Rectangle.width?", None, -1))
        self.one.setText(QtWidgets.QApplication.translate("practicWin3", "Помилка", None, -1))
        self.two.setText(QtWidgets.QApplication.translate("practicWin3", "Виведе 10", None, -1))
        self.three.setText(QtWidgets.QApplication.translate("practicWin3", "Виведе 20", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("practicWin3", "class Rectangle:\n"
"    default_color = \"green\"\n"
"\n"
"    def __init__(self, width, height):\n"
"        self.width = width\n"
"        self.height = height", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("practicWin3", ">>> rect = Rectangle(10, 20)\n"
">>> Rectangle.width", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    practicWin3 = QtWidgets.QMainWindow()
    ui = Ui_practicWin3()
    ui.setupUi(practicWin3)
    practicWin3.show()
    sys.exit(app.exec_())

