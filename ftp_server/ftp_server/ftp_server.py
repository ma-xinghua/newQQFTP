# __*__ coding:utf-8 __*__
import logging
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from config_ftp import *

#用户信息表，信息储存在userinfo中
user_list=[]  
def init_ftp_server():
    #用于FTPHandler类的管理员
    authorizer = DummyAuthorizer()    
    #读权限e：改变目录，l：列出文件，r：从服务器接收文件
	#写权限a：文件上传，d：删除文件，f：文件重命名，m：创建文件，w：写权限
    for user in user_list:
        name,passwd,permit,homedir = user      
        try:
            authorizer.add_user(name,passwd,homedir,perm=permit)
        except:
            print("配置文件错误请检查是否正确匹配了相应的用户名、密码、权限、路径")
            print(user)
    
    dtp_handler = ThrottledDTPHandler
    # 上传速度 下载速度
    dtp_handler.read_limit = max_download
    dtp_handler.write_limit = max_upload

    #创建服务器
    #handler用于处理接受到的命令，参数包括超时机制(300s)、最大登陆尝试（3）
    #handler = TLS_FTPHandler
    #handler.certfile = 'keycert.pem' 如果我们有证书的话，这就是证书地址，但是证书太贵了
    handler = FTPHandler
    handler.authorizer = authorizer   
    #是否打开记录
    if enable_logging:
        logging.basicConfig(filename=logging_name,level=logging.INFO)
    handler.masquerade_address = masquerade_address   #处理NAT时的私有地址和共有地址，这里即本机公网ip
    handler.passive_ports = range(passive_ports[0],passive_ports[1])    #被动连接
    server = FTPServer((ip,port),handler)
    server.max_cons = max_cons
    server.max_cons_per_ip = max_pre_ip
    server.serve_forever()

#处理user信息表中的信息
def ignor_octothrpe(txt):
    for x,item in enumerate(txt):
        if item == "#":
            return txt[:x]
        pass
    return txt

def init_user_config():
    f = open(user_config_file,encoding='utf-8')
    while True:
        line = f.readline()
        if len(ignor_octothrpe(line))>3:
            user_list.append(line.split())
        if not line:
            break

def ftp():   
     init_user_config()
     print ("QQFTP server has been launched!")
     init_ftp_server()
     
    