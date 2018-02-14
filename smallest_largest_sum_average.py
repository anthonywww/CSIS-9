#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: smallest_largest_sum_average.py
# Anthony Waldsmith
# 6/16/2016
# Python Version 3.4
# Description: A program that generates X random numbers (between 10 to 15) (integers) and those random numbers are between 20 to 50

# Optional import for versions of python <= 2
from __future__ import print_function
import random
import sys

# A random int between 10 and 15
amount = random.randint(10,15)
randomnums = []
smallest = 9999
largest = 0
sum = 0

# Loop to the amount of random numbers
for i in range(amount):
	# Generate random number and set as variable num to use in this for loop
	num = random.randint(20,50)

	# Set the current list object to num
	randomnums.append(num)

	# Set smallest number
	if (num < smallest):
		smallest = num

	# Set largest number
	if (num > largest):
		largest = num

# Create sum
for i in range(amount):
	# Add all values together
	sum += randomnums[i]


# Print answers
print ("Generated %i random numbers: %s" %(amount,randomnums))
print ("Sum = %i" %(sum))
print ("Average = %i/%i = %.1f" %(sum,amount,float(sum/amount)))
print ("Smallest = %i" %(smallest))
print ("Largest = %i" %(largest))


"""
Generated 14 random numbers: [50, 49, 47, 32, 22, 49, 48, 39, 27, 45, 26, 29, 23, 37]
Sum = 523
Average = 523/14 = 37.0
Smallest = 22
Largest = 50
"""
