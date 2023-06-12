import sys
from PySide2 import QtCore, QtGui, QtWidgets
from mainWindow import Ui_Menu
from secondWindow1 import Ui_Menu_oop1
from secondWindow2 import Ui_Menu_oop2
from bonusWindow import Ui_Menu_bonus
from about_pr import Ui_About_pr
from secondWindow_class1 import Ui_class_1
from secondWindow_class2 import Ui_class_2
from secondWindow_class3 import Ui_class_3
from secondWindow_class4 import Ui_class_4
from secondWindow_class5 import Ui_class_5
from secondWindow_class6 import Ui_class_6
from secondWindow_class7 import Ui_class_7
from practicWindow1 import Ui_practicWin1
from practicWindow2 import Ui_practicWin2
from practicWindow3 import Ui_practicWin3
import webbrowser
import os

app = QtWidgets.QApplication(sys.argv)
Menu = QtWidgets.QMainWindow()
ui = Ui_Menu()
ui.setupUi(Menu)
Menu.show()


def open_Oop():
    global Menu_oop1
    Menu_oop1 = QtWidgets.QMainWindow()
    ui = Ui_Menu_oop1()
    ui.setupUi(Menu_oop1)
    Menu.close()
    Menu_oop1.show()

    def returnToMain():
        Menu_oop1.close()
        Menu.show()

    ui.back_to_menu.clicked.connect(returnToMain)

    def exit_app():
        app.quit()

    ui.exit.clicked.connect(exit_app)
    ui.wikipedia.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/%D0%9E%D0%B1%27%D1%94%D0%BA%D1%82%D0%BD%D0%BE-%D0%BE%D1%80%D1%96%D1%94%D0%BD%D1%82%D0%BE%D0%B2%D0%B0%D0%BD%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F'))


    def open_Oop2():
        global Menu_oop2
        Menu_oop2 = QtWidgets.QMainWindow()
        ui = Ui_Menu_oop2()
        ui.setupUi(Menu_oop2)
        Menu.close()
        Menu_oop1.close()
        Menu_oop2.show()

        def returnTooop1():
            Menu_oop2.close()
            Menu_oop1.show()

        ui.back.clicked.connect(returnTooop1)

        def exit_app():
            app.quit()

        ui.exit.clicked.connect(exit_app)
        ui.wikipedia.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/%D0%9E%D0%B1%27%D1%94%D0%BA%D1%82%D0%BD%D0%BE-%D0%BE%D1%80%D1%96%D1%94%D0%BD%D1%82%D0%BE%D0%B2%D0%B0%D0%BD%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F'))

        def returnToMain():
            Menu_oop2.close()
            Menu.show()

            ui.exit.clicked.connect(exit_app)
        ui.back_to_menu.clicked.connect(returnToMain)

    ui.next.clicked.connect(open_Oop2)


def exit_app():
    app.quit()


def bonus():
    global Menu_bonus
    Menu_bonus = QtWidgets.QMainWindow()
    ui = Ui_Menu_bonus()
    ui.setupUi(Menu_bonus)
    Menu_bonus.show()
    Menu.close()

    def ReturToMain():
        Menu_bonus.close()
        Menu.show()

    ui.back_to_menu.clicked.connect(ReturToMain)

    def exit_app():
        app.quit()


    os.startfile("tetris.exe")

    ui.exit.clicked.connect(exit_app)
    ui.wikipedia.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/%D0%A2%D0%B5%D1%82%D1%80%D1%96%D1%81'))

def about_pr():
    global About_pr
    About_pr = QtWidgets.QMainWindow()
    ui = Ui_About_pr()
    ui.setupUi(About_pr)
    Menu.close()
    About_pr.show()

    def ReturToMain():
        About_pr.close()
        Menu.show()

    ui.back_to_menu.clicked.connect(ReturToMain)


    def exit_app():
        app.quit()

    ui.exit.clicked.connect(exit_app)

def class1():
    global class_1
    class_1 = QtWidgets.QMainWindow()
    ui = Ui_class_1()
    ui.setupUi(class_1)
    Menu.close()
    class_1.show()

    def exit_app():
        app.quit()

    ui.exit.clicked.connect(exit_app)

    def ReturToMain():
        class_1.close()
        Menu.show()

    ui.back_to_menu.clicked.connect(ReturToMain)
    ui.wikipedia_class.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/Python'))

    def class2():
        global class_2
        class_2 = QtWidgets.QMainWindow()
        ui = Ui_class_2()
        ui.setupUi(class_2)
        class_1.close()
        class_2.show()

        def exit_app():
            app.quit()

        ui.exit.clicked.connect(exit_app)

        def ReturToMain():
            class_1.close()
            Menu.show()

        def returnToclass1():
            class_2.close()
            class_1.show()

        ui.back.clicked.connect(returnToclass1)

        ui.back_to_menu.clicked.connect(ReturToMain)
        ui.wikipedia_class.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/Python'))

        def class3():
            global class_3
            class_3 = QtWidgets.QMainWindow()
            ui = Ui_class_3()
            ui.setupUi(class_3)
            class_3.show()
            class_2.close()

            def ReturToMain():
                class_3.close()
                Menu.show()

            ui.back_to_menu.clicked.connect(ReturToMain)

            def returnToclass2():
                class_3.close()
                class_2.show()

            ui.back.clicked.connect(returnToclass2)

            def exit_app():
                app.quit()

            ui.exit.clicked.connect(exit_app)
            ui.wikipedia.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/Python'))

            def class4():
                global class_4
                class_4 = QtWidgets.QMainWindow()
                ui = Ui_class_4()
                ui.setupUi(class_4)
                class_4.show()
                class_3.close()

                def ReturToMain():
                    class_4.close()
                    Menu.show()

                ui.back_to_menu.clicked.connect(ReturToMain)

                def returnToclass3():
                    class_4.close()
                    class_3.show()

                ui.back.clicked.connect(returnToclass3)

                def exit_app():
                    app.quit()

                ui.exit.clicked.connect(exit_app)
                ui.wikipedia.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/Python'))

                def class5():
                    global class_5
                    class_5 = QtWidgets.QMainWindow()
                    ui = Ui_class_5()
                    ui.setupUi(class_5)
                    class_5.show()
                    class_4.close()

                    def ReturToMain():
                        class_5.close()
                        Menu.show()

                    ui.back_to_menu.clicked.connect(ReturToMain)

                    def returnToclass4():
                        class_5.close()
                        class_4.show()

                    ui.back.clicked.connect(returnToclass4)

                    def exit_app():
                        app.quit()

                    ui.exit.clicked.connect(exit_app)
                    ui.wikipedia.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/Python'))

                    def class6():
                        global class_6
                        class_6 = QtWidgets.QMainWindow()
                        ui = Ui_class_6()
                        ui.setupUi(class_6)
                        class_6.show()
                        class_5.close()

                        def ReturToMain():
                            class_6.close()
                            Menu.show()

                        ui.back_to_menu.clicked.connect(ReturToMain)

                        def returnToclass5():
                            class_6.close()
                            class_5.show()

                        ui.back.clicked.connect(returnToclass5)

                        def exit_app():
                            app.quit()

                        ui.exit.clicked.connect(exit_app)
                        ui.wikipedia.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/Python'))

                        def class7():
                            global class_7
                            class_7 = QtWidgets.QMainWindow()
                            ui = Ui_class_7()
                            ui.setupUi(class_7)
                            class_7.show()
                            class_6.close()

                            def ReturToMain():
                                class_7.close()
                                Menu.show()

                            ui.back_to_menu.clicked.connect(ReturToMain)

                            def returnToclass6():
                                class_7.close()
                                class_6.show()

                            ui.back_2.clicked.connect(returnToclass6)

                            def exit_app():
                                app.quit()

                            ui.exit.clicked.connect(exit_app)
                            ui.wikipedia.clicked.connect(lambda: webbrowser.open('https://uk.wikipedia.org/wiki/Python'))

                        ui.next.clicked.connect(class7)
                    ui.next.clicked.connect(class6)
                ui.next.clicked.connect(class5)
            ui.next.clicked.connect(class4)
        ui.next.clicked.connect(class3)

    ui.next.clicked.connect(class2)

def practic():
    global practicWin1
    practicWin1 = QtWidgets.QMainWindow()
    ui = Ui_practicWin1()
    ui.setupUi(practicWin1)
    practicWin1.show()
    Menu.close()

    def ReturToMain():
        practicWin1.close()
        Menu.show()

    ui.back_to_menu.clicked.connect(ReturToMain)

    def exit_app():
        app.quit()

    ui.exit.clicked.connect(exit_app)

    def practic2():
        global practicWin2
        practicWin2 = QtWidgets.QMainWindow()
        ui = Ui_practicWin2()
        ui.setupUi(practicWin2)
        practicWin2.show()
        practicWin1.close()

        def ReturToMain():
            practicWin2.close()
            Menu.show()

        ui.back_to_menu.clicked.connect(ReturToMain)

        def returnToPractic1():
            practicWin2.close()
            practicWin1.show()

        ui.back.clicked.connect(returnToPractic1)

        def exit_app():
            app.quit()

        ui.exit.clicked.connect(exit_app)

        def practic3():
            global practicWin3
            practicWin3 = QtWidgets.QMainWindow()
            ui = Ui_practicWin3()
            ui.setupUi(practicWin3)
            practicWin3.show()
            practicWin2.close()

            def ReturToMain():
                practicWin3.close()
                Menu.show()

            ui.back_to_menu.clicked.connect(ReturToMain)

            def returnToPractic2():
                practicWin3.close()
                Menu.show()

            ui.back.clicked.connect(returnToPractic2)

            def exit_app():
                app.quit()

            ui.exit.clicked.connect(exit_app)

        ui.next.clicked.connect(practic3)
    ui.next.clicked.connect(practic2)

ui.practic.clicked.connect(practic)
ui.main_classes.clicked.connect(class1)
ui.about_pr.clicked.connect(about_pr)
ui.bonus.clicked.connect(bonus)
ui.exit.clicked.connect(exit_app)
ui.main_oop.clicked.connect(open_Oop)
sys.exit(app.exec_())