import sys
from ftplib import FTP
from client import Ui_Dialog
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog,QMessageBox

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
            self.Client=FTP(self.lineEdit.text())
            self.Client.login(self.lineEdit_2.text(),self.lineEdit_3.text())
            self.Client.encoding='gbk'
            self.textBrowser.append("Login successfully!")
        except:
            self.textBrowser.append("ERROR!Failing to login.")
    def back(self):
        print ("hahahanima")
    def enter(self):
        print ("hahahanima")
    def rename(self):
        print ("hahahanima")
    def upload(self):
        print ("hahahanima")
    def download(self):
        print ("hahahanima")
    def delete(self):
        print ("hahahanima")
    def quit(self):
        print ("hahahanima")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())

