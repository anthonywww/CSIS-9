#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: is_divisible.py
# Anthony Waldsmith
# 07/14/2016
# Python Version 3.4
# Description: A function that checks if two numbers are evenly divisible

# Define function take in 2 parameters if N is cleanly divisible by m (n, m)
def isDivisible(n, m):
	# Modulus
	if (n % m == 0):
		return True
	else:
		return False

print ("4 is evenly divisible by 5: ", isDivisible(4,5))
print ("10 is evenly divisible by 2: ", isDivisible(10,2))

"""
4 is evenly divisible by 5:  False
10 is evenly divisible by 2:  True
"""
