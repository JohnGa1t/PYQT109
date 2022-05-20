
import sys
from os import getcwd
from PyQt5 import QtWidgets, uic, QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QSizePolicy,QPushButton
from PyQt5.QtGui import QIcon
from qt_material import apply_stylesheet
import sqlite3

import u2,u3  # Это наш конвертированный файл дизайна
from untitled import Ui_Form
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

app = QtWidgets.QApplication(sys.argv)

# with open('style.qss', 'r') as f:
#     style = f.read()

#     # Set the stylesheet of the application
#     app.setStyleSheet(style)

class ExampleApp(QtWidgets.QMainWindow, u2.Ui_MainWindow):
    def __init__(self):
        g =0
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.add_menu_theme(self.main, self.main.menuStyles)
       # self.btnBrowse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки
        #self.pushButton.clicked.connect(self.Clk)
        items = [['3420325', '11.11.21', '10:10', ' ', ' ', ' ', ' ', ' ', ' '],['3420005', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3454187', '2.11.21', '10:45', 'ОТИ', '2.11.21', 'О', '16.11.21', '10:51', 'КЛ3'], ['3452256', '16.11.21', '9:06', 'ОТИ', ' ', ' ', '16.11.21', '10:31', 'ЛН19'],
                ['3456187', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3479325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3458187', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3478325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3459187', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3477325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3450187', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3476325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453127', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3475325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453137', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3474325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
                ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' ']]
        
        self.tableWidget.setColumnCount(len(items[0])+3)
        self.tableWidget.setRowCount(len(items))
        self.tableWidget.setHorizontalHeaderLabels( ["ТФ","МГ","АРЕСС","ЗАЯ-НО","ВРЕМЯ","ВИД Н","ПОДТ-НО","ВИД Н","УСТР-НО","ВРЕМЯ","ВИД Н","DOWNTIME"])
        
        for i in range(len(items)):

            for k in range(len(items[0])+2):
                if(k==0):
                    
                    self.tableWidget.setCellWidget(i, k, self.createButtonLabel("d"+str(k),items[i][k]))
                if(k==1):
                    
                    self.tableWidget.setCellWidget(i, k, self.createButtonLabel("d"+str(k),items[i][k]))
                if(k==2):
                    self.tableWidget.setItem(i, k, QTableWidgetItem(self.readSqlBase(items[i][0][2:],4) ))
                       
                if(k!=1 and k!=2):
                    self.tableWidget.setItem(i, k, QTableWidgetItem(items[i][k-2]))

        #self.tableWidget.horizontalHeaderItem(8).setTextAlignment(Qt.AlignRight)
        #self.tableWidget.horizontalHeaderItem(0).setToolTip("Column 1 ")

        
        
        
        self.tableWidget.horizontalHeader().resizeSection(0, 80)
        self.tableWidget.horizontalHeader().resizeSection(1, 80)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().resizeSection(3, 80)
        self.tableWidget.horizontalHeader().resizeSection(4, 80)
        self.tableWidget.horizontalHeader().resizeSection(5, 80)
        self.tableWidget.horizontalHeader().resizeSection(6, 80)
        self.tableWidget.horizontalHeader().resizeSection(7, 80)
        self.tableWidget.horizontalHeader().resizeSection(8, 80)
        self.tableWidget.horizontalHeader().resizeSection(9, 80)
        self.tableWidget.horizontalHeader().resizeSection(10, 80)
        self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # model = QtGui.QStandardItemModel()
        # for row_number, row_data in enumerate(items):
        #     tableitem = []
        #     model.insertRow(row_number)
        #     for value in row_data:
        #         item = QtGui.QStandardItem(str(value))
        #         tableitem.append(item)
        #     model.insertRow(row_number, tableitem)

        #self.tableWidget.setModel(model)
        
        
        
        # self.tableWidget.setColumnCount(14)
        # self.tableWidget.setRowCount(14)

        # # self.tableWidget.setItem(0, 0, QTableWidgetItem("Text in column 1"))
        # # self.tableWidget.setItem(0, 1, QTableWidgetItem("Text in column 2"))
        # # self.tableWidget.setItem(0, 2, QTableWidgetItem("Text in column 3"))

        # btn = QPushButton()
        # btn.setText('12/1/12')
        # # setattr(self, "label_{}".format(2), btn)


        # # obj_label = getattr(self, "label_{}".format(2))               # !!!
        # # obj_edit = getattr(self, "lineEdit_{}".format(2))             # !!!
        # # obj_label.setText(f'{_[0]}: {obj_edit.text()}')
        # btn.setAccessibleName("push button")
        # self.tableWidget.setCellWidget(0, 2, btn)
        # self.tableWidget.setCellWidget(0, 3, self.createButtonLabel("d0","1"))
        # self.tableWidget.setCellWidget(1, 4, self.createButtonLabel("d1","2"))
        # self.tableWidget.setItem(2, 0, QTableWidgetItem("Text in cowwwwwwwwwwwwwwwlumn 3"))
        self.pushButton.clicked.connect(self.Clk)


        # self.tableWidget.setCellWidget(0, 4, QPushButton("Center"))
        # print(g)
        # # делаем ресайз колонок по содержимому
        
        #self.tableWidget.resizeColumnsToContents()
 
        #grid_layout.addWidget(self.tableWidget, 0, 0)   # Добавляем таблицу в сетку

        #self.tableWidget.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        #self.setCentralWidget(QtWidgets.QTableWidget)
        # central_widget = QWidget(self)                  # Створюємо центральний віджет
        # self.setCentralWidget(central_widget)           # Встановлюємо центральний віджет
    def GetNT(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text())
        # rowPosition = self.tableWidget.rowCount()
        # self.tableWidget.insertRow(rowPosition)   
    def Clk(self):
        self.pushButton.setProperty('class', 'danger')
        self.openWindow()
        #self.apply_stylesheet(self.main, 'dark_teal.xml')
        print("OK")
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
    def readSqlBase(self,nomer,info):
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        cursor.execute("select * from AbonInfo where nomer=:c",{"c":nomer}) 
        search = cursor.fetchall()
        conn.close()
        return search[0][info]
    def createButtonLabel(self, labelname,txt):
            labelname = QPushButton(self)
            #print(txt)
            labelname.setText(txt)
            labelname.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Fixed)
            labelname.clicked.connect(self.GetNT)
            #labelname.resize(300, 40)
            #labelname.move(50, self.Yposition)
            #labelname.clicked.connect(self.printbutton)
            return labelname
    def openWindow(self):
        self.window1 = QtWidgets.QMainWindow()
        self.untitled = u3.Ui_dialog()
        self.untitled.setupUi(self.window1)
        self.window1.show()
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 303)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadData)

        # self.tableView = QtWidgets.QTableView(Dialog)
        # self.tableView.setGeometry(QtCore.QRect(10, 10, 521, 251))
        # self.tableView.setSortingEnabled(True)
        # self.tableView.setObjectName("tableView")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(340, 270, 191, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Загрузить"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Поиск по имени или ID"))

    def loadData(self):
        headers = ["Имя", "Очки", "Дата регистрации", "ID"]
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(headers)

        items = [
            ('Oleg', 22.98, 1587900157, 188530139),
            ('Max', 223.05, 1587900543, 17578),
            ('Vladimir324235576576294592', -99.12, 1587900003, 1),
            ('Anton', -11.32, 1587900322, 5675677),
            ('Глеб', 17.21, 1587900932, 2277786),
            ('Nataliya', 989.16, 1587900113, 7887678),
            ('Виталий', -233.04, 1587900199, 124214)
        ]


        for row_number, row_data in enumerate(items):
            tableitem = []
            model.insertRow(row_number)
            for value in row_data:
                item = QtGui.QStandardItem(str(value))
                tableitem.append(item)
            model.insertRow(row_number, tableitem)

        self.tableView.setModel(model)



def main():

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    apply_stylesheet(app, theme='dark_amber.xml', extra=extra)
    
    #window.adjustSize()
    # window.setStyleSheet(open("coffe.qss", "r").read())
    # window.setAutoFillBackground(True)
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
# window = uic.loadUi("untitled.ui")

# #window.lineEdit.setText("dd")
# window.setWindowIcon(QIcon('phone1.png'))
# window.setFixedSize(920,720)

# #window.tableView.show()
# apply_stylesheet(app, theme='dark_amber.xml')

# window.show()
# sys.exit(app.exec_())