import sys
from os import getcwd
from PyQt5 import QtWidgets, uic, QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QSizePolicy,QPushButton
from PyQt5.QtGui import QIcon,QFont
import json
from datetime import datetime
import webbrowser
import sqlite3
from qt_material import apply_stylesheet
from Net import infoToNariad
import qtmodern.styles
import qtmodern.windows

import nariad

masiv = ["3422805","3451116","3452752","3450000","3470000","3460000"]

class nariadApp(QtWidgets.QDialog, nariad.Ui_Dialog):
    def __init__(self,masiv,adsL,link_n,link_pd):
        super().__init__()
        self.setupUi(self) 
        g =0
        self.adsl = adsL
        self.ln = link_n
        self.pd = link_pd
        self.x = []
        self.y = []
        self.tempDataG = []
        d = []
        temp= []
        for m in range(len(masiv)): #ColumCount
            d.append(masiv[m][:3])
            if(temp.count(masiv[m][:3])==0):
                temp.append(masiv[m][:3])
        for k in range(len(temp)): #RowCount
            if(d.count(temp[k]) > g):
                g = d.count(temp[k])     
        self.pushButton.clicked.connect(self.nariadLoadData)
        self.tableWidget.setColumnCount(len(temp))
        self.tableWidget.setRowCount(g)
        self.tableWidget.setHorizontalHeaderLabels(temp) 
        self.tableWidget.setStyleSheet('QAbstractItemView::indicator {width: 20px; height: 20px;}')
        self.checKAdd(temp)
        for j in range(g):
            for l in range (len(temp)):
                
                for r in range(len(masiv)):
                    if(temp[l] == masiv[r][:3] ) :               
                        self.item = QtWidgets.QTableWidgetItem(str(masiv[r]))
                        self.item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                        self.item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                        masiv.pop(r)
                        self.tableWidget.setItem(j,l,self.item)
                        break

    def checKAdd(self,data):
        for d in range(len(data)):
            labelname = QPushButton(self.horizontalLayoutWidget)
            self.formLayout.setWidget(d+1,QtWidgets.QFormLayout.LabelRole, labelname)
            labelname.setText(data[d])
            labelname.setFont(QFont('Microsoft YaHei', 8))
            labelname.setFocusPolicy(QtCore.Qt.NoFocus)
            labelname.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
            
            labelname.clicked.connect(self.Check_Answer)
    def retriveCheck(self):
        data = []
        for row in range(self.tableWidget.columnCount()):
            for col in range(self.tableWidget.rowCount()):
                try:
                    if self.tableWidget.item(col,row).checkState() == QtCore.Qt.CheckState.Checked:
                        data.append(self.tableWidget.item(col,row).text())
                except AttributeError:
                    pass
        return data               

    def Check_Answer(self):
        for row in range(self.tableWidget.columnCount()):
            for col in range(self.tableWidget.rowCount()):
                try:
                        if(self.sender().text() == self.tableWidget.item(col,row).text()[:3]):
                            #pass
                            if self.tableWidget.item(col,row).checkState() == QtCore.Qt.CheckState.Checked:
                                self.tableWidget.item(col,row).setCheckState(QtCore.Qt.CheckState.Unchecked)
                            else:
                                self.tableWidget.item(col,row).setCheckState(QtCore.Qt.CheckState.Checked)
                except AttributeError:
                    pass
    def getKodAts(self):
        codAts=[]
        data = self.retriveCheck()
        for d in range(len(data)):
            if(codAts.count(data[d][:3])==0):
                codAts.append(data[d][:3])
        return codAts,data
    def nariadLoadData(self):
        t = nameTime()
        gKA,nomera = self.getKodAts()
        for g in range(len(gKA)):
            data = infoToNariad(gKA[g]+"0000",gKA[g]+"9999",self.ln,self.pd)
            self.SearchXY(data,nomera)
            nariadWrite(self.tempDataG,t,nomera,self.adsl)
            self.x.clear()
            self.y.clear()
            self.tempDataG.clear()
        webbrowser.open(t)    
    def SearchXY(self,data,spisokN):
        dataNsort = data
        a = 0
        for i in range(len(dataNsort)):     
            if(spisokN.count(dataNsort[i][0:7]) > 0):
                self.x.append(i)
                a = 1
            if(dataNsort[i][1:5]=="----" and a == 1):
                self.y.append(i)
                a = 0
        for iz in range(len(self.x)):
            tempData=[]
            col = self.y[iz]-self.x[iz]
            for ss in range(col+1):
                if(dataNsort[self.x[iz]+ss][0:2] != "- "):
                    tempData.append(dataNsort[self.x[iz]+ss].split())
                    self.tempDataG.append(tempData.copy())
                    tempData.clear()     
def nariadWrite(tempDataS,name,nomera,adsl):        
    f = open(name,'a+',encoding="UTF-8")
    for aa in range(len(tempDataS)):

        a = ' '.join(tempDataS[aa][0])
        if(nomera.count(a[0:7])):
            txt =  tempDataS[aa][0][0]
            #print(internet.count(txt))
            
            db = "base\\" + txt[0:3] + ".db"
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            cursor.execute("select * from AbonInfo where nomer=:c",{"c":txt}) 
            search = cursor.fetchall()
            conn.close()
            f.write(txt[2:] + (" +ADSL" if adsl.count(txt) else "" ) +"\n")
            #f.write(txt[2:] +"\n")
            f.write(" ".join(tempDataS[aa][0]).replace(tempDataS[aa][0][0],"")[1:] + "\n")

        elif(a.rfind("СВЕРДЛОВСК")!= -1):
            f.write(a.replace("СВЕРДЛОВСК"," ")+ "\n")    
        elif(a[0:4]=="----"):
            
            f.write("Магистраль ("+search[0][1]+")\n") 
            f.write("---------------------------------"+ "\n")
        
        else:
            f.write(a + "\n")
    f.close


def nameTime():
    GlobTime = datetime.now().replace(microsecond=0) 
    name = 'Наряды\\'+ GlobTime.strftime("%d-%b-%Y %H-%M-%S") +".txt"
    return name
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = nariadApp(masiv)  # Создаём объект класса ExampleApp
    window.show()
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()