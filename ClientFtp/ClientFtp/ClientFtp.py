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
            f.connect(self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit.text())
            self.textBrowser.append("Login successfully!")
            self.listshow()
            file = open("info.txt",'w')              #将用户这次的登陆信息分三行全部写入info.txt中，格式为地址，用户名，密码
            file.write(self.lineEdit.text()+'\n')
            file.write(self.lineEdit_2.text()+'\n')
            file.write(self.lineEdit_3.text()+'\n')
            file.close()
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
            self.textBrowser.append("Size: %.2f KB, Time: %.2f s"%(f.size,f.time))  #显示传输文件的大小和时间
        except:
            self.textBrowser.append("EEROR!Failing to upload.")

    def download(self):
        try:
            row = self.listView.currentIndex().row()
            dr = f.curdata[row]
            f.download(dr)
            self.textBrowser.append("You have successfully download %s"%dr)
            self.textBrowser.append("Size: %.2f KB, Time: %.2f s"%(f.size,f.time))    #显示传输文件的大小和时间
        except:
            self.textBrowser.append("EEROR!Failing to download.")

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

    def clicked(self):        #处理在listView中对于每一项鼠标双击的动作，即双击后自动进入该文件夹
        self.enter()

    def listshow(self):
        slm=QStringListModel()         #在listView框中显示所有文件名
        slm.setStringList(f.curdata)
        self.listView.setModel(slm)
        list=[]                          #用来显示文件夹内文件的详细信息
        f.client.dir('.', list.append)
        self.textBrowser_2.clear()     #清除上一次的信息
        for i in list:
            self.textBrowser_2.append(i)    #把信息写在“详细信息”框中
        
if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())

