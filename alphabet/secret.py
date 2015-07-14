#!/usr/bin/env python

import os
from os import path
from string import digits

#Getting the file name from the directory

files_name = os.listdir('./')  #List all the files and directories from the current directory

for file_name in files_name:
	if path.isfile(file_name): #Check whether the component is File or directory if File it will rename
		os.rename(file_name, file_name.translate(None, digits)) #Rename the file and revel the secret message
		
