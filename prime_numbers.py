#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: prime_numbers.py
# Anthony Waldsmith
# 07/12/2016
# Python Version 3.4
# Description: Print out prime numbers between 3 to 100.

# Optional import for versions of python <= 2
from __future__ import print_function

# Loop between 3(start) to 100(end)
for i in range(3,100):
	# Nested loop, check every integer that can be divisible (n-1)
	for j in range(2,i-1):
		if (i % j == 0):
			# Number is not prime, break out of this loop
			break;
		if (i % j != 0 and j == i-2):
			# Number is prime
			print(i)

"""
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
"""
