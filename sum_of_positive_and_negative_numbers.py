#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: sum_of_positive_and_negative_numbers.py
# Anthony Waldsmith
# 6/16/16
# Python Version 3.4
# Description: Sums of positive and negative numbers with a repeat ability

# Optional import for versions of python <= 2
from __future__ import print_function

# This function is for safely getting input of a integer type, returns an integer
def intInput(prompt):
	while True:
		try:
			# Get input
			val = int(input(prompt))
		except ValueError:
			# If there is invalid input (casting exception)
			# Show the user this text in console, then continue the loop
			print("Sorry, I didn't understand that, try again.")
			continue
		else:
			# The value was successfully parsed
			# So, break out of the loop and return value
			break
	return val



# BEGIN looping here
while True:
	# Get int input for how many numbers to request
	amt = intInput("How many numbers would you like to enter?: ")
	nums = []
	total = 0
	negnums = 0
	posnums = 0

	while (amt < 1):
		amt = intInput("You must pick a number greater than 0")

	# For loop for each itteration (for input)
	for itteration in range(amt):
		nums.append(intInput("Enter value for number %i: " %(itteration+1)))
		#print (list(nums))
		total += nums[itteration]
		if(nums[itteration] < 0):
			negnums += nums[itteration]
		else:
			posnums += nums[itteration]

	# Finally print
	print ("----")
	print ("The sum of negative numbers = %i" %(negnums))
	print ("The sum of positive numbers = %i" %(posnums))
	print ("The total sum of all numbers = %i" %(total))

	while True:
		# Get input for retry
		redo = input("Would you like to repeat? [Y/N]: ")

		# If the value is not 'y' or 'n' re-ask question
		if (redo.lower() == "n" or redo.lower() == "no"):
			exit()
		else:
			if(redo.lower() != "y" and redo.lower() != "yes"):
				continue
			else:
				break



"""
How many numbers would you like to enter?: 5
Enter value for number 1: -1
Enter value for number 2: 20
Enter value for number 3: 3
Enter value for number 4: 18
Enter value for number 5: -6
----
The sum of negative numbers = -7
The sum of positive numbers = 41
The total sum of all numbers = 34
Would you like to repeat? [Y/N]: h
Would you like to repeat? [Y/N]: n
"""
