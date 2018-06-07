#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders
import os


email_user="your gmail"
email_send="receiver's gmail"
subject= "dog"
passwd="passwd"
img_data=open('dog.jpeg','rb').read()
msg=MIMEMultipart()
msg['From']=email_user
msg['To']=email_send
msg['subject']=subject

body='hii there'
msg.attach(MIMEText(body,'plain'))

text=MIMEText("dog")
msg.attach(text)
image=MIMEImage(img_data,"dog.jpeg")
msg.attach(image)

text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user,passwd)


server.sendmail(email_user,email_send,text)
server.quit()


