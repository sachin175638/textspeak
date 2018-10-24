#!/bin/env python2
#script owner = sachin

import os

try:
 from gtts import gTTS
except ImportError:
 os.system("pip2 install gTTS")

logo = '''
\t\t \033[1;31m=======================
\t\t |\033[1;32mText to mp3 converter\033[1;31m|
\t\t =======================\033[1;39m
\t\t Type: help
'''
print logo

def h():
  help = '''\033[1;33m
 \t Commands        Description

 \t set file        set file /< File path> /file.txt
 \t save mp3        save mp3 /< Destination path >/file
 \t clear           clear screen
 \t convert         converting text into mp3
 \t exit            exiting the program\033[1;39m
                '''
  print help

def cl():
	 os.system("clear")
y = ""
file =""
mp3 =""
print ""
while True:
#	print ''
	man = raw_input("\033[1;39mText-speak\033[1;32m >>\033[1;39m ")
	main = man.split()
	if not main:
		print "<\033[1;31minvalid command\033[1;39m>"
		continue
	elif main[0] == "help":
		h()
	elif main[0] == "exit":
		break
	elif main[0] == "clear":
		cl()
	elif main[0] == "set":
		 if main[1] == "file": 
		  file = str(main[2])
		  if file != "":
		     try:
		  	sachin = file
 		  	x = open(sachin, "r")
 		  	y = x.read()
 		  	x.close()
	             except IOError:
        	  		print "[x] No such a file or directory",file
				file = ""
	elif main[0] == "save":
		if main[1] == "mp3":
 		 mp3_path = str(main[2])
		 mp3 = mp3_path+".mp3"
		 if os.path.exists(mp3):
		 	print "[x] This file name already exists"
			mp3 = ""
	elif main[0] == "show":
		if main[1] == "options":
		 print "\033[1;33m"
		 print "\t Input optins"
		 print ''
		 print "\t File path : ",file
		 print "\t Saved to  : ",mp3
		 print "\033[1;39m"
	elif main[0] == "convert":
		print "\033[1;32m Converting ... "
		print ''
		print "\033[1;32m\t--==="+file+"===---\033[1;39m"
		print y
		print ''
		if file == "":
			print "\033[1;39m[\033[1;31mx\033[1;39m] No input found"
			print ""
			continue
		if mp3 == "":
			print "\033[1;39m[\033[1;31mx\033[1;39m] No input found "
			print ""
			continue
		try:
 		  try:
  		    tts = gTTS(text=y, lang="en")
  	            tts.save(mp3)
 		  except connection:
  		    pass
		except NameError:
 		   print "\033[1;39m[\033[1;31mx\033[1;39m] Please check your  internet connection"
 		   print ''
		   os.remove(mp3)


		if os.path.exists(mp3):
        		print ""
        		print "\033[1;39mmp3 file generated in this path \033[1;32m",mp3
        		print "\033[1;39m"
	else:
		print "<\033[1;31minvalid command\033[1;39m>"


