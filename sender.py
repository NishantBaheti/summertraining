#!/usr/bin/python2
import socket
import time

rec_ip="127.0.0.1" #my ip ="192.168.10.197"
port=8881


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	x=raw_input("enter the msg please::::::")
	s.sendto(x,(rec_ip,port))
	#time.sleep(1)
	print s.recvfrom(100)


