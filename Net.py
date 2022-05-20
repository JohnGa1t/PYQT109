from bs4 import BeautifulSoup
import requests
from datetime import date, datetime,timedelta


#link = 'http://10.15.10.241/cgi-bin/T_S.cgi'


def infoToNariad(data,data2,l_n,l_pd):

    R = requests.post(l_n, data = {"ats": data[0:3],"nt": data[3:7],"kt": data2[3:7]})
    if R.status_code == 200:
        response = requests.post(l_pd)
        soup =BeautifulSoup(response.text,"lxml")
        table = soup.find("pre").find(text=True)
        lines=[]
        lines=table.text.split('\n')
        #print(lines)
        return lines
def infoP(data,l_n,l_pd):
    print("infoP")
    R = requests.post(l_n, data = {"ats": data[0:3],"nt": data[3:7],"kt": data[3:7]})
    if R.status_code == 200:
        response = requests.post(l_pd)
        soup =BeautifulSoup(response.text,"lxml")
        table = soup.find("pre").find(text=True)
        lines=[]
        lines=table.text.split('\n')
        #print(lines)
        return lines
def infoN(data,l_n,l_nd):
    print("infoN")
    R = requests.post(l_n, data = {"ats": data[0:3],"nt": data[3:7],"kt": data[3:7]})
    if R.status_code == 200:
        response = requests.post(l_nd)
        soup =BeautifulSoup(response.text,"lxml")
        table = soup.find("pre").find(text=True)
        lines=[]
        lines=table.text.split('\n')
        return lines
class Sortirofka:

    def __init__(self,link,data,povLinKabProcie,povLinKab):
        self.lines2=[]
        try:
            self.povP = povLinKabProcie
            self.pov = povLinKab
            self.r = requests.post(link)
            if self.r.status_code == 200:
                print('Success!')
                self.soup =BeautifulSoup(self.r.text,"lxml")
                self.table = self.soup.find("pre").find(text=True)
                self.lines=[]
                self.lines=self.table.text.split('\n')
                #for d in range(len(data)):
                for i in range(len(self.lines)):
                    self.a=self.lines[i]
                    #print(self.a[1:3])
                    #dt = str(data[d])
                    #if( "3" == self.a[1:2] or "4" == self.a[1:2] or "5" == self.a[1:2] or "7" == self.a[1:2]):
                    #print(data.count(self.a[1:3]))
                    #print(type(self.a[1:3]))
                    #print(data.count(str(self.a[1:3])))
                    if (data.count(self.a[1:3]) != 0): 
                        self.lines2.append(self.lines[i].replace("|",""))
                # for i in range(len(self.lines)):
                #     self.a=self.lines[i]
                #     if("342"== self.a[1:4]or"345"== self.a[1:4]or"347"== self.a[1:4] ): 
                #         self.lines2.append(self.lines[i].replace("|",""))
                #return  self.lines2    
            # elif self.r.status_code == 404:
            #     print('Not Found.')
            elif    400 <=  self.r.status_code <= 499:
                        print('Not Found.')
                        self.lines2.append('3459999 01.01.22  7:30  О 01.01.22  О                     ')
                        return  
        except requests.exceptions.RequestException as e:
            print('Not Found.exept')
            self.lines2.append('3459999 01.01.22  7:30  О 01.01.22  О                     ')


    def Sort(self,lines2):
        self.d=[]
        self.sort_data = []
        self.data = lines2

        for i in range(len(self.data)):
            
            listRes = list(self.data[i].split()) 
            
            for n in range(len(listRes)):     
                if listRes[n] != '':
                    self.d.append(listRes[n])
            if len(self.d) == 6 :
                for f in range(3):
                    self.d.append(" ")
            if len(self.d) == 4 :
                for f in range(5):
                     self.d.append(" ")                     
            if len(self.d)== 7 :
                self.d.insert(4," ")
                self.d.insert(5," ")

#############################

#############################
            #self.addColor(self.d,i,povLinKabProcie)
            
            #print(self.d)             
            #self.sort_data.insert(i,self.d.copy())
            self.sort_data.insert(i,self.addColor(self.d).copy())
            listRes.clear()
            self.d.clear()
        #print(self.sort_data)    
        return (self.sort_data)

    def addColor(self,items):
            dddd = items[1] + items[2]
            
            ddddz = datetime.strptime(dddd, '%d.%m.%y%H:%M')
            k1= ddddz + timedelta(days=5)
            k2= ddddz + timedelta(days=20)
            GlobTime = datetime.now()
            timeDown = GlobTime.replace(microsecond=0) - ddddz.replace(microsecond=0) 
            if(k1 > GlobTime and k2 > GlobTime and items[5] == " " and items[8] == " " ):     #красный
                items.append("red")
                items.append("OL") 
                #continue           
            elif (k1 > GlobTime and k2 > GlobTime and items[5] != " "and items[8] == " "):       #оранж 
                items.append("orange")
                if(self.povP.count(items[5])==1):
                    items.append("OK") 
                else:
                    items.append("OL") 
                    
                #continue
            elif (k1 < GlobTime and k2 > GlobTime and items[8] == " "):  # желтый
                items.append("yellow")
                if(self.povP.count(items[5])==1):
                    items.append("OK") 
                else:
                    items.append("OL")                
                #continue
            elif (items[8] != " " and self.povP.count(items[8])==0):    #зеленый
                items.append("green")
                if(self.pov.count(items[8])==1):
                    items.append("SK") 
                else:
                    items.append("SL")                
                #continue
            elif (items[8] != " " and self.povP.count(items[8])==1):    #серый
                items.append("grey")
                items.append("") 
                #continue
            elif (k2 < GlobTime and items[8] == " "):  # синий
                items.append("blue") 
                if(self.povP.count(items[5])==1):
                    items.append("OK") 
                else:
                    items.append("OL")                   
            items.append(str(timeDown))
            return items           
# nn = ReadHtml(link)
# s = nn.lines2
# print(s)

# ff = Sortirofka(link)
# print(ff.Sort(ff.lines2))