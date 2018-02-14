# -*- coding: utf-8 -*-
# Program Name: circumference_and_area_of_a_circle.py
# Anthony Waldsmith
# 6/15/2016
# Python Version 3.4
# Description: Computes the circumference and area of a circle.

# Optional import for versions of python <= 2
from __future__ import print_function

# Do this until valid input is given
while True:

	try:
		# This takes in first number and casts to float
		r = float(input("What is the radius (in inches) of the circle you want to draw?: "))
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
pi = 3.1415
area = (pi * (r**2))
circ = (2 * pi * r)


# Print out answer
print("A circle with a radius of %f inches has" %(r))
print("Circumference: %.1f inches" %(circ))
print("Area: %.1f sq. inches" %(area))

"""
What is the radius (in inches) of the circle you want to draw?: 35
A circle with a radius of 35.000000 inches has
Circumference: 219.9 inches
Area: 3848.3 sq. inches
"""
