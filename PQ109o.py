
import sys
from os import getcwd
from PyQt5 import QtWidgets, uic, QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QSizePolicy,QPushButton
from PyQt5.QtGui import QIcon
from qt_material import apply_stylesheet
import json
#import qtmodern.styles
#import qtmodern.windows

import sqlite3

#from sklearn.cluster import k_means
from Net import Sortirofka
import u1,u2  # Это наш конвертированный файл дизайна

path = getcwd()

extra = {

    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',
    'density_scale': '-2',
    # Font
    'font_family': 'Palatino Linotype',
    'font_size': '9px',
    'line_height': '2px',
}
th = ['dark_amber.xml',
 'dark_blue.xml',
 'dark_cyan.xml',
 'dark_lightgreen.xml',
 'dark_pink.xml',
 'dark_purple.xml',
 'dark_red.xml',
 'dark_teal.xml',
 'dark_yellow.xml',
 'light_amber.xml',
 'light_blue.xml',
 'light_cyan.xml',
 'light_cyan_500.xml',
 'light_lightgreen.xml',
 'light_pink.xml',
 'light_purple.xml',
 'light_red.xml',
 'light_teal.xml',
 'light_yellow.xml']
with open("conf.json", "r", encoding='utf8') as read_file:
    dataJson = json.load(read_file)
app = QtWidgets.QApplication(sys.argv)
db_filename = 'base.db'
baseJson = dataJson["promptDATA"]
base = baseJson[0]
TableUp1 = dataJson["TableUp1Json"]#TableUp1 = ["ТФ","ЗАЯВЛЕНО","ВРЕМЯ","ВИД Н","ПОДТВЕРЖДЕННО","ВИД Н","УСТРАНЕНО","ВРЕМЯ","ВИД Н","TIME"]
TableUp2 = dataJson["TableUp2Json"]#TableUp2 = ["Сделано Л.","Сделано К.","Осталось Л.","Осталось К.",">5",">20","Всего"]
povLinKab = dataJson["povLinKabJson"]#povLinKab = ["К1","К2","К3","К4","КН19","ПК","К6"]
povLinKabProcie = dataJson["povLinKabProcieJson"]#povLinKabProcie =["КЛ1","КЛ2","КЛ3","КЛ4","КЛ5","ЭЛЛ","КЛ6","КЛ7","ПА","Х","ВСО","СБ"]
link = dataJson["link"]#link = 'http://10.15.10.241/cgi-bin/T_S.cgi'
kodStancii = dataJson["kodStanciiJson"]#["342"]
#kodStancii = [3]
def SortClass():

    ff = Sortirofka(link,kodStancii)

    return ff.Sort(ff.lines2)

asorti = SortClass()
print(asorti)

class ExampleApp(QtWidgets.QMainWindow, u1.Ui_MainWindow):
    def __init__(self):
        g =0
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
       # self.btnBrowse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки
        #self.pushButton.clicked.connect(self.Clk)
        # items = [['3420325', '11.11.21', '10:10', ' ', ' ', ' ', ' ', ' ', ' '],['3420005', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
        #         ['3454187', '2.11.21', '10:45', 'ОТИ', '2.11.21', 'О', '16.11.21', '10:51', 'КЛ3'], ['3452256', '16.11.21', '9:06', 'ОТИ', ' ', ' ', '16.11.21', '10:31', 'ЛН19'],
        #         ['3456187', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3479325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
        #         ['3458187', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3478325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
        #         ['3459187', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3477325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
        #         ['3450187', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3476325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
        #         ['3453127', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3475325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
        #         ['3453137', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3474325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' '],
        #         ['3453197', '2.11.21', '10:51', 'ОТИ', '16.11.21', 'КЛ3', ' ', ' ', ' '], ['3473325', '11.11.21', '10:10', 'О', '11.11.21', 'О', ' ', ' ', ' ']]
        items = asorti
       
        #self.combo = QComboBox()
        self.comboBox.addItems(['dark_amber.xml','dark_blue.xml','dark_cyan.xml','dark_lightgreen.xml','dark_pink.xml','dark_purple.xml','dark_red.xml','dark_teal.xml','dark_yellow.xml','light_amber.xml','light_blue.xml','light_cyan.xml','light_cyan_500.xml','light_lightgreen.xml','light_pink.xml','light_purple.xml','light_red.xml','light_teal.xml','light_yellow.xml'])
        self.comboBox.activated[str].connect(self.onChanged)
        self.comboBox_2.addItems(["34","44"])
        self.comboBox_2.activated[str].connect(self.onChangedSity)
        self.tableWidget.setColumnCount(len(items[0])+3)
        self.tableWidget.setRowCount(len(items))
        self.tableWidget.setHorizontalHeaderLabels( ["ТФ","МГ","АДРЕСС","ЗАЯ-НО","ВРЕМЯ","ВИД Н","ПОДТ-НО","ВИД Н","УСТР-НО","ВРЕМЯ","ВИД Н","DOWNTIME"])
        
        for i in range(len(items)):

            for k in range(len(items[0])+2):
                if(k==0):
                    #pass
                    self.tableWidget.setCellWidget(i, k, self.createButtonLabel("d"+str(k),items[i][k]))
                    #self.tableWidget.item(i, k).setBackground(QtGui.QColor(125,125,125))
                # if(k==2):
                #     self.tableWidget.setItem(i, k, QTableWidgetItem(self.readSqlBase(items[i][0][2:],4) ))
                #     self.tableWidget.item(i, k).setBackground(QtGui.QColor(252,252,252))
                       
                if(k!=1 and k!=2):
                    self.tableWidget.setItem(i, k, QTableWidgetItem(items[i][k-2]))
                    #self.tableWidget.item(i, k).setBackground(QtGui.QColor(0,0,0))
                    #self.tableWidget.item(i, k).setToolTip("Column 1 ")
        #self.tableWidget.horizontalHeaderItem(8).setTextAlignment(Qt.AlignRight)
        #self.tableWidget.horizontalHeaderItem(0).setToolTip("Column 1 ")

        
        self.tableWidget.horizontalHeader().resizeSection(0, 90)
        self.tableWidget.horizontalHeader().resizeSection(1, 70)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        #self.tableWidget.horizontalHeader().resizeSection(2, 180)
        self.tableWidget.horizontalHeader().resizeSection(3, 80)
        self.tableWidget.horizontalHeader().resizeSection(4, 80)
        self.tableWidget.horizontalHeader().resizeSection(5, 80)
        self.tableWidget.horizontalHeader().resizeSection(6, 90)
        self.tableWidget.horizontalHeader().resizeSection(7, 80)
        self.tableWidget.horizontalHeader().resizeSection(8, 90)
        self.tableWidget.horizontalHeader().resizeSection(9, 80)
        self.tableWidget.horizontalHeader().resizeSection(10, 80)
        #self.tableWidget.horizontalHeader().resizeSection(11, 80)
        self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.pushButton.clicked.connect(self.Clk)
        self.pushButton_2.clicked.connect(self.Clk2)
    def GetNT(self):
        sender = self.sender()
        sender.setStyleSheet('QPushButton {background-color: red; color: white;}')
        self.statusBar().showMessage(sender.text())
        # rowPosition = self.tableWidget.rowCount()
        # self.tableWidget.insertRow(rowPosition)   
    def Clk(self):
        print("OK")
        self.pushButton.setStyleSheet('QPushButton {background-color: red; color: white;}')
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
    def onChanged(self, text):
        print(text)
        
        apply_stylesheet(app, theme=text, extra=extra)
    def renew(self,items):
        self.tableWidget.setColumnCount(len(items[0])+3)
        self.tableWidget.setRowCount(len(items))
        for i in range(len(items)):

            for k in range(len(items[0])+2):
                if(k==0):
                    #pass
                    self.tableWidget.setCellWidget(i, k, self.createButtonLabel("d"+str(k),items[i][k]))
                    #self.tableWidget.item(i, k).setBackground(QtGui.QColor(125,125,125))
                # if(k==2):
                #     self.tableWidget.setItem(i, k, QTableWidgetItem(self.readSqlBase(items[i][0][2:],4) ))
                #     self.tableWidget.item(i, k).setBackground(QtGui.QColor(252,252,252))
                       
                if(k!=1 and k!=2):
                    self.tableWidget.setItem(i, k, QTableWidgetItem(items[i][k-2]))
                    #self.tableWidget.item(i, k).setBackground(QtGui.QColor(0,0,0))
                    #self.tableWidget.item(i, k).setToolTip("Column 1 ")
    def onChangedSity(self, text):
        data = asorti
        print(text)
        g = []
        for d in range(len(data)):
            if(data[d][0][0:2] == text):
                g.append(data[d])
        self.renew(g)

        
        

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
            #labelname.setStyleSheet('QPushButton {background-color: red; color: white;}')
            labelname.setText(txt)
            labelname.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
            labelname.clicked.connect(self.GetNT)
            #labelname.resize(300, 40)
            #labelname.move(50, self.Yposition)
            #labelname.clicked.connect(self.printbutton)
            return labelname 
    def Clk2(self):
        self.window2 = ExampleApp1()  # Создаём объект класса ExampleApp
        #apply_stylesheet(app, theme='dark_teal.xml')
        
        self.window2.show()  # Показываем окно
class ExampleApp1(QtWidgets.QDialog, u2.Ui_Dialog):
    def __init__(self):
        g =0
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self) 

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    #apply_stylesheet(app, theme='dark_teal.xml', extra=extra)
    #qtmodern.styles.dark(app)
    
    #mw = qtmodern.windows.ModernWindow(window)
    #mw.show()  # Показываем окно
    window.show()
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
