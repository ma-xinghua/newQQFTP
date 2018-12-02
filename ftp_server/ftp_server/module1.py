from ftp_server import *

def collect_info():
    account = input("your Account: ")
    password = input("your password: ")
    authority = input("a for load, b for all, your authority: ")
    path = input("your path: ")
    file = open('userinfo.ini', 'a')
    if authority=='a':
        word = '\n'+account+' '+password+' '+"elr"+' '+path
    elif authority=='b':
        word = '\n'+account+' '+password+' '+"elradfmwMT"+' '+path
    file.write(word)
    file.close()

def main():
    ans = input("Do you want to write your info? y/n")
    if ans=='y':
        collect_info()
    ftp()
  
    
main()