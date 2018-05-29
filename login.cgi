#!/usr/bin/python3

import cgi
import cgitb
import mysql.connector as msql
cgitb.enable()


print("content-type:text/html")
print ("")
 	

conn=msql.connect(user='root',password='1234',host='localhost',database='nishant')
cur=conn.cursor()
def db():
	try:
		if conn.is_connected():
			print("database connected")
	except:
		print("not connected")
	
if __name__=='__main__':
	db()


data=cgi.FieldStorage()

name=data.getvalue('n')
email=data.getvalue('e')
password=data.getvalue('p')
contact=data.getvalue('c')
print(name)	
print(email)
print(password)
print(contact)

add_user=("insert into login"
	  "(name,email,password,contact)"
	  "values(%s,%s,%s,%s)")

data_user=(name,email,password,contact)

cur.execute(add_user,data_user)

conn.commit()
cur.close()
conn.close()

























