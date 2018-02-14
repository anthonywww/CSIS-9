#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: stars.py
# Anthony Waldsmith
# 7/11/2016
# Python Version 3.4
# Description: Display amount of stars depending on variable

# Optional import for versions of python <= 2
from __future__ import print_function

# Number of stars
stars = 10

# Character to use, for example ツ
char = "+"

# For each of the stars
for i in range(stars):
	# For each of the stars on "this" line that will appear
	for j in range(i):
		# Print the character, change the line ending to a space rather than \n (new line)
		print (char, end=' ')
	# Print a new line at the end of each loop of "this" line
	print ("")

"""
+ 
+ + 
+ + + 
+ + + + 
+ + + + + 
+ + + + + + 
+ + + + + + + 
+ + + + + + + + 
+ + + + + + + + + 
"""
