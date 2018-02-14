#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: indexes.py
# Anthony Waldsmith
# 07/27/2016
# Python Version 3.4
# Description: Show the current index where a word appears in a list

def indexes(array, match):
	count = 0
	array2 = []
	for s in array:
		if s == match:
			array2 += [count]
		count += 1
	return array2


def main():
	array = ['one','two','two','three','five','four','two']
	print (indexes(array,'two'))

main()

"""'
[1, 2, 6]
"""
