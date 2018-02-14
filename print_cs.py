# -*- coding: utf-8 -*-
# Program Name: print_cs.py
# Anthony Waldsmith
# 6/13/2016
# Python Version 2.7
# Description: Program to print "CS" ASCII-PUNK style

# Must import print_function because I didn't update to Python 3.x yet.
from __future__ import print_function

# Imports extra utilities that I used to spice up the text print
import time
import sys

# Here I defined a function with a parameter text
def coolprint(text):
	# Here it takes each letter (character) from text and sets it to the variable char
	for char in text:
		# Here we add a short delay
		time.sleep(0.01)
		# This is essentially the same as print ("text",end=' ') however that function does not handle spaces very well.
		# so using this function deeper in python allows me to directly write each character individually.
		sys.stdout.write(char)
		# This pushes the text out to the stdout stream (in this case the console is the output)
		sys.stdout.flush()

print ("*"*55)
coolprint ("                CCCCCC         SSSS            \n")
coolprint ("               C              S    S           \n")
coolprint ("              C              S                 \n")
coolprint ("             C               S                 \n")
coolprint ("            C                 SSSSS            \n")
coolprint ("             C                     S           \n")
coolprint ("              C                     S          \n")
coolprint ("               C             S     S           \n")
coolprint ("                CCCCC         SSSSS            \n")
print ("*"*55)
print ("\n")
coolprint ("Computer Science is Cool Stuff!\n")


'''
*******************************************************
                CCCCCC         SSSS            
               C              S    S           
              C              S                 
             C               S                 
            C                 SSSSS            
             C                     S           
              C                     S          
               C             S     S           
                CCCCC         SSSSS            
*******************************************************


Computer Science is Cool Stuff!

'''
