#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: mult_add.py
# Anthony Waldsmith
# 07/14/2016
# Python Version 3.4
# Description: A function that takes in 3 parameters (a,b,c) and does the following operation a*b+c

# multAdd function
def multAdd(a,b,c):
	return ((a*b)+c)



# Main function
def main():
	a = 6
	b = 10
	c = 4
	print("Num 1 = %i, Num 2 = %i, Num 3 = %i; Answer: %i" %(a,b,c,multAdd(a,b,c)))

main()

"""
Num 1 = 6, Num 2 = 10, Num 3 = 4; Answer: 64
"""
