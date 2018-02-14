#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: longer_program.py
# Anthony Waldsmith
# 07/25/2016
# Python Version 3.4
# Description:

# Optional import for versions of python <= 2
from __future__ import print_function

def isTriangle(a, b, c):
	if ((a + b > c) and (a + c > b) and (c + b > a)):
		return True
	else:
		return False

def isEquiladeral(a, b, c):
	if (a == b):
		if (b == c):
			return True
	return False

def isIsosceles(a, b, c):
	if(a == b):
		if(a != c and b != c):
			return True
	if(a == c):
		if(a != b and b != c):
			return True
	return False

def isRight(a, b, c):
	if((a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (c**2 + b**2 == a**2)):
		return True
	return False

def compute(a, b, c):
	if isTriangle(a, b, c) == False:
		return "not a triangle"
	else:
		if isIsosceles(a, b, c) == True:
			return "a isosceles triangle!"
		elif isEquiladeral(a, b, c) == True:
			return "a equilateral triangle!"
		elif isRight(a, b, c) == True:
			return "a right triangle!"
		else:
			return "a another type of triangle."

def main():
	running = True
	while running:
		while True:
			try:
				a = int(input("Enter side a: "))
				b = int(input("Enter side b: "))
				c = int(input("Enter side c: "))
				if (a < 0 or b < 0 or c < 0):
					print ("All values must be positive, try again.")
					continue
			except ValueError:
				print ("Sorry, I didn't understand that, try again.")
				continue
			else:
				break

		print ("This is %s" %(compute(a, b, c)))

		while True:
			text = input("Run again? [Y/N]: ")
			if (text == 'y' or text == 'Y'):
				break
			elif (text == 'n' or text == 'N'):
				running = False
				break
			else:
				continue

# Call Main
main()


"""
Enter side a: 1
Enter side b: 2
Enter side c: 3
This is not a triangle
Run again? [Y/N]: y
Enter side a: 2
Enter side b: 2
Enter side c: 1
This is a isosceles triangle!
Run again? [Y/N]: y
Enter side a: 3
Enter side b: 4
Enter side c: 5
This is a right triangle!
Run again? [Y/N]: y
Enter side a: 1
Enter side b: 1
Enter side c: 1
This is a equilateral triangle!
Run again? [Y/N]: y
Enter side a: 39
Enter side b: 183
Enter side c: 4
This is not a triangle
Run again? [Y/N]: n
"""
