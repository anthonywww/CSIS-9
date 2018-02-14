#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: tuition_table.py
# Anthony Waldsmith
# 6/16/16
# Python Version 3.4
# Description: Computes the tuition for 10 years of a university that is $10,000 initially and increases 5% each year

# Optional import for versions of python <= 2
from __future__ import print_function
import time

cost = 10000

for year in range(1,11):
	print ("Year %i\t Tuition %i" %(year,cost))
	cost = cost * 1.05
	time.sleep(0.03)



"""
Year 1	 Tuition 10000
Year 2	 Tuition 10500
Year 3	 Tuition 11025
Year 4	 Tuition 11576
Year 5	 Tuition 12155
Year 6	 Tuition 12762
Year 7	 Tuition 13400
Year 8	 Tuition 14071
Year 9	 Tuition 14774
Year 10	 Tuition 15513
"""
