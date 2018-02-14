#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: sort_list.py
# Anthony Waldsmith
# 07/27/2016
# Python Version 3.4
# Description: Sort a array list

# Optional import for versions of python <= 2
from __future__ import print_function

def sortList(array):
	size = len(array)
	for i in range(size):
		for j in range(size-i-1):
			if (array[j] > array[j+1]):
				var = array[j]
				array[j] = array[j+1]
				array[j+1] = var
	return array

def reverseSortList(array):
	size = len(array)
	for i in range(size):
		for j in range(size-i-1):
			if (array[j] > array[j-1]):
				var = array[j]
				array[j] = array[j-1]
				array[j-1] = var
	# Prepend to array last object
	array = [array[len(array)-1]] + array[:-1]
	return array

# A function that sorts a list in either smallest to greatest or if reversed, greatest to smallest.
def sort(array, reverse):
	array2 = []
	init = False
	for i in array:
		if not reverse:
			array2 = sortList(array)
		else:
			array2 = reverseSortList(array)
	return array2


def main():
	array = [2,7,3,1,4,51,18,-2]
	print (sort(array, True))

main()

"""'
[51, 18, 7, 4, 3, 2, 1, -2]
"""
