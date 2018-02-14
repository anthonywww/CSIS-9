#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: absolute_value.py
# Anthony Waldsmith
# 07/14/2016
# Python Version 3.4
# Description: Absolute value function.

# Define function
def abVal(num):
	# If the value is < 0 then the number is negative, so invert it by multiplying by -1
	if(num < 0):
		return (num * -1)
	else:
		return (num)





print (abVal(-28))
print (abVal(-255))
print (abVal(12))

"""
28
255
12
"""
