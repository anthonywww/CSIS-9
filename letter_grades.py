# -*- coding: utf-8 -*-
# Program Name: letter_grades.py
# Anthony Waldsmith
# 6/15/2016
# Python Version 3.4
# Description: Convert grade percentage to letter grade

# Optional import for versions of python <= 2
from __future__ import print_function


# Do this until valid input is given
while True:

	try:
		# This takes in a integer
		percent = int(input("Please enter a grade in percent: "))
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
message = "Error"

if (percent >= 90):
	message = "A"
elif (percent < 90 and percent >= 80):
	message = "B"
elif (percent < 80 and percent >= 70):
	message = "C"
elif (percent < 70 and percent >= 60):
	message = "D"
elif (percent < 60):
	message = "F"
else:
	message = "Error"

# Print out message
print("Your letter grade is an \"%s\"" %(message))

"""
Please enter a grade in percent: 100
Your letter grade is an "A"
"""
