# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bonusWindow.ui',
# licensing of 'bonusWindow.ui' applies.
#
# Created: Fri Dec  4 09:33:50 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Menu_bonus(object):
    def setupUi(self, Menu_bonus):
        Menu_bonus.setObjectName("Menu_bonus")
        Menu_bonus.setFixedSize(1000, 700)
        font = QtGui.QFont()
        font.setPointSize(10)
        Menu_bonus.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Menu_bonus.setWindowIcon(icon)
        Menu_bonus.setStyleSheet("background:#F9F9F9;")
        self.centralwidget = QtWidgets.QWidget(Menu_bonus)
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
        self.label_5.setGeometry(QtCore.QRect(500, 90, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tetris_photo = QtWidgets.QLabel(self.centralwidget)
        self.tetris_photo.setGeometry(QtCore.QRect(680, 150, 301, 251))
        self.tetris_photo.setText("")
        self.tetris_photo.setPixmap(QtGui.QPixmap("img/tetris.png"))
        self.tetris_photo.setScaledContents(True)
        self.tetris_photo.setObjectName("tetris_photo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 160, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 190, 411, 16))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 400, 771, 141))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
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
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 210, 471, 191))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        Menu_bonus.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu_bonus)
        QtCore.QMetaObject.connectSlotsByName(Menu_bonus)

    def retranslateUi(self, Menu_bonus):
        Menu_bonus.setWindowTitle(QtWidgets.QApplication.translate("Menu_bonus", "Objects and classes", None, -1))
        self.version.setText(QtWidgets.QApplication.translate("Menu_bonus", "version 1.0", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Menu_bonus", "Головне меню", None, -1))
        self.exit.setText(QtWidgets.QApplication.translate("Menu_bonus", "Вихід", None, -1))
        self.back_to_menu.setText(QtWidgets.QApplication.translate("Menu_bonus", "На головну\n"
"сторінку", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Menu_bonus", "#Класи і об\'єкти в Python", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Menu_bonus", "Тетріс", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Menu_bonus", "Правила гри", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("Menu_bonus", "__________________________________________________________", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Menu_bonus", "У спеціальному полі гравець бачить фігурку, яка буде слідувати після поточної — ця підказка\n"
"дозволяє планувати свої дії. Темп гри поступово збільшується. Назва гри походить від кількості\n"
"клітин, з яких складається кожна фігура. Гра закінчується, коли нова фігурка не може\n"
"поміститися в стакан. Гравець отримує бали за кожну фігурку, тому його задача — заповнювати\n"
"ряди, не заповнюючи саму склянку якомога довше, щоб таким чином отримати якомога більше\n"
"балів.", None, -1))
        self.wikipedia.setText(QtWidgets.QApplication.translate("Menu_bonus", "Читати на Wikipedia", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("Menu_bonus", "Випадкові фігурки падають зверху в прямокутний\n"
"стакан шириною 10 і висотою 20 клітин.\n"
"У польоті гравець може повертати фігурку та рухати її по\n"
"горизонталі. Також можна «скидати» фігурку, тобто\n"
"прискорювати її падіння, коли вже вирішено, куди фігурка\n"
"повинна впасти. Фігурка летить, поки не наткнеться\n"
"на іншу фігурку або на дно склянки. Якщо при цьому\n"
"заповнився горизонтальний ряд з 10 кліток, він пропадає і\n"
"все, що вище нього, опускається на одну клітку.", None, -1))