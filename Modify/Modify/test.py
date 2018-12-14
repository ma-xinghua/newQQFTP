import sys
from Modify import Ui_Dialog
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog,QMessageBox

class mywindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())

