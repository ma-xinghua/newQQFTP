import sys
from Ftp_class import *
from client import Ui_Dialog
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import QStringListModel

global f
f=ftpclass()

class mywindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def create(self):
        try:
            f.mkdir()
            self.listshow()
            self.textBrowser.append("You have successfully create it.")
        except:
            self.textBrowser.append("EEROR!Failing to create.")

    def login(self):
        self.textBrowser.append("Beginning login.")
        try:
            f.connect("yaolh","public","public.sjtu.edu.cn")
            self.textBrowser.append("Login successfully!")
            self.listshow()
        except:
            self.textBrowser.append("ERROR!Failing to login.")
        
    def back(self):
        f.changecwd('..')          #返回上一级
        self.listshow()
        self.textBrowser.append("Go back.")
        

    def enter(self):
        try:
            row = self.listView.currentIndex().row();        #返回点击的所在行
            dr = f.curdata[row]
            f.changecwd(dr)
            self.listshow()
            self.textBrowser.append("Enter the directory.%s"%dr)
        except:
            self.textBrowser.append("It's not a directory.")

    def rename(self):
        try:
            row = self.listView.currentIndex().row();        #返回点击的所在行
            dr1 = f.curdata[row]
            f.rename(dr1)
            self.listshow()
            self.textBrowser.append("You have changed successfully.")
        except:
            self.textBrowser.append("ERROR!Failing to rename.")
        

    def upload(self):
        try:
            f.unpload()
            self.listshow()
            self.textBrowser.append("You have successfully upload.")
        except:
            self.textBrowser.append("EEROR!Failing to upload.")

    def download(self):
        try:
            row = self.listView.currentIndex().row()
            dr = f.curdata[row]
            f.download(dr)
            self.textBrowser.append("You have successfully download %s."%dr)
        except:
            self.textBrowser.append("You cannot download that.")

    def delete(self):
        try:
            row = self.listView.currentIndex().row() 
            dr = f.curdata[row]
            f.dellete(dr)
            self.listshow()
            self.textBrowser.append("You have successfully delete %s."%dr)
        except:
            self.textBrowser.append("EEROR!Failing to delete.")

    def quit(self):
        f.client.quit()
        self.close()

    def listshow(self):
        slm=QStringListModel()         #在listView框中显示所有文件名
        slm.setStringList(f.curdata)
        self.listView.setModel(slm)
        f.client.dir('.', f.list.append)
        for i in f.list:
            self.textBrowser_2.append(i)
        
if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())

