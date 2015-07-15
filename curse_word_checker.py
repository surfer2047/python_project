#!/usr/bin/env python
#Author: @nix1947
#Description: Take the file input from the current working directory and check the curse words into that file, if curse word exist, It will return True, else return false

from urllib import urlopen
from sys import exit

def check_curse_word(content):
	connection = urlopen("http://www.wdyl.com/profanity?q="+content)
	boolean = connection.read() #Return the string {"response": "false"} if no curse word, {"response": "true"}, if curse word

	if "false" in boolean:
		print "Doesn't contain CURSE word"
	elif "true" in boolean:
		print "Contain CURSE  word"
	else:
		exit(1)
	connection.close()  #Close the connection

def read_word(file_name):
	file_object = open(file_name, 'r') 	 # Create the file object for operation
	content = file_object.read()      	 #read the content of file
	check_curse_word(content)        	 #Check for curse word by calling check_curse_word() function
	file_object.seek(0)			 #Set the pointer to initial position
	file_object.close() #Close the file

	

read_word("movie_quotes.txt")
