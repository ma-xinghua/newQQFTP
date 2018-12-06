import sys
from ftplib import FTP
from client import Ui_Dialog
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import QStringListModel
from tkinter.filedialog import askopenfilename
    
class ftpclass():
    def __init__(self):
        self.relogin = False      #relogin状态
        self.curdata = ''         #文件名列表
        self.username = ''
        self.password = ''
        self.host = ''
        self.prevcwd = []         #上一级文件夹名
        
    def connect(self,user,passwd,host):      #login使用的函数
        self.username = user
        self.password = passwd
        self.client = FTP(host)
        self.host = host
        self.relogin = True
        self.client.login(user,passwd)
        self.client.encoding='gbk'
        self.getcwd()        

        
    def getcwd(self):           #显示文件列表函数
        self.curdata = self.client.nlst()      #用nlst返回文件列表，用dir只能打印文件名，但是有详细信息
        
        
    def relog(self):             #relogin函数，用于刷新状态
        if self.relogin == False:
            showinfo('FTP','You must login at least 1 time to relog')
            return 0
        self.client = FTP(self.host)
        self.client.login(self.username,self.password)
        self.getcwd()
        self.prevcwd = []      #回到主文件夹
        
    def download(self,file):         #下载文件
        local = open(file,'wb')
        self.client.retrbinary('RETR '+file,local.write,1024)
        local.close()
        

    def unpload(self):           #上传文件
        file = askopenfilename()        
        name = file.split('/')[-1]      #从路径取文件名
        local = open(file,'rb')
        self.client.storbinary('STOR '+name,local,1024)
        local.close()
        

    def changecwd(self,dr):          #改变路径，选择文件夹
        self.client.cwd(dr)
        self.getcwd()

    def mkdir(self):            #创建文件夹
        dr = askstring('FTP','Enter the name of the folder')
        try:
          self.client.mkd(dr)
        except:
          showinfo('Error','Unable to create Directory on the remote server')

global f
f=ftpclass()


class mywindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def create(self):
        print ("hahahanima")

    def login(self):
        self.textBrowser.append("Beginning login.")
        try:
            f.connect(self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit.text())
            self.textBrowser.append("Login successfully!")
            print (f.curdata)
        except:
            self.textBrowser.append("ERROR!Failing to login.")
        self.listshow()

    def back(self):
        f.changecwd('..')          #返回上一级
        self.listshow()
        f.prevcwd.append(f.client.pwd())        #不知道要不要
        self.textBrowser.append("Go back.")
        

    def enter(self):
        try:
            row = self.listView.currentIndex().row();        #返回点击的所在行
            dr = f.curdata[row]
            f.changecwd(dr)
            self.listshow()
            f.prevcwd.append(f.client.pwd())        #不知道要不要
            self.textBrowser.append("Enter the directory.%s"%dr)
        except:
            self.textBrowser.append("It's not a directory.")

    def rename(self):
        print ("hahahanima")

    def upload(self):
        try:
            f.unpload()
            f.getcwd()
            self.listshow()
            self.textBrowser.append("You have successfully upload.")
        except:
            self.textBrowser.append("Failed.")

    def download(self):
        try:
            row = self.listView.currentIndex().row(); 
            dr = f.curdata[row]
            f.download(dr)
            self.textBrowser.append("You have successfully download the %s."%dr)
        except:
            self.textBrowser.append("You cannot download that.")

    def delete(self):
        print ("hahahanima")

    def quit(self):
        self.close()

    def listshow(self):
        slm=QStringListModel()         #在listView框中显示所有文件名
        slm.setStringList(f.curdata)
        self.listView.setModel(slm)
        
if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())

