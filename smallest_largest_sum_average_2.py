#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: smallest_largest_sum_average_2.py
# Anthony Waldsmith
# 6/16/2016
# Python Version 3.4
# Description: A program that generates X random numbers of the users choice by console input

# Optional import for versions of python <= 2
from __future__ import print_function
import random
import sys

# Define function for integer inputting
def intInput(prompt):
	# While the input is invalid keep re-trying
	while True:
		# Try getting user input
		try:
			value = int(input(prompt))
		# Catch exception
		except ValueError:
			print ("That is not a whole number, try again")
			continue
		except NameError:
			print ("That is not a whole number, try again")
			continue
		except SyntaxError:
			print ("That is not a whole number, try again")
			continue

		# If the input is valid return (break)
		else:
			return value

print ()
amount = intInput("How many numbers would you like to enter?: ")
nums = []
doubled = []
smallest = 9999999
largest = 0
sum = 0

# Loop to the amount of random numbers
for i in range(amount):

	# Get user input for numbers
	num = intInput("Enter number %i: " %(i+1))

	# Set the current list object to num
	nums.append(num)

	# Set doubled amount to next list object
	doubled.append(num*2)

	# Set smallest number
	if (num < smallest):
		smallest = num

	# Set largest number
	if (num > largest):
		largest = num

# Create sum
for i in range(amount):
	# Add all values together
	sum += nums[i]

# Print answers
print ()
print ("You used a total of %i numbers: %s" %(amount,nums))
print ("Sum = %i" %(sum))
print ("Average = %i/%i = %.1f" %(sum,amount,float(sum/amount)))
print ("Smallest = %i" %(smallest))
print ("Largest = %i" %(largest))
print ("Doubled = %s" %(doubled))




"""
How many numbers would you like to enter?: 10
Enter number 1: -90
Enter number 2: 53
Enter number 3: 10
Enter number 4: 11
Enter number 5: 46
Enter number 6: 82
Enter number 7: 49
Enter number 8: -3
Enter number 9: s
That is not a whole number, try again
Enter number 9: 4
Enter number 10: 20

You used a total of 10 numbers: [-90, 53, 10, 11, 46, 82, 49, -3, 4, 20]
Sum = 182
Average = 182/10 = 18.0
Smallest = -90
Largest = 82
Doubled = [-180, 106, 20, 22, 92, 164, 98, -6, 8, 40]
"""
