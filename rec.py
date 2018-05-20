#!/usr/bin/python2
import socket


rec_ip="127.0.0.1" #rec_ip
my_port=8881   #5000+ port number will be free most of the time



#socket function in the socket library imported earlier

#we are using           ipv4,           UDP   
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
#for                  tcp       DGRAM  <-> STREAM

#binding ip and port
s.bind((rec_ip,my_port))

#buffersize 
while True:
	data=s.recvfrom(100)
	print "data from client,",data[0]
	#print "ip of client ,",data[1][0]
	reply=raw_input("enter your reply    :")
	s.sendto(reply,data[1])
