import ftplib 
import os,socket 
import threading
# -*- coding: utf-8 -*-


class FTPClient: 
    def __init__(self): 
        self.curDir = "/"     #当前文件夹名
        self.cursize = 0  

    def ListFile(self):    #列出所有文件
        self.ftp.encoding = 'utf-8 '
        self.ftp.dir(self.curDir)
        pass  

    def Connect(self,host):    #建立连接
        try: 
            self.ftp = ftplib.FTP(host) 
            
        except (socket.error, socket.gaierror) as e: 
            print("Er#ror:cannot reach%s" % (host)) 
            return  
        print("Conneted host:", host)  

    def Login(self,user,password):      
        try: 
            self.ftp.login(user, password) 
        except ftplib.error_perm: 
            print("Error: cannot login anonymously") 
            
            return 
        print("logined as ", user) 
        self.ListFile()  

    def EnterDir(self,dirname):        #输入文件夹名
        try: 
            #change dir 
            self.curDir = self.curDir+"/"+dirname 
            self.ftp.cwd(self.curDir)      #内置函数，进入另一个文件夹
        except ftplib.error_perm: 
            print("Error: cannot CD into %s" % (self.curDir))
            
            
            return 
        print("Changed into %s folder" % (self.curDir))  

    def DownloadFile(self, filename): 
        try: 
            #local file 
            self.cursize = 0 
            filehandle = open(filename, "wb") 
            #remote file 
           
            self.totalsize = os.path.getsize(filename)  
           
            #define callback 
            chunkwrite = lambda chunk: self.ChunkWrite(chunk, filehandle)   #chunkwrite显示下载进度
           
            self.ftp.retrbinary("RETR %s" % (filename), filehandle.write)    #内置函数，下载文件
            print("….Download “%s” to Local" % (filename))
        except ftplib.error_perm:  
            print("Error: cannot read file %s" % (filename)) 
              
        filehandle.close() 
          

    def UPLoadFile(self, filename): 
        try: 
            #local 
            self.cursize = 0
            filehandle = open(filename, "rb") 
            self.totalsize = os.path.getsize(filename)  
            #remote 
            pathFormat = filename.split("\\") 
            remotefile = pathFormat[len(pathFormat) - 1]  
            self.ftp.storbinary("STOR %s" % (remotefile),filehandle, 1024,self.ChunkRead)    #内置函数，上传文件，chunkread显示上传进度
            print("….UpLoad “%s” to FTP" % (filename))
            filehandle.close() 
        except IOError:
            print("Error: cannot read file %s" % (filename)) 
        except ftplib.error_perm:  
            print("Error: cannot read file %s" % (filename)) 
        
        
        

   
    def ChunkWrite(self,chunk, filehandle):  
        # calc process 
        self.cursize = self.cursize + len(chunk) 
        process = self.cursize*100 / self.totalsize
        print(str(round(process, 3))+"%",end = "\r")  
        #save data to local 
        filehandle.write(chunk)  


    def ChunkRead(self, chunk):  
        #calc process 
        self.cursize = self.cursize + len(chunk) 
        process = self.cursize * 100 / self.totalsize 
        print(str(round(process, 3)) + "%",end="\r")  
        

    def Disconnect(self): 
        try: 
            self.ftp.quit() 
        except (socket.error, socket.gaierror) as e: 
            print(e)

class CustomConsole(threading.Thread): 
    def __init__(self): 
        self.cmd = "" 
        threading.Thread.__init__(self)  


    def run(self):  
        print("*********Command Usaged************") 
        print("***conn :Connect to ftp server*****") 
        print("***login:Login ftp server**********") 
        print("***ls:List files and directories***") 
        print("***cd:Change directory*************") 
        print("***put:Upload File to ftp server***") 
        print("***get:Download from ftp server****") 
        print("***quit:disconnect with ftp server*")  

        while(True): 
            cmd = input("Please input command:") 
            if(cmd == "quit"): 
                self.ftp.Disconnect() 
                break  

            if (cmd == "conn"): 
                serverip = input("Please input server ip:") 
                self.ftp = FTPClient() 
                self.ftp.Connect(serverip)  

            if (cmd == "login"): 
                username = input("Please input username:") 
                password = input("Please input password:") 
                self.ftp.Login(username,password)  

            if(cmd == "ls"): 
                files = self.ftp.ListFile()  

            if (cmd == "cd"): 
                files = self.ftp.ListFile() 
                subdir = input("Please input subdir:") 
                self.ftp.EnterDir(subdir)  

            if (cmd == "get"): 
                filename = input("Please input filename:") 
                self.ftp.DownloadFile(filename)  

            if (cmd == "put"): 
                filename = input("Please input filename:") 
                self.ftp.UPLoadFile(filename)




if __name__ == '__main__': 

    c = CustomConsole() 
    c.start()
    c.join()
    
