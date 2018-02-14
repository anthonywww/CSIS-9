#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: is_triangle.py
# Anthony Waldsmith
# 07/14/2016
# Python Version 3.4
# Description: A function that checks if a triangle can be formed with the following parameters (a, b, c)
import random

# isTriangle function
def isTriangle(a,b,c):
	# Check if the lengths are less-than or equal to two other sides.
	if (a <= (b+c)) and (b <= (a+c)) and (c <= (a+b)):
		return True
	else:
		# Otherwise it's not a triangle
		return False


# Main function
def main():
	# Set side values to random nums
	a = random.randint(0,256)
	b = random.randint(0,256)
	c = random.randint(0,256)

	# Set default string value
	s = "does NOT"

	# Change string value if it's a triangle
	if (isTriangle(a,b,c)):
		s = "DOES"

	# Print final values
	print ("Side 1 = [%i], Side 2 = [%i], Side 3 = [%i]; this %s make a triangle" %(a,b,c,s))

main()

"""
Side 1 = [114], Side 2 = [10], Side 3 = [9]; this does NOT make a triangle
Side 1 = [4], Side 2 = [176], Side 3 = [225]; this does NOT make a triangle
Side 1 = [175], Side 2 = [53], Side 3 = [212]; this DOES make a triangle
Side 1 = [132], Side 2 = [187], Side 3 = [117]; this DOES make a triangle
Side 1 = [143], Side 2 = [124], Side 3 = [85]; this DOES make a triangle
"""
