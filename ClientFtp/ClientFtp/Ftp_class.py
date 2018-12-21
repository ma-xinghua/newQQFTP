#coding=utf-8
import os
import time
from ftplib import FTP
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askstring
import tkinter

class ftpclass():
    def __init__(self):
        self.relogin = False      #relogin状态
        self.curdata = ''         #文件名列表
        self.username = ''
        self.password = ''
        self.host = ''
        self.size = 0        #储存当前传输文件的大小
        self.time = 0        #储存时间
        
    def connect(self,user,passwd,host):      #login使用的函数
        self.username = user
        self.password = passwd
        self.client = FTP(host)
        self.host = host
        self.relogin = True
        self.client.login(user,passwd)      
        self.client.encoding='gbk'
        self.getcwd()        
      
    def getcwd(self):           #更新文件列表函数
        self.curdata = self.client.nlst()      #用nlst返回文件列表，用dir只能打印文件名，但是有详细信息
        
    def download(self,file):         #下载文件
        local = open(file,'wb')
        time_start = time.time()
        self.client.retrbinary('RETR '+file,local.write,1024)
        time_end = time.time()
        self.time = time_end-time_start
        self.size = os.path.getsize(file)
        self.size = self.size/float(1024)
        local.close()
         
    def unpload(self):           #上传文件
        root = tkinter.Tk()      
        root.withdraw()
        file = askopenfilename()
        root.destroy()
        name = file.split('/')[-1]      #从路径取文件名
        local = open(file,'rb')
        time_start = time.time()
        self.client.storbinary('STOR '+name,local,1024)
        time_end = time.time()
        self.time = time_end-time_start
        self.size = os.path.getsize(file)
        self.size = self.size/float(1024)
        local.close()
        self.getcwd()
        
    def changecwd(self,dr):          #改变路径，选择文件夹
        self.client.cwd(dr)
        self.getcwd()

    def mkdir(self):            #创建文件夹
        root = tkinter.Tk()      #解决多线程中askstring的问题
        root.withdraw()
        dr = askstring("FTP", "Enter the name of the folder.")
        root.destroy()
        self.client.mkd(dr)
        self.getcwd()

    def dellete(self,dr):     #删除文件及文件夹
        try:
            self.client.delete(dr)    #删除文件
        except:
            self.client.rmd(dr)    #删除文件夹
        self.getcwd()

    def rename(self,dr):
        root = tkinter.Tk()      #解决多线程中askstring的问题
        root.withdraw()
        dr2 = askstring("FTP", "What name do you want to change to?")
        root.destroy()
        self.client.rename(dr,dr2)
        self.getcwd()

    