#!/usr/bin/env python

import webbrowser #import webbrowser module
import time #import time module
from random import randint #import randint to generate random intiger no

print "The program started at %s" % time.ctime()

# This is the list of 6 random music form youtube URL (0-5) which will be played every 10 sec

music = ['https://www.youtube.com/watch?v=w--g30WTfBs', 'https://www.youtube.com/watch?v=BWLYFc9MDFI', 'https://www.youtube.com/watch?v=aE79diaYIww', 'https://www.youtube.com/watch?v=KHrvjVxXRhU', 'https://www.youtube.com/watch?v=w5e66arTahc', 'https://www.youtube.com/watch?v=GvK5ZVFju1I' ]

def play_music(music):
	random_music = randint(0, 5) #Generate random no of int values from 0-5
	webbrowser.open(music[random_music])


break_no = 3
break_count = 0

while break_count < 3:
	
	time.sleep(10)    #Pause the Music 10 Sec after starting the program
	play_music(music) #Play Music by calling music function
	break_count += 1  # Increase break_count by 1 after playing music




