#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: count_letters_in_sentence.py
# Anthony Waldsmith
# 6/16/2016
# Python Version 3.4
# Description: Count and display how many times two letter are used in a sentance/input

# Optional import for versions of python <= 2
from __future__ import print_function

# Initialize variables
text = ""
letter1 = ""
letter2 = ""
count1 = 0
count2 = 0

# Get inputs
text = input("Please enter a sentence: ")
letter1 = input("Please enter first letter: ")
letter2 = input("Please enter second letter: ")

# For each character in text
for char in text:
	if (char == letter1):
		count1 += 1
	if (char == letter2):
		count2 +=1

print ()
print ("Letter 1 (%s) occures %i time(s)" %(letter1, count1))
print ("Letter 2 (%s) occures %i time(s)" %(letter2, count2))

"""
Please enter a sentence: hello world!
Please enter first letter: l
Please enter second letter: d

Letter 1 (l) occures 3 time(s)
Letter 2 (d) occures 1 time(s)
"""
