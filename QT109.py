
import sys
from os import getcwd
from PyQt5 import QtWidgets, uic, QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QSizePolicy,QPushButton
from PyQt5.QtGui import QIcon
from qt_material import apply_stylesheet,QtStyleTools
import sqlite3

import u1,u2  # Это наш конвертированный файл дизайна
#from untitled import Ui_Form
path = getcwd()
db_filename = 'baseF.db'
extra = {

    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',
    'density_scale': '-1',
    # Font
    'font_family': 'Roboto',
}

class ExampleApp(QtWidgets.QMainWindow, u1.Ui_MainWindow,QtStyleTools):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.apply_stylesheet(self, 'dark_teal.xml')

        self.pushButton.clicked.connect(self.Clk)
        self.pushButton_2.clicked.connect(self.gg)
    def Clk(self):
        #self.pushButton.setProperty('class', 'danger')
        #self.openWindow()
        #self.apply_stylesheet(self, 'light_red.xml')
        print("OK")
        #rowPosition = self.tableWidget.rowCount()
        #self.tableWidget.insertRow(rowPosition)

    def gg(self):
        #self.app = QtWidgets.QApplication(sys.argv)
        self.window2 = ExampleApp1()  # Создаём объект класса ExampleApp
        self.window2.show()  # Показываем окно
        #self.app.exec_()
class ExampleApp1(QtWidgets.QMainWindow, u2.Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.apply_stylesheet(self, 'dark_teal.xml')

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()