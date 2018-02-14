#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: sum_double.py
# Anthony Waldsmith
# 07/14/2016
# Python Version 3.4
# Description: Sum or sum and double the values if input values are the same as a function


# Define function take in 2 parameters (num1, num2)
def sum_double(v1, v2):
	# If the two numbers values are equal sum and multiply by 2
	if (v1 == v2):
		ans = (v1 + v2)
		ans *= 2
		return ans
	else:
		# Otherwise just return the sum
		return (v1 + v2)


print (sum_double(2,3))
print (sum_double(2,2))
print (sum_double(20,3))
print (sum_double(6,-15))
print (sum_double(-10,-5))

"""
5
8
23
-9
-15
"""
