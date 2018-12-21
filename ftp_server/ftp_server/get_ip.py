import socket

def get_host_ip():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		ip = s.getsockname()[0]
	finally:
		s.close()
	file = open('config_ftp.py','r',encoding = 'UTF-8')
	array=file.readlines()
	file.close()

	i=0
	for line in array:
		if ('masquerade_address' in line):
			array[i]="masquerade_address = '" + ip + "'\n" 
		i=i+1
	file_new=open('config_ftp.py','w',encoding='UTF-8')
	for lines in array:
		file_new.write(lines)
	file_new.close()
	return ip


