
import sys
from os import getcwd
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QTableWidgetItem,QSizePolicy,QPushButton
from PyQt5.QtGui import QIcon,QFont
import json
from datetime import datetime,timedelta
import clipboard
from qt_material import apply_stylesheet
import qtmodern.styles
import qtmodern.windows
import sqlite3

import root,info,find,nariad,nariadApp  # Это наш конвертированный файл дизайна
from Net import Sortirofka,infoN,infoP
from Base import ReadBase,WriteAll_BaseSql,WriteMG_BaseSql
path = getcwd()
with open("conf.json", "r", encoding='utf8') as read_file:
    dataJson = json.load(read_file)

GlobTime = datetime.now()

baseJson = dataJson["promptDATA"]
base = baseJson[0]
TableUp1 = dataJson["TableUp1Json"]#TableUp1 = ["ТФ","ЗАЯВЛЕНО","ВРЕМЯ","ВИД Н","ПОДТВЕРЖДЕННО","ВИД Н","УСТРАНЕНО","ВРЕМЯ","ВИД Н","TIME"]
TableUp2 = dataJson["TableUp2Json"]#TableUp2 = ["Сделано Л.","Сделано К.","Осталось Л.","Осталось К.",">5",">20","Всего"]
povLinKab = dataJson["povLinKabJson"]#povLinKab = ["К1","К2","К3","К4","КН19","ПК","К6"]
povLinKabProcie = dataJson["povLinKabProcieJson"]#povLinKabProcie =["КЛ1","КЛ2","КЛ3","КЛ4","КЛ5","ЭЛЛ","КЛ6","КЛ7","ПА","Х","ВСО","СБ"]
link = dataJson["link_T_S"]#link = 'http://10.15.10.241/cgi-bin/T_S.cgi'
link_n = dataJson["link_NAR"]
link_pd = dataJson["link_P_D"]
link_nd = dataJson["link_N_D"]
kodStancii = dataJson["kodStanciiJson"]#["342"]
kodSity = dataJson["kodSity"]
defSity = dataJson["defSity"]
theme = dataJson["Themes"]
app = QtWidgets.QApplication(sys.argv)

def SortClass():
    ff = Sortirofka(link,kodStancii,povLinKabProcie,povLinKab)
    items = ff.Sort(ff.lines2)
    return items

asorti = SortClass()

class ExampleApp(QtWidgets.QMainWindow, root.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.comboBox.addItems(kodSity[0])
        self.comboBox.setCurrentText(defSity)
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setHorizontalHeaderLabels(TableUp2 )
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)        
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)



        self.pushButton.clicked.connect(self.u_App) #UPDATE
        #self.pushButton_2.clicked.connect(self.App2)#INFO
        self.pushButton_2.clicked.connect(lambda: self.n_App(asorti,kodSity[0][str(self.comboBox.currentText())]))#NARIAD
        self.pushButton_3.clicked.connect(lambda: self.f_App(str(self.comboBox.currentText())))#FIND
        self.comboBox.activated.connect(self.ComboClick)
        #self.TableUpdate(asorti,base,kodSity[0][defSity])
        self.TableUpdateNew(asorti,base,kodSity[0][defSity])

    def TableUpdateNew(self,item,base,city):
        global timeg
        
        sdell = 0
        sdelk = 0
        ostl = 0
        ostk = 0
        b5 = 0
        b20 = 0
        ot4et = []
        items = []
        for g in range(len(item)):
            if(item[g][0][0:2] == city):
                #print(item[g][0][0:2])
                items.append(item[g])
        #print(items)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.setStyleSheet('QTableWidget  {gridline-color: #75797C}')
        if(len(items)>0): 
            
            self.tableWidget.setColumnCount(len(items[0]))
            self.tableWidget.setRowCount(len(items))
            self.tableWidget.setHorizontalHeaderLabels(TableUp1) 
            #self.tableWidget.setColumnCount(len(items[0])+3)
            #self.tableWidget.setRowCount(len(items))
            
            self.tableWidget.horizontalHeader().resizeSection(0, 65)
            self.tableWidget.horizontalHeader().resizeSection(1, 45)
            #self.tableWidget.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
            #self.tableWidget.horizontalHeader().resizeSection(2, 330)
            self.tableWidget.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
            self.tableWidget.horizontalHeader().resizeSection(3, 90)
            self.tableWidget.horizontalHeader().resizeSection(4, 60)
            self.tableWidget.horizontalHeader().resizeSection(5, 50)
            self.tableWidget.horizontalHeader().resizeSection(6, 90)
            self.tableWidget.horizontalHeader().resizeSection(7, 50)
            self.tableWidget.horizontalHeader().resizeSection(8, 90)
            self.tableWidget.horizontalHeader().resizeSection(9, 55)
            self.tableWidget.horizontalHeader().resizeSection(10, 50)
            #self.tableWidget.horizontalHeader().resizeSection(11, 80)
            self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.Stretch)
            # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            # self.tableWidget.horizontalHeader().setSectionResizeMode(11, QtWidgets.QHeaderView.Stretch)
            #self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            #self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        else:
            self.tableWidget.setColumnCount(0)
            self.tableWidget.setRowCount(0) 
        for i in range(len(items)):
            dddd = items[i][1] + items[i][2]
            ddddz = datetime.strptime(dddd, '%d.%m.%y%H:%M')
            k1= ddddz + timedelta(days=5)
            k2= ddddz + timedelta(days=20)
            GlobTime = datetime.now()
            g = GlobTime.replace(microsecond=0) - ddddz.replace(microsecond=0) 
            if(len(items[i]) == 12):
                for k in range(len(items[i])):
                    if(k==0):
                        self.tableWidget.setCellWidget(i, k, self.createButtonLabel("b1"+str(k),items[i][k],items[i][9],"btn1"))
                        if(items[i][10] == "OL"):
                            ostl = ostl +1
                            if(items[i][9]=="yellow"):
                                b5 = b5 + 1
                            elif (items[i][9]=="blue"):
                                b20 = b20 + 1
                        elif(items[i][10] == "OK"):
                            ostk = ostk + 1
                            if(items[i][9]=="yellow"):
                                b5 = b5 + 1
                            elif (items[i][9]=="blue"):
                                b20 = b20 + 1                        
                        elif(items[i][10] == "SL"):
                            sdell = sdell + 1
                        elif(items[i][10] == "SK"):
                            sdelk = sdelk + 1                                                

                    if(k==1):
                        s = self.readSqlBase(items[i][0],1)
                        l = ("< ? >" if s == "" else s)
                        self.tableWidget.setCellWidget(i, k, self.createButtonLabel("b2"+str(k),l,items[i][9],"btn2",items[i][0]))
                        continue
                    if(k==2):
                        self.tableWidget.setItem(i, k, QTableWidgetItem(self.readSqlBase(items[i][0],4)[:45]))
                        continue
                        
                    if(k!=11):
                        self.item = QtWidgets.QTableWidgetItem(str(items[i][k-2]))
                        self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        self.tableWidget.setItem(i, k, self.item)
                        if((k==5 or k==7 or k==10)and items[i][k-2] != " "):  
                            self.tableWidget.item(i, k).setToolTip(base[items[i][k-2]])
                        continue    
                    if(k == 11):
                        self.tableWidget.setItem(i, k, QTableWidgetItem(str(g)))
            else:
                self.tableWidget.setCellWidget(i, 0, self.createButtonLabel("b1"+str(k),items[i][0],items[i][9],"btn1"))
                self.tableWidget.setItem(i, 2, QTableWidgetItem("Ошибочный код неисправности !"))
                pass
        ot4et = [sdell,sdelk,ostl,ostk,b5,b20]
        for i in range(1):
            for k in range(6):
                self.item = QtWidgets.QTableWidgetItem( str(ot4et[k]))
                self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.tableWidget_2.setItem(i, k, self.item)

    def GetNT(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text())
        clipboard.copy(sender.text())    
    def u_App(self):#UPDATE
        global asorti
        asorti = SortClass()
        self.label.setText(self.upTime())
        text = str(self.comboBox.currentText())
        self.TableUpdateNew(asorti,base,kodSity[0][text])
    def upTime(self):
        time=QtCore.QDateTime.currentDateTime()
        timeDisplay=time.toString('hh:mm:ss')
        timeg = ("Last Update:"+ timeDisplay)
        return timeg
    def ComboClick(self):
        text = str(self.comboBox.currentText())
        self.TableUpdateNew(asorti,base,kodSity[0][text])

    def onChangedTheme(self, text):
        pass
        #apply_stylesheet(app, theme=text, invert_secondary=False,extra=extra)      

    def readSqlBase(self,nomer,info):
        db = "base\\" +nomer[0:3] + ".db"
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute("select * from AbonInfo where nomer=:c",{"c":nomer}) 
        search = cursor.fetchall()
        conn.close()
        return search[0][info]
    def createButtonLabel(self, labelname,txt,color,btn,nomer = 0):
            labelname = QPushButton(self)
            labelname.setText(txt)
            labelname.setFont(QFont('Microsoft YaHei', 10))
            labelname.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
            if(btn == "btn1"):
                labelname.clicked.connect(self.GetNT)
                if(color == "orange"):
                    pass
                if(color == "red"):
                    labelname.setStyleSheet('QPushButton{background-color: #8B0000; color: #F9FBF9;}') # красный
                if(color == "blue"):

                
                    labelname.setStyleSheet('QPushButton{background-color: #0083D0; color: black;}') #синий
                if(color == "green"):
                    labelname.setStyleSheet('QPushButton{background-color: #0F5209; color: #F9FBF9;}') #зеленый
                if(color == "grey"):
                    labelname.setStyleSheet('QPushButton{background-color: #353535; color: #353535;}') #серый
                if(color == "yellow"):
                    labelname.setStyleSheet('QPushButton{background-color: #FFB400; color: black;}') #желтый  
            else:
                labelname.clicked.connect(lambda:self.App2(color,nomer))
            return labelname 
    def App2(self,color,nomer = 0):#INFO
        x = []
        y = []
        tempData=[]
        tempDataS=[]
        self.window2 = infoApp()  # Создаём объект класса ExampleApp
        #text = str(self.comboBox.currentText())
        data = ReadBase(nomer)
        if(color == "orange" or color == "yellow" or color == "blue"):
            dataN = infoP(nomer,link_n,link_pd)      
            for i in range(len(dataN)):
                if(dataN[i][0:7]==nomer):
                    x.append(i)
                if(dataN[i][1:5]=="----"):
                    y.append(i)  
            for iz in range(len(x)):
                col = y[iz]-x[iz]
                for ss in range(col+1):
                    if(dataN[x[iz]+ss][0:5] != "-    "):
                        tempData.append(dataN[x[iz]+ss].split())
                        tempDataS.append(tempData.copy())
                        tempData.clear()          
            self.window2.lineEdit.setText(nomer)
            self.window2.lineEdit_2.setText(data[0][2])
            self.window2.lineEdit_3.setText(" ".join(tempDataS[0][0])[7:])
            self.window2.lineEdit_4.setText(" ".join(tempDataS[1][0]))
            self.window2.lineEdit_5.setText(" ".join(tempDataS[2][0]))
            self.window2.lineEdit_6.setText(" ".join(tempDataS[3][0]))
            self.window2.lineEdit_7.setText(data[0][1])
            self.window2.lineEdit_8.setText(data[0][6])
        if(color == "red"):
            dataN = infoN(nomer,link_n,link_nd)        
            for i in range(len(dataN)):

                if(dataN[i][0:7]==nomer):
                    x.append(i)
                if(dataN[i][1:5]=="----"):
                    y.append(i)  
            for iz in range(len(x)):
                col = y[iz]-x[iz]
                for ss in range(col+1):
                    if(dataN[x[iz]+ss][0:5] != "-    "):
                        tempData.append(dataN[x[iz]+ss].split())
                        tempDataS.append(tempData.copy())
                        tempData.clear()
            self.window2.lineEdit.setText(nomer)
            self.window2.lineEdit_3.setText(" ".join(tempDataS[0][0])[7:])
            self.window2.lineEdit_2.setText(data[0][2])
            self.window2.lineEdit_4.setText(" ".join(tempDataS[1][0]))
            self.window2.lineEdit_5.setText(" ".join(tempDataS[2][0]))
            self.window2.lineEdit_6.setText(" ".join(tempDataS[3][0]))
            self.window2.lineEdit_7.setText(data[0][1])
            self.window2.lineEdit_8.setText(data[0][6])

        self.window2.show()  # Показываем окно
        if(color == "green"):
            self.window2.lineEdit.setText(nomer)
            self.window2.lineEdit_2.setText(data[0][2])
            self.window2.lineEdit_3.setText(data[0][3])
            self.window2.lineEdit_4.setText(data[0][4])
            self.window2.lineEdit_5.setText(data[0][5])
            self.window2.lineEdit_7.setText(data[0][1])
            self.window2.lineEdit_8.setText(data[0][6])
            pass
    def n_App(self,item,sity):
        masiv = []
        adsl = []
        for g in range(len(item)):
            if(item[g][0][0:2] == sity and  item[g][9] != "red" and  item[g][9] != "green" and  item[g][9] != "grey" ):
                masiv.append(item[g][0])
                if(item[g][0][0:2] == sity and item[g][3]=="ОТИ" and item[g][8] == " "):
                    adsl.append(item[g][0])   
        self.window3 = nariadApp.nariadApp(masiv,adsl,link_n,link_pd)  # Создаём объект класса ExampleApp
        #apply_stylesheet(app, theme='dark_teal.xml')
        #self.window2.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window3.show()  # Показываем окно    
    def f_App(self,sity):
        self.window4 = findApp(sity)  # Создаём объект класса ExampleApp
        #apply_stylesheet(app, theme='dark_teal.xml')
        #self.window2.setWindowModality(QtCore.Qt.ApplicationModal)
        self.window4.show()  # Показываем окно           
class infoApp(QtWidgets.QDialog, info.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.Save_ALL)
        self.pushButton.clicked.connect(self.Save_MG)
    def Save_ALL(self):
        n = self.lineEdit.text() #номе
        t = self.lineEdit_2.text() #tip
        ab = self.lineEdit_3.text() #абон
        ad = self.lineEdit_4.text() #adres
        m = self.lineEdit_5.text() #mob
        mg = self.lineEdit_7.text() #mg
        mg1 = ("" if mg == "-" else mg)
        p = self.lineEdit_8.text() #prim
        WriteAll_BaseSql(n,mg1,t,ab,ad,m,p)
    def Save_MG(self):
        n = self.lineEdit.text() #номе
        #m = self.lineEdit_5.text() #mob
        mg = self.lineEdit_7.text() #mg
        mg1 = ("" if mg == "-" else mg)       
        WriteMG_BaseSql(n,mg1)            
class findApp(QtWidgets.QDialog, find.Ui_Dialog):
    def __init__(self,sity):
        super().__init__()
        self.setupUi(self)
        self.comboBox.addItems(kodSity[0])
        self.comboBox.setCurrentText(sity)
        self.pushButton.clicked.connect(self.Clk)
        self.pushButton_2.clicked.connect(self.Save_ALL_Find)  
    def Save_ALL_Find(self):

        
        n = self.lineEdit.text() #номе
        nn = kodSity[0][self.comboBox.currentText()] + n
        t = self.lineEdit_2.text() #tip
        ab = self.lineEdit_3.text() #абон
        ad = self.lineEdit_4.text() #adres
        m = self.lineEdit_5.text() #mob
        mg = self.lineEdit_6.text() #mg
        mg1 = ("" if mg == "-" else mg)
        p = self.lineEdit_7.text() #prim
        WriteAll_BaseSql(nn,mg1,t,ab,ad,m,p)          
    def Clk(self):
        text = str(self.comboBox.currentText())
        
        indata = self.lineEdit.text()
        
        data = ReadBase(kodSity[0][text] + indata)
        if(len(kodSity[0][text] + indata) == 7):
            self.lineEdit_2.setText(data[0][2])
            self.lineEdit_3.setText(data[0][3])
            self.lineEdit_4.setText(data[0][4])
            self.lineEdit_5.setText(data[0][5])
            self.lineEdit_6.setText(data[0][1])
            self.lineEdit_7.setText(data[0][6])
        else:
            self.lineEdit_2.setText("Нет такого!")
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
def main():
    timer = QtCore.QTimer()
    timer.setInterval(600000)
    timer.timeout.connect(lambda: window.u_App())
    timer.start() 
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.label.setText(window.upTime())
    #apply_stylesheet(app, theme='default', invert_secondary=False,extra=extra)
    qtmodern.styles.dark(app)
    
    #mw = qtmodern.windows.ModernWindow(window)
    #mw.show()  # Показываем окно
    window.show()
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
