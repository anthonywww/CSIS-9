#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: codingBat_2.py
# Anthony Waldsmith
# 07/23/16
# Python Version 3.4
# Description: A collection of Functions 2

# Optional import for versions of python <= 2
from __future__ import print_function

def main():
	# Main Method
	print()
	big_diff([10, 3, 5 , 6])

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

def smallest(nums):
	smallest = 9999
	for i in nums:
		if (i < smallest):
			smallest = i
	return smallest


def largest(nums):
	largest = -9999
	for i in nums:
		if (i > largest):
			largest = i
	return largest


def sortList(array):
	size = len(array)
	for i in range(size):
		for j in range(size-i-1):
			if (array[j] > array[j+1]):
				var = array[j]
				array[j] = array[j+1]
				array[j+1] = var
	return array

def centered_average(nums):
	amount = len(nums)
	# Not using min() , max(), sort(), sorted(), or reduce()
	# Sorting and trimming
	array = sortList(nums)
	array = array[1:-1]
	total = 0
	for i in array:
		total += i
	total = (total / amount)
	return total

def big_diff(nums):
	minimum = smallest(nums)
	maximum = largest(nums)
	#print ("Min: %i" %(minimum))
	#print ("Max: %i" %(maximum))
	return (maximum - minimum)

# Call main
main()
