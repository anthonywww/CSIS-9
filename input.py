# -*- coding: utf-8 -*-
# Program Name: input.py
# Anthony Waldsmith
# 6/15/2016
# Python Version 3.4
# Description: Program to take user input from console

# Optional import for versions of python < 3
from __future__ import print_function


# Set predefined variables
title = "Human"



# Do this until valid input is given
while True:

	try:
		# This takes in a string
		name = input("Please enter your name: ")
		# This takes in a string and casts it to a float, this should be used with caution
		weightLbs = float(input("Please enter your weight in lbs: "))
		# This takes in a string and casts it to a integer, again, use with cation.
		age = int(input("Please enter your age: "))

	except ValueError:
		# If there is invalid input (casting exception)
		# Show the user this text in console, then continue the loop
		print("Sorry, I didn't understand that, try again.")
		continue

	else:
		# The value was successfully parsed
		# So break out of the loop
		break


# Do calculations
weightKg = weightLbs*0.453592

# Print out
print("Hello", title, name, "your weight is")
print(weightLbs, "lbs")
print("which is %.2f" %weightKg, end=' ')
print("in killograms")


"""
Please enter your name: Anthony Waldsmith
Please enter your weight in lbs: 150
Please enter your age: 9001
Hello Human Anthony Waldsmith your weight is
150.0 lbs
which is 68.04 in killograms
"""
