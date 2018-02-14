#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: codingBat.py
# Anthony Waldsmith
# 07/20/16
# Python Version 3.4
# Description: A collection of Functions

# Optional import for versions of python <= 2
from __future__ import print_function

def main():
	# Main Method
	print()

#### FUNCTIONS ####

# Count utility function
def count(needle, haystack):
	counter = 0
	for i in range(len(haystack)):
		# Scan along the haystack for needle
		if (haystack[i:i + len(needle)] == needle):
			# Increment by 1 if found
			counter += 1
	return counter

# Multiply a string n amount of times
def string_times(str, n):
	result = ""
	for i in range(abs(n)):
		# Normally I would also do + " " to add a space at the end, but the instructions said to not add extra spaces.
		result = result + str
	return result

def extra_end(str):
	# Basically call the string_timems() function with the parameter of a substring "length-2", and a second parameter telling the function to repeat it 3 times.
	return string_times(str[-2:], 3)

def make_tags(tag, str):
	# The correct term is called XML Stringification. (Gnerically this is XML not HTML, because we're talking about the generic type)
	return ("<" + tag + ">" + str + "</" + tag + ">")

def combo_string(a, b):
	# Just append the strings as "short" "long" "short"
	if (len(a) > len(b)):
		return (b + a + b)
	else:
		return (a + b + a)


def count_code(str):
	inc = 0
	for i in range(33, 127):
		d = chr(i)
		if ("co" + d + "e" in str):
			inc += count("co" + d + "e", str)

	return inc



def xyz_there(str):
	value = False
	if (count("xyz",str) > 0):
		value = True
		if (count(".xyz",str) > 0):
			value = False
			if(str.endswith("xyz") and not str.endswith(".xyz")):
				value = True
	else:
		value = False
	return value


# Call main
main()
