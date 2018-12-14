# __*__ coding:utf-8 __*__

#本机绑定ip
ip = "0.0.0.0"
#本机绑定端口
port = "21"
#上传速度 300Kb/sec
max_upload = 500 * 1024
#下载速度 300Kb/sec
max_download = 500 * 1024
#最大连接数
max_cons = 256
#最多ip连接数
max_pre_ip = 10
#被动连接端口
passive_ports = (10200,10400)
#是否容许匿名访问
enable_anonymous = False
#是否打开日志记录
enable_logging = False
#日志记录文件名称
logging_name = r"pyftp.log"
#公网ip
masquerade_address = "192.168.3.8"
#默认匿名用户路径
anonymous_path = r"C:\\ftp"
#用户名配置文件
user_config_file = r"userinfo.ini"

