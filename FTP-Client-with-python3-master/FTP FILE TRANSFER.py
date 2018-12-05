#Created by Callibrator
#Using python 3.x
#callibrator21@gmail.com
#coding:utf-8

from tkinter import *
from ftplib import FTP
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askstring

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
        showinfo('FTP','File succesfully Downloaded')

    def unpload(self):           #上传文件
        file = askopenfilename()        
        name = file.split('/')[-1]      #从路径取文件名
        local = open(file,'rb')
        self.client.storbinary('STOR '+name,local,1024)
        local.close()
        showinfo('FTP','File succesfully unploaded')

    def changecwd(self,dr):          #改变路径，选择文件夹
        self.client.cwd(dr)
        self.getcwd()

    def mkdir(self):            #创建文件夹
        dr = askstring('FTP','Enter the name of the folder')
        try:
          self.client.mkd(dr)
        except:
          showinfo('Error','Unable to create Directory on the remote server')
        
        
root = Tk()
root.title('FTP File Transfer')

global f
f= ftpclass()

conframe = Frame(root)
conframe.pack()

Label(conframe,text='Host: ').pack(side=LEFT)
hosttext = Entry(conframe)
hosttext.pack(side=LEFT)
hosttext.insert(0,'public.sjtu.edu.cn')

Label(conframe,text='Username: ').pack(side=LEFT)
username = Entry(conframe)
username.pack(side=LEFT)
username.insert(0,'yaolh')

Label(conframe,text='Password: ').pack(side=LEFT)
password = Entry(conframe,show='*')
password.pack(side=LEFT)
password.insert(0,'public')


dataframe = Frame(root)
dataframe.pack(expand=YES,fill=BOTH)

data = Listbox(dataframe)
data.pack(side=LEFT,fill=BOTH,expand=YES)

botframe = Frame(root)
botframe.pack()

#以下是与界面连接的函数
def conn(host,user,passwd,lst):           #lst即data（listbox）
    try:
     f.connect(user,passwd,host)
     lst.delete(0,END)
     for i in range(len(f.curdata)):         #将lst信息填入curdata数组
        lst.insert(i,f.curdata[i])

    except:
       showerror('Error','Somthing didn\'t go well :/')
       
def recon(lst):
    try:
        lst.delete(0,END)
        f.relog()
        for i in range(len(f.curdata)):
            lst.insert(i,f.curdata[i])

    except:
        showerror('Error','Somthing didn\'t go well :/')

def changecwd(dr,lst):             
    try:
        lst.delete(0,END)
        f.prevcwd.append(f.client.pwd())        #pwd内建函数，返回当前目录
        f.changecwd(dr)
        
        for i in range(len(f.curdata)):
            lst.insert(i,f.curdata[i])
            
    except:
        showerror('Error','Somthing didn\'t go well :/')

def prevcwd(lst):       #可以不要了
    try:
        dr = f.prevcwd[-1]
        lst.delete(0,END)
        f.prevcwd.remove(dr)
        f.changecwd(dr)
        
        for i in range(len(f.curdata)):
            lst.insert(i,f.curdata[i])
    except IndexError:
        showerror('Error','You alredy are in the home directory')
            
    except:
        showerror('Error','Somthing didn\'t go well :/')



def unpload(lst):      
    try:
       f.unpload()
       f.getcwd()
       lst.delete(0,END)
       for i in range(len(f.curdata)):
           lst.insert(i,f.curdata[i])
    except:
       showerror('Error','Somthing didn\'t go well :/')


def makedir(lst):
    try:
      f.mkdir()
      f.getcwd()
      lst.delete(0,END)
      for i in range(len(f.curdata)):
           lst.insert(i,f.curdata[i])
    except:
      showerror('Error','Somthing didn\'t go well')
       
Button(botframe,text='Download',command=lambda:f.download(data.get(data.curselection(),data.curselection())[0])).pack(side=LEFT)
Button(botframe,text='Unpload',command=lambda:unpload(data)).pack(side=LEFT)
Button(botframe,text='Change CWD',command=lambda:changecwd(data.get(data.curselection(),data.curselection())[0],data)).pack(side=LEFT)
Button(botframe,text='Previus CWD',command=lambda:prevcwd(data)).pack(side=LEFT)
Button(botframe,text='Create Directory',command=lambda:makedir(data)).pack(side=LEFT)
Button(botframe,text='Up Directory',command=lambda:changecwd('..',data)).pack(side=LEFT)
Button(conframe,text='Log in',command=lambda:conn(hosttext.get(),username.get(),password.get(),data)).pack(side=LEFT)
Button(conframe,text='Relog in',command=lambda:recon(data)).pack(side=LEFT)

root.mainloop()
