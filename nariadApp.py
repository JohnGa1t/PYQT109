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
    def __init__(self,masiv,link_n,link_pd):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self) 
        #self.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)
        g =0
        self.ln = link_n
        self.pd = link_pd
        self.x = []
        self.y = []
        self.tempDataG = []
        d = []
        temp= []
        for m in range(len(masiv)): #ColumCount
            
            #print(masiv[m][:3])
            d.append(masiv[m][:3])
            if(temp.count(masiv[m][:3])==0):
                temp.append(masiv[m][:3])
        for k in range(len(temp)): #RowCount
            if(d.count(temp[k]) > g):
                g = d.count(temp[k])     
        #print(d)
        #print(temp)
        #print(g)
        self.pushButton.clicked.connect(self.nariadLoadData)
        self.tableWidget.setColumnCount(len(temp))
        self.tableWidget.setRowCount(g)
        self.tableWidget.setHorizontalHeaderLabels(temp) 
        self.tableWidget.setStyleSheet('QAbstractItemView::indicator {width: 20px; height: 20px;}')
        #border: 1px solid #FFB400;
        #self.pushButton.clicked.connect(self.Clk)
        #print(len(temp)) 
        #print(len(masiv))
        
        self.checKAdd(temp)
        for j in range(g):
            #print(j)
            
            #masiv = ["3423171","3451116","3452752","3450000","3470000","3460000"]
            #temp =['342', '345', '347', '346']
            for l in range (len(temp)):
                
                for r in range(len(masiv)):
                    if(temp[l] == masiv[r][:3] ) : 
                        #print(temp[l])
                        #print(masiv[r])               
                        self.item = QtWidgets.QTableWidgetItem(str(masiv[r]))
                        self.item.setFlags(QtCore.Qt.ItemFlag.ItemIsUserCheckable | QtCore.Qt.ItemFlag.ItemIsEnabled)
                        self.item.setCheckState(QtCore.Qt.CheckState.Unchecked)
                        #cbox = QtWidgets.QCheckBox(str(masiv[r]))
                        #cbox.stateChanged.connect(self.Check)
                        # cbox.setStyleSheet("QCheckBox::indicator:checked" "{"
                        #         "color: #b1b1b1;"
                        #         "background-color: red;"
                        #         "border: 1px solid #b1b1b1;"
                        #         "border-radius: 1px;"
                        #         "width: 15px;"
                        #         "height: 15px;"
                        #         "margin: 0px 5px 0 5px;"
                        #     "}"
                        #     "QCheckBox::indicator" "{"
                        #         "color: #b1b1b1;"
                        #         "background-color: #323232;"
                        #         "border: 1px solid #b1b1b1;"
                        #         "border-radius: 1px;"
                        #         "width: 15px;"
                        #         "height: 15px;"
                        #         "margin: 0px 5px 0 5px;"
                        #     "}"
                        #     )
                        masiv.pop(r)
                        #masiv.insert(r,"0000")
                        #print(masiv)
                        #print(str(items[i][k-2]))
                        #self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                        #self.tableWidget.setItem(j, l, cbox)
                        #self.tableWidget.setCellWidget(j, l, cbox)
                        self.tableWidget.setItem(j,l,self.item)
                        break
            # it_state = QtGui.QStandardItem()
            # it_state.setEditable(False)
            # it_state.setCheckable(True)
            # it_state.setCheckState(QtCore.Qt.Checked if state else QtCore.Qt.UnChecked)
            # it_firstname = QtGui.QStandardItem(firstname)
            # it_lastname = QtGui.QStandardItem(lastname)
            # it_company = QtGui.QStandardItem(company)
            # self.model.appendRow([it_state, it_firstname, it_lastname, it_company])
                #     self.item = QtWidgets.QTableWidgetItem(str(l))
                    
                #     #print(str(items[i][k-2]))
                #     self.item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                #     self.tableWidget.setItem(j, l, self.item)
    def checKAdd(self,data):
        for d in range(len(data)):
            labelname = QPushButton(self.horizontalLayoutWidget)
            self.formLayout.setWidget(d+1,QtWidgets.QFormLayout.LabelRole, labelname)
            #print(txt)
            #labelname.setStyleSheet('QPushButton {background-color: red; color: white;}')
            labelname.setText(data[d])
            labelname.setFont(QFont('Microsoft YaHei', 8))
            labelname.setFocusPolicy(QtCore.Qt.NoFocus)
            labelname.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)
            
            labelname.clicked.connect(self.Check_Answer)
        # for d in range(len(data)):
            
                        
        #     #print(str(items[i][k-2]))
            
            

        #     self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        #     #self.checkBox.setObjectName(str(d+1))
        #     self.formLayout.setWidget(d+1,QtWidgets.QFormLayout.LabelRole, self.checkBox)
        #     self.checkBox.setText(QtCore.QCoreApplication.translate("Dialog"+str(d),data[d]))
        #     self.checkBox.setItem("Dialog"+str(d))
        #     self.checkBox.stateChanged.connect(self.Check_Answer)
    def retriveCheck(self):
        data = []
        for row in range(self.tableWidget.columnCount()):
            for col in range(self.tableWidget.rowCount()):
                try:
                    if self.tableWidget.item(col,row).checkState() == QtCore.Qt.CheckState.Checked:
                        #print([self.tableWidget.item(col,row).text()])
                        data.append(self.tableWidget.item(col,row).text())
                except AttributeError:
                    pass
                    #print("There is no such attribute") 
        return data               
    #def buttomClk():

    def Check_Answer(self):
        #print(self.sender().text())
        for row in range(self.tableWidget.columnCount()):
            for col in range(self.tableWidget.rowCount()):
                try:
                    #if self.tableWidget.item(col,row).checkState() == QtCore.Qt.CheckState.Checked:
                        #print([self.tableWidget.item(col,row).text()])
                        if(self.sender().text() == self.tableWidget.item(col,row).text()[:3]):
                            #pass
                            if self.tableWidget.item(col,row).checkState() == QtCore.Qt.CheckState.Checked:
                                self.tableWidget.item(col,row).setCheckState(QtCore.Qt.CheckState.Unchecked)
                            else:
                                self.tableWidget.item(col,row).setCheckState(QtCore.Qt.CheckState.Checked)
                            #print(self.tableWidget.item(col,row).text())
                except AttributeError:
                    pass
        #pass
    def getKodAts(self):
        codAts=[]
        data = self.retriveCheck()
        #print(data)
        for d in range(len(data)):
            #print(data[d][:3])
            if(codAts.count(data[d][:3])==0):
                codAts.append(data[d][:3])
        return codAts,data
    def nariadLoadData(self):
        t = nameTime()
        gKA,nomera = self.getKodAts()
        #nomera = self.retriveCheck()
        for g in range(len(gKA)):
            data = infoToNariad(gKA[g]+"0000",gKA[g]+"9999",self.ln,self.pd)
            #print(self.x,self.y)
            self.SearchXY(data,nomera)
            nariadWrite(self.tempDataG,t)
            #print(self.x,self.y)
            #print(self.tempDataG)
            self.x.clear()
            self.y.clear()
            self.tempDataG.clear()
        webbrowser.open(t)    
        

        pass
    def SearchXY(self,data,spisokN):
        dataNsort = data
        
        a = 0
        #print(type(data))
        for i in range(len(dataNsort)):
            
            if(spisokN.count(dataNsort[i][0:7]) > 0):
                #print(dataNsort[i][0:7])
                self.x.append(i)
                #nomera.append(dataNsort[i][0:7])
                a = 1
            if(dataNsort[i][1:5]=="----" and a == 1):
                self.y.append(i)
                a = 0
        # x.pop(2)
        # y.pop(2)
        for iz in range(len(self.x)):
            tempData=[]
            #print(len(y),len(x))
            col = self.y[iz]-self.x[iz]
            for ss in range(col+1):
                #print(dataNsort[self.x[iz]+ss][0:5])
                if(dataNsort[self.x[iz]+ss][0:2] != "- "):
                    tempData.append(dataNsort[self.x[iz]+ss].split())
                    self.tempDataG.append(tempData.copy())
                    tempData.clear()     
def nariadWrite(tempDataS,name):
#print(name)         
    f = open(name,'a+',encoding="UTF-8")
    #f.write('Hello \n World')
    for aa in range(len(tempDataS)):

        a = ' '.join(tempDataS[aa][0])
        if((a[0:1]=="3" or a[0:1]=="4" or a[0:1]=="5" or a[0:1]=="7")and aa == 0):
            txt =  tempDataS[aa][0][0]
            #print(internet.count(txt))
            print(txt)
            db = "base\\" + txt[0:3] + ".db"
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            cursor.execute("select * from AbonInfo where nomer=:c",{"c":txt}) 
            search = cursor.fetchall()
            conn.close()
            #f.write(txt[2:] + (" +ADSL" if internet.count(txt) else "" ) +"\n")
            f.write(txt +"\n")
            #ts = tempDataS[aa]
            #print(ts)
            f.write(" ".join(tempDataS[aa][0]).replace(tempDataS[aa][0][0],"")[1:] + "\n")
            #print(txt)
            #print(search)
            #print("+++")
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
    extra = {
    'font_family': 'Microsoft YaHei',
    # Density Scale
    #'density_scale': '0',
    }
      
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = nariadApp(masiv)  # Создаём объект класса ExampleApp
    #apply_stylesheet(app, theme='dark_amber.xml', invert_secondary=False,extra=extra)
    #qtmodern.styles.dark(app)
    
    #mw = qtmodern.windows.ModernWindow(window)
    #mw.show()  # Показываем окно
    window.show()
    #print("KKK") 
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()