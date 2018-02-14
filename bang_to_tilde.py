#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: bang_to_tilde.py
# Anthony Waldsmith
# 6/16/2016
# Python Version 3.4
# Description: Prints ASCII values from 33 (bang) to 126 (tilde) (two of my favorite ASCII characters)

# Optional import for versions of python <= 2
from __future__ import print_function

# Initialize variables
count = 0

# While the ascii count hasn't reached tilde (~) yet, then continue. (Starts at bang (!))
for value in range(33, 127):

	# Print character on same line
	print (chr(value), end = ' ')

	# Increment counters
	count += 1

	# If the count is past 10 characters, then create new line
	if (count >= 10):
		count = 0
		print ()

# Add a new line at the end of the program
print ()


"""
! " # $ % & ' ( ) *
+ , - . / 0 1 2 3 4
5 6 7 8 9 : ; < = >
? @ A B C D E F G H
I J K L M N O P Q R
S T U V W X Y Z [ \
] ^ _ ` a b c d e f
g h i j k l m n o p
q r s t u v w x y z
{ | } ~
"""
