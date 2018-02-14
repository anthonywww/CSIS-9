#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: short_programs.py
# Anthony Waldsmith
# 07/25/2016
# Python Version 3.4
# Description: Write the following two functions, and test them (show output)

# Optional import for versions of python <= 2
from __future__ import print_function

# Arguments are type float (distance, time)
def speed(distance, time):
	return ("%.2f" %(distance/time))

# Arguments are type int, returns the bigger number
def bigger(num1, num2):
	if (num1 > num2):
		return num1
	else:
		return num2


def main():
	# Test program
	print(speed(51, 34.5))
	print(bigger(3, 16))


main()
