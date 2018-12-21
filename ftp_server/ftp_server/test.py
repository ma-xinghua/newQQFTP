import sys
import os
from server import Ui_Dialog_server
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from create import *
from ftp_server import *
from change import *
from modify import *

class createwindow(QtWidgets.QWidget, Ui_Dialog_create):
    def __init__(self):
        super(createwindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def create(self):
        self.userName=self.lineEdit.text()
        self.userPasscode=self.lineEdit_2.text()
        self.userPasscodeAgain=self.lineEdit_3.text()
        self.Docupass=self.lineEdit_4.text()
        #print (self.userName)
        #print (self.userPasscode)
        #print (self.userPasscodeAgain)
        #print (self.Docupass)
        self.authority=""
        if (self.checkBox.isChecked()):
            self.authority=self.authority+"e"
        if (self.checkBox_2.isChecked()):
            self.authority=self.authority+"l"
        if (self.checkBox_3.isChecked()):
            self.authority=self.authority+"r"
        if (self.checkBox_4.isChecked()):
            self.authority=self.authority+"d"
        if (self.checkBox_5.isChecked()):
            self.authority=self.authority+"a"
        if (self.checkBox_6.isChecked()):
            self.authority=self.authority+"m"
        if (self.checkBox_7.isChecked()):
            self.authority=self.authority+"f"
        if (self.checkBox_8.isChecked()):
            self.authority=self.authority+"w"
        #print (self.authority)
        file = open('userinfo.ini','r',encoding = 'UTF-8')
        for line in file.readlines():
            self.information=line.split()
            if self.userName==self.information[0]:
                warning6=QMessageBox.warning(self,"警告","该用户名已存在")
                return
        file.close()
        if (self.userName==""):
            warning3=QMessageBox.warning(self,"警告","用户名不能为空")
            return
        if (self.userPasscode==''):
            warning4=QMessageBox.warning(self,"警告","密码不能为空")
            return
        if (self.userPasscode!=self.userPasscodeAgain):
            warning1=QMessageBox.warning(self,"警告","两次输入密码不一致")
            return
        if (self.authority==""):
            warning2=QMessageBox.warning(self,"警告","必须选择一个权限")
            return
        if (self.Docupass==''):
            warning5=QMessageBox.warning(self,"警告","路径不能为空")
        if not os.path.exists(self.Docupass):
               os.makedirs(self.Docupass) #如果不存在这个文件夹，就创建一个
        file = open('userinfo.ini', 'a')
        self.word = '\n'+self.userName+' '+self.userPasscode+' '+self.authority+' '+self.Docupass
        file.write(self.word)
        file.close()
        information=QMessageBox.information(self,"提示","新用户成功创建")
        self.close()

class changewindow(QtWidgets.QWidget, Ui_Dialog_change):
    def __init__(self):
        super(changewindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def change(self):
        self.userName=self.lineEdit.text()
        self.userPasscode=self.lineEdit_2.text()
        self.data = ''
        self.array=[]
        self.ctr=1
        file = open('userinfo.ini','r',encoding = 'UTF-8')
        self.information=file.readlines()
        file.close()
        for line in self.information:
                self.array= line.split()
                if((self.userName == self.array[0]) and (self.userPasscode == self.array[1])):
                    self.ctr=0
                    if(self.checkBox.isChecked()):
                        self.array[0]=self.lineEdit_3.text()
                        if(self.array[0]==""):
                            warning3=QMessageBox.warning(self,"警告","你的用户名不能为空")
                            return
                    if(self.checkBox_2.isChecked()):
                        self.array[1]=self.lineEdit_4.text()
                        if(self.array[1]==""):
                            warning4=QMessageBox.warning(self,"警告","你的密码不能为空")
                            return
                    if(self.checkBox_3.isChecked()):
                        self.authority=""
                        if (self.checkBox_5.isChecked()):
                            self.authority=self.authority+"e"
                        if (self.checkBox_6.isChecked()):
                            self.authority=self.authority+"l"
                        if (self.checkBox_7.isChecked()):
                            self.authority=self.authority+"r"
                        if (self.checkBox_8.isChecked()):
                            self.authority=self.authority+"d"
                        if (self.checkBox_9.isChecked()):
                            self.authority=self.authority+"a"
                        if (self.checkBox_10.isChecked()):
                            self.authority=self.authority+"m"
                        if (self.checkBox_11.isChecked()):
                            self.authority=self.authority+"f"
                        if (self.checkBox_12.isChecked()):
                            self.authority=self.authority+"w"
                        if (self.authority==""):
                            warning1=QMessageBox.warning(self,"警告","你必须选择一个权限")
                            return
                        self.array[2]=self.authority
                    if(self.checkBox_4.isChecked()):
                        self.array[3]=self.lineEdit_5.text()
                        if(self.array[3]==""):
                            warning5=QMessageBox.warning(self,"警告","你的路径不能为空")
                            return
                    self.data="\n"+self.array[0]+" "+self.array[1]+" "+self.array[2]+" "+self.array[3]
                    self.information.remove(line)
                    self.information.append(self.data)
        if(self.ctr):
            warning2=QMessageBox.warning(self,"警告","用户名或密码错误")
            return
        if not os.path.exists(self.array[3]):
            os.makedirs(self.array[3]) #如果不存在这个文件夹，就创建一个
        file_new=open('userinfo.ini','w',encoding='UTF-8')
        for line in self.information:
            file_new.write(line)
        file_new.close()
        information1=QMessageBox.information(self,"提示","用户信息已经修改")
        self.close()



class modifywindow(QtWidgets.QWidget, Ui_Dialog_modify):
    def __init__(self):
        super(modifywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def modify(self):
        self.startPort=self.lineEdit.text()
        self.endPort=self.lineEdit_2.text()
        self.uploadSpeed=self.lineEdit_3.text()
        self.downloadSpeed=self.lineEdit_4.text()   
        if(self.checkBox.isChecked()):
            if ((self.startPort=='') or (self.endPort=='')):
                warning1=QMessageBox.warning(self,"警告","你必须指明起始和结束端口")
                return
            if (eval(self.startPort)<1023 or eval(self.endPort)>49151):
                warning2=QMessageBox.warning(self,"警告","你只能使用1024~49151的登记端口")
                return
            if ((eval(self.endPort)-eval(self.startPort))>255):
                warning3=QMessageBox.warning(self,"警告","你最多只能开放256个端口")
                return
        if(self.checkBox_2.isChecked()):
            if ((self.uploadSpeed=='') or (self.downloadSpeed=='')):
                warning4=QMessageBox.warning(self,"警告","你必须指明上传和下载速度")
                return
        if(self.checkBox_3.isChecked()):
            if ((self.checkBox_4.isChecked() and self.checkBox_5.isChecked())):
                warning5=QMessageBox.warning(self,"警告","你的日志选择有误")
                return
        file = open('config_ftp.py','r',encoding = 'UTF-8')
        self.array=file.readlines()
        file.close()
        i=0
        for line in self.array:
            if(self.checkBox.isChecked()):
                if ('passive_ports' in line):
                    self.array[i]='passive_ports = ('+self.startPort+','+self.endPort+')\n'
            if(self.checkBox_2.isChecked()):
                if ('max_upload' in line):
                    self.array[i]='max_upload = '+self.uploadSpeed+' * 1024\n'
                if ('max_download' in line):
                    self.array[i]='max_download = '+self.downloadSpeed+' * 1024\n'
            if(self.checkBox_3.isChecked()):
                if (self.checkBox_4.isChecked()):
                    if('enable_logging' in line):
                        self.array[i]='enable_logging = True\n'
                if (self.checkBox_5.isChecked()):
                    if('enable_logging' in line):
                        self.array[i]='enable_logging = False\n'
            i=i+1
        file_new=open('config_ftp.py','w',encoding='UTF-8')
        for lines in self.array:
             file_new.write(lines)
        file_new.close()
        information1=QMessageBox.information(self,"提示","服务器配置已经修改")
        self.close()

class mywindow(QtWidgets.QWidget, Ui_Dialog_server):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

    # 定义槽函数
    def newuser(self):
        self.create_app = QtWidgets.QApplication(sys.argv)
        self.create_show = createwindow()
        self.create_show.show()
         
    def changeuser(self):
        self.change_app = QtWidgets.QApplication(sys.argv)
        self.change_show = changewindow()
        self.change_show.show()
         
    def modify(self):
        self.modify_app = QtWidgets.QApplication(sys.argv)
        self.modify_show = modifywindow()
        self.modify_show.show()
        
    def start(self):
        self.close()
        ftp()
        
    
    
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
    
    
