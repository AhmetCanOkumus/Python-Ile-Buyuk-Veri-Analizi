from untitled_python import  Ui_MainWindow
from PyQt5.QtWidgets import *
import pandas as pd
import threading

df = pd.read_csv('currentfile.csv', usecols=['Product', 'Issue','Company','State','ZIP code','Complaint ID'])
df2 = pd.read_csv('currentfile.csv', usecols=['Product', 'Issue','Company','State','ZIP code','Complaint ID'])


threads=[]


def zipcodegetir(baslangic,zip_code,columngetir1,arananoran,self,sayac):
    baslangic2=baslangic
    baslangic3=baslangic
    for i in range(len(df)):
     baslangic3=baslangic
     row1=baslangic2
     arama1string=df.loc[int(row1),"columngetir1"]
     arama1list=list(arama1string.split(" ")) #kayıtı stringe çevirme
     arama1uzunluk=len(arama1list)
     baslangic2=baslangic2+1
     if(baslangic2==baslangic+sayac):
        break     
     for j in range(len(df)):
        row2=baslangic3
        arama2string=df.loc[int(row2),"columngetir2"]
        arama2list=list(arama2string.split(" "))
        arama2uzunluk=len(arama2list)
        benzerkelime=list(set(arama1list).intersection(arama2list))
        benzerkelimesayisi=len(benzerkelime)
        if(arama1uzunluk>arama2uzunluk):
            oran=(benzerkelimesayisi/arama1uzunluk)*100
        if(arama1uzunluk<arama2uzunluk):
            oran=(benzerkelimesayisi/arama2uzunluk)*100    
        if(arama1uzunluk==arama2uzunluk):
            oran=(benzerkelimesayisi/arama2uzunluk)*100
        if(oran>=int(arananoran)):
            if(df.at[int(row1),"ZIP code"]==zip_code):
                if(df.at[int(row2),"ZIP code"]==zip_code):
                    print("Verilen Zip code'a sahip ve belirtilen benzerlik oranındaki kayıtlar "+str(int(row1))+"  "+str(int(row2))+df.at[int(row1),columngetir1]+"  "+df.at[int(row2),columngetir1])
        baslangic3=baslangic3+1





def complaintidgetir(baslangic,complaintid,columngetir1,arananoran,self,sayac):
    baslangic2=baslangic
    baslangic3=baslangic
    for i in range(len(df)):
     baslangic3=baslangic
     row1=baslangic2
     arama1string=df.loc[int(row1),columngetir1]
     arama1list=list(arama1string.split(" ")) #kayıtı stringe çevirme
     arama1uzunluk=len(arama1list)
     baslangic2=baslangic2+1
     if(baslangic2==baslangic+sayac):
        break
     for j in range(len(df)):
        row2=baslangic3
        arama2string=df.loc[int(row2),columngetir1]
        arama2list=list(arama2string.split(" "))
        arama2uzunluk=len(arama2list)
        benzerkelime=list(set(arama1list).intersection(arama2list))
        benzerkelimesayisi=len(benzerkelime)
        if(arama1uzunluk>arama2uzunluk):
            oran=(benzerkelimesayisi/arama1uzunluk)*100
        if(arama1uzunluk<arama2uzunluk):
            oran=(benzerkelimesayisi/arama2uzunluk)*100    
        if(arama1uzunluk==arama2uzunluk):
            oran=(benzerkelimesayisi/arama2uzunluk)*100
        if(oran>=int(arananoran)):
            if(df.at[int(row1),"Complaint ID"]==complaintid):
                if(df.at[int(row2),"Complaint ID"]==complaintid):
                    print("Verilen Complaint ID'li ve belirtilen benzerlik oranındaki kayıtlar "+str(int(row1))+"  "+str(int(row2))+df.at[int(row1),columngetir1]+"  "+df.at[int(row2),columngetir1])
        baslangic3=baslangic3+1



def ikisutungetir(baslangic,columnarama,columngetir1,columngetir2,arananoran,self,sayac):
    baslangic2=baslangic
    baslangic3=baslangic
    for i in range(len(df)):
     baslangic3=baslangic
     row1=baslangic2
     kontrol1=df.loc[int(row1),columnarama]
     kontrol1list=list(kontrol1.split(" "))
     arama1string=df.loc[int(row1),columngetir1]
     arama1list=list(arama1string.split(" ")) #kayıtı stringe çevirme
     arama1uzunluk=len(arama1list)
     arama11string=df.loc[int(row1),columngetir2]
     arama11list=list(arama11string.split(" ")) #kayıtı stringe çevirme
     arama11uzunluk=len(arama11list)
     baslangic2=baslangic2+1
     if(baslangic2==baslangic+sayac):
        break
     for j in range(len(df)):
        row2=baslangic3
        kontrol2=df.loc[int(row2),columnarama]
        kontrol2list=list(kontrol2.split(" "))
        arama2string=df.loc[int(row2),columngetir1]
        arama2list=list(arama2string.split(" "))
        arama2uzunluk=len(arama2list)
        arama22string=df.loc[int(row2),columngetir2]
        arama22list=list(arama22string.split(" "))
        arama22uzunluk=len(arama22list)
        benzerkelime=list(set(arama1list).intersection(arama2list))
        benzerkelimesayisi=len(benzerkelime)
        benzerkelime2=list(set(arama11list).intersection(arama22list))
        benzerkelimesayisi2=len(benzerkelime2)
        if(arama1uzunluk>arama2uzunluk ):
            oran=(benzerkelimesayisi/arama1uzunluk)*100
        if(arama1uzunluk<arama2uzunluk):
            oran=(benzerkelimesayisi/arama2uzunluk)*100    
        if(arama1uzunluk==arama2uzunluk):
            oran=(benzerkelimesayisi/arama2uzunluk)*100

        if(arama11uzunluk>arama22uzunluk):
            oran2=(benzerkelimesayisi2/arama11uzunluk)*100
        if(arama11uzunluk<arama22uzunluk):
            oran2=(benzerkelimesayisi2/arama22uzunluk)*100    
        if(arama11uzunluk==arama22uzunluk):
            oran2=(benzerkelimesayisi2/arama22uzunluk)*100            
        if(oran>=int(arananoran) and oran2>=int(arananoran)):
            if(kontrol2list==kontrol1list):
             print(columnarama+"  Aynı Olan ve "+arananoran+" ve üzeri benzerliğe sahip kayıtlar"+str(row1)+"  "+str(row2)+"   "+df.at[int(row1),columngetir1]+"   "+df.at[int(row2),columngetir1]+"   "+df.at[int(row1),columngetir2]+"   "+df.at[int(row2),columngetir2])
        baslangic3=baslangic3+1




def birsutunugetir(baslangic,columnarama,columngetir1,arananoran,self,sayac):
    baslangic2=baslangic
    baslangic3=baslangic
    for i in range(len(df)):
     baslangic3=baslangic
     row1=baslangic2
     kontrol1=df.loc[int(row1),columnarama]
     arama1string=df.loc[int(row1),columngetir1]
     arama1list=list(arama1string.split(" ")) #kayıtı stringe çevirme
     arama1uzunluk=len(arama1list)
     baslangic2=baslangic2+1
     if(baslangic2==baslangic+sayac):
        break
     for j in range(len(df)):
        row2=baslangic3
        kontrol2=df.loc[int(row2),columnarama]
        arama2string=df.loc[int(row2),columngetir1]
        arama2list=list(arama2string.split(" "))
        arama2uzunluk=len(arama2list)
        benzerkelime=list(set(arama1list).intersection(arama2list))
        benzerkelimesayisi=len(benzerkelime)
        if(arama1uzunluk>arama2uzunluk):
            oran=(benzerkelimesayisi/arama1uzunluk)*100
        if(arama1uzunluk<arama2uzunluk):
            oran=(benzerkelimesayisi/arama2uzunluk)*100    
        if(arama1uzunluk==arama2uzunluk):
            oran=(benzerkelimesayisi/arama2uzunluk)*100
        if(oran>=int(arananoran)):
            if(kontrol1==kontrol2):
             print(columnarama +"  aynı olan"+arananoran+" ve üzeri benzerlikte olan "+columngetir1+" kayıtları  "+"Kayıt "+str(row1)+" ,"+str(row2)+"  "+df.at[int(row1),columngetir1]+"  "+df.at[int(row2),columngetir1])
        baslangic3=baslangic3+1





def birsutunbenzerlik(baslangic,columnn,arananoran,self,sayac):
        baslangic2=baslangic
        baslangic3=baslangic
        for i in range(len(df)):
         baslangic3=baslangic
         row1=baslangic2
         birincistring=df.loc[int(row1),columnn]
         birincilist=list(birincistring.split(" ")) #kayıtı stringe çevirme
         birinciuzunluk=len(birincilist)
         baslangic2=baslangic2+1
         if(baslangic2==baslangic+sayac):
          break
         for j in range(len(df)):
            row2=baslangic3
            ikincistring=df2.loc[int(row2),columnn]
            ikincilist=list(ikincistring.split(" "))
            ikinciuzunluk=len(ikincilist)
            benzerkelime=list(set(birincilist).intersection(ikincilist))
            benzerkelimesayisi=len(benzerkelime)
            if(birinciuzunluk>ikinciuzunluk):
                orann=(benzerkelimesayisi/birinciuzunluk)*100
            if(ikinciuzunluk>birinciuzunluk):
                orann=(benzerkelimesayisi/ikinciuzunluk)*100
            if(birinciuzunluk==ikinciuzunluk):
                orann=(benzerkelimesayisi/ikinciuzunluk)*100 
            if(int(orann)>=int(arananoran)):
              if(row1!=row2):
               #self.ui.textBrowser.setText(str(row1)+" ve "+str(row2)+"kayıtları %100 ve üzeri benzerlikte")
               print(str(int(row1))+" ve "+str(int(row2))+"  kayıtları "+arananoran+" ve üzeri benzerliktedir   "+df.at[int(row1),columnn],"  "+df.at[int(row2),columnn])
            baslangic3=baslangic3+1



class ders(QMainWindow):
    def __init__(self):
        received_signal="ahmet"
        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Birsutungoster.clicked.connect(self.process)
        self.ui.ayni1sutungoster.clicked.connect(self.process2)
        self.ui.ayni2sutungoster.clicked.connect(self.process3)
        self.ui.complaintidgetir.clicked.connect(self.process4)
        self.ui.zipcodegetir.clicked.connect(self.process5)

    def process(self):
        
        arananoran=self.ui.lineEdit.text()
        thread_sayisi=self.ui.threadsayisi.text()
        columnn=self.ui.sutunsec.text()
        print("Aranılacak sutun: "+columnn)
        print("Alinan benzerlik:"+arananoran)
        print("Thread sayisi"+str(thread_sayisi))
        
        temp=0
        sayac=len(df)/int(thread_sayisi)

        for _ in range(int(thread_sayisi)):
            t=threading.Thread(target=birsutunbenzerlik(temp,columnn,arananoran,self,sayac))
            t.start()
            threads.append(t)
            temp=temp+sayac
        for thread in threads:
           thread.join()

    def process2(self):
        columnarama=self.ui.lineEdit_4.text()
        arananoran=self.ui.lineEdit_5.text()
        columngetir1=self.ui.lineEdit_2.text()
        thread_sayisi=self.ui.threadsayisi.text()

        temp=0
        sayac=len(df)/int(thread_sayisi)

        for _ in range(int(thread_sayisi)):
            t=threading.Thread(target=birsutunugetir(temp,columnarama,columngetir1,arananoran,self,sayac))
            t.start()
            threads.append(t)
            temp=temp+sayac
        for thread in threads:
           thread.join()


    def process3(self):
        columnarama=self.ui.lineEdit_4.text()
        arananoran=self.ui.lineEdit_5.text()
        columngetir1=self.ui.lineEdit_2.text()
        columngetir2=self.ui.lineEdit_3.text()
        thread_sayisi=self.ui.threadsayisi.text()

        temp=0
        sayac=len(df)/int(thread_sayisi)

        for _ in range(int(thread_sayisi)):
            t=threading.Thread(target=ikisutungetir(temp,columnarama,columngetir1,columngetir2,arananoran,self,sayac))
            t.start()
            threads.append(t)
            temp=temp+sayac
        for thread in threads:
           thread.join()

    def process4(self):
        complaint_id=self.ui.lineEdit_6.text()
        arananoran=self.ui.lineEdit_10.text()
        columngetir1=self.ui.lineEdit_7.text()
        thread_sayisi=self.ui.threadsayisi.text()

        temp=0
        sayac=len(df)/int(thread_sayisi)

        for _ in range(int(thread_sayisi)):
            t=threading.Thread(target=complaintidgetir(temp,complaint_id,columngetir1,arananoran,self,sayac))
            t.start()
            threads.append(t)
            temp=temp+sayac
        for thread in threads:
           thread.join()


    def process5(self):
        zip_code=self.ui.lineEdit_8.text()
        arananoran=self.ui.lineEdit_11.text()
        columngetir1=self.ui.lineEdit_9.text()
        thread_sayisi=self.ui.threadsayisi.text()
        temp=0
        sayac=len(df)/int(thread_sayisi)

        for _ in range(int(thread_sayisi)):
            t=threading.Thread(target=zipcodegetir(temp,zip_code,columngetir1,arananoran,self,sayac))
            t.start()
            threads.append(t)
            temp=temp+sayac
        for thread in threads:
           thread.join()




uygulama =QApplication([])
pencere=ders()
pencere.show()
uygulama.exec_()