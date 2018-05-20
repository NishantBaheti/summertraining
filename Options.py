#!/usr/bin/python2
import time
import webbrowser
option ='''
press 1: to enter an thing -split each word and search it on google
press 2: same but find url
press 3: same but find images answer
press 4: current time and date
press 5: opwn default browser
press 6: all network IP
press 7: enter domain name and find owner
'''
print option  #useful to print multiple option /lines

ch=raw_input()

#webbrowser.open("my name is nishant")
if  ch == '1' :
	search_data=raw_input("enter data...-")
	final_data=search_data.strip()
	#removing leading and trailing spaces
	done_data=final_data.split()
	#spliting each word in given input
	#print done_data
	for i in done_data:
		#print i
		#time.sleep(2)
		webbrowser.open_new_tab('http://www.google.com/search?q='+i)
		#will go in the location or try to open a file so http url should be given
		#search content will be saved in a variable q

