# -*- coding: utf-8 -*-
# Program Name: compute_height.py
# Anthony Waldsmith
# 6/15/2016
# Python Version 3.4
# Description: Take user input of two numbers, one of feet, one of inches, and compute the inches total

# Optional import for versions of python <= 2
from __future__ import print_function


# Do this until valid input is given
while True:

	try:
		# This takes in first number and casts to integer
		feet = int(input("Please enter the number of feet: "))
		# This takes in second number and casts to integer
		inches = int(input("Please enter the number of inches: "))
	except ValueError:
		# If there is invalid input (casting exception)
		# Show the user this text in console, then continue the loop
		print("Sorry, I didn't understand that, try again.")
		continue

	else:
		# The value was successfully parsed
		# So break out of the loop
		break


# Do calculations, convert feet to inches, then add inches together
inches2 = (feet * 12)
ans = (inches + inches2)


# Print out answer
print("%i feet %i inch(es) = %i inches" %(feet,inches,ans))


"""
Please enter the number of feet: 6
Please enter the number of inches: 2
6 feet 2 inch(es) = 74 inches
"""
