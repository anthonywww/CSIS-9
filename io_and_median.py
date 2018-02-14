#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: io_and_median.py
# Anthony Waldsmith
# 08/01/2016
# Python Version 3.4
# Description: Random IO and get median

# Optional import for versions of python <= 2
from __future__ import print_function
import random


def generateRandomArray():
	array = []
	rand = random.randint(50,55);
	for i in range(0,rand+1):
		array += [random.randint(0, 100)]
	return array

def sortList(array):
	size = len(array)
	for i in range(size):
		for j in range(size-i-1):
			if (array[j] > array[j+1]):
				var = array[j]
				array[j] = array[j+1]
				array[j+1] = var
	return array

def countList(array):
	index = 0
	for i in array:
		index += 1
	return index

def helper():
	# Open and put data in file
	f = open("random.txt", "w")

	input_array = generateRandomArray()

	print("Random List: %s" %(input_array))

	for i in input_array:
		f.write("%i\n" %(i))

	# Close file operations
	f.close()



	# Open and read data from file
	f = open("random.txt", "r")
	# May throw casting exception if someone adds strings in here
	output_array = []

	# Read from file
	for line in f:
		output_array += [int(line)]

	# Close file operations
	f.close()

	sorted_array = sortList(output_array)
	print ("Sorted List: %s" %(sorted_array))
	middle = int(countList(sorted_array) / 2)

	if ((countList(sorted_array) % 2) == 0):
		print ("Is Even ... Averaging")
		n1 = sorted_array[middle-1]
		n2 = sorted_array[middle]
		avg = ((n1 + n2) / 2)
		return avg
	else:
		return sorted_array[middle]


def main():
	print("Median: %s" %(helper()))

main()


"""'
Random List: [86, 99, 85, 12, 33, 18, 36, 30, 22, 76, 63, 14, 79, 89, 31, 24, 82, 6, 64, 58, 93, 12, 83, 60, 100, 45, 35, 32, 55, 7, 60, 96, 9, 68, 44, 16, 3, 31, 3, 1, 14, 53, 15, 72, 99, 53, 92, 11, 10, 82, 42, 57, 22, 79, 31, 1]
Sorted List: [1, 1, 3, 3, 6, 7, 9, 10, 11, 12, 12, 14, 14, 15, 16, 18, 22, 22, 24, 30, 31, 31, 31, 32, 33, 35, 36, 42, 44, 45, 53, 53, 55, 57, 58, 60, 60, 63, 64, 68, 72, 76, 79, 79, 82, 82, 83, 85, 86, 89, 92, 93, 96, 99, 99, 100]
Is Even ... Averaging
Median: 43.0
"""
