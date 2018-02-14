#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: penny_or_million_dollars.py
# Anthony Waldsmith
# 6/16/16
# Python Version 3.4
# Description: Computes weither a penny or a million dollars is worth more in 30 days if the penny doubles in value each day

# Optional import for versions of python <= 2
from __future__ import print_function
import time

# Set variables
million = 100000
penny = 1
days = 30
tab = "\t"

# Print header
print ()
print ("\t\tPenny\t|\tMillion $")
print ("-"*23,"+","-"*23)

# Itterate over days to 30
for day in range(days):

	# Tab spacing
	if (penny > 16777200):
		tab = ""
	else:
		tab = "\t"

	# Print table
	print ("Day %i:\t%i\t%s|\t%i" %(day+1,penny,tab,million))

	# Increment
	penny *= 2
	time.sleep(0.03)

print ()
print ("I'd pick the penny!")



"""

		Penny	|	Million $
----------------------- + -----------------------
Day 1:	1		|	100000
Day 2:	2		|	100000
Day 3:	4		|	100000
Day 4:	8		|	100000
Day 5:	16		|	100000
Day 6:	32		|	100000
Day 7:	64		|	100000
Day 8:	128		|	100000
Day 9:	256		|	100000
Day 10:	512		|	100000
Day 11:	1024		|	100000
Day 12:	2048		|	100000
Day 13:	4096		|	100000
Day 14:	8192		|	100000
Day 15:	16384		|	100000
Day 16:	32768		|	100000
Day 17:	65536		|	100000
Day 18:	131072		|	100000
Day 19:	262144		|	100000
Day 20:	524288		|	100000
Day 21:	1048576		|	100000
Day 22:	2097152		|	100000
Day 23:	4194304		|	100000
Day 24:	8388608		|	100000
Day 25:	16777216	|	100000
Day 26:	33554432	|	100000
Day 27:	67108864	|	100000
Day 28:	134217728	|	100000
Day 29:	268435456	|	100000
Day 30:	536870912	|	100000

I'd pick the penny!
"""
