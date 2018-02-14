# -*- coding: utf-8 -*-
# Program Name: multiplication_table.py
# Anthony Waldsmith
# 6/13/2016
# Python Version 2.7
# Description: Program to show a multiplication table for floats 0.1, 0.2, 0.3

# Import for python versions <= 2
from __future__ import print_function

prompt = "Please input "
num1 = 0.1
num2 = 0.2
num3 = 0.3

# Do this until valid input is given
while True:

	try:
		# This takes in first number and casts to float
		num1 = float(input(prompt + "first number: "))
		# This takes in second number and casts to float
		num2 = float(input(prompt + "second number: "))
		# This takes in third number and casts to float
		num3 = float(input(prompt + "third number: "))
	except ValueError:
		# If there is invalid input (casting exception)
		# Show the user this text in console, then continue the loop
		print("Sorry, I didn't understand that, try again.")
		continue

	else:
		# The value was successfully parsed
		# So break out of the loop
		break


# Print table/matrix values
print("\nMultiplication Table/Matrix for (%.2f, %.2f, %.2f):\n" %(num1,num2,num3))

print("        %.2f    %.2f    %.2f" %(num1,num2,num3))
print("     +----------------------------")
print("%.2f |  %.2f    %.2f    %.2f" %(num1, num1*num1, num1*num2, num1*num3))
print("%.2f |  %.2f    %.2f    %.2f" %(num2, num2*num1, num2*num2, num2*num3))
print("%.2f |  %.2f    %.2f    %.2f" %(num2, num3*num1, num3*num2, num3*num3))

"""
Please input first number: 0.6
Please input second number: 0.8
Please input third number: 0.10

Multiplication Table/Matrix for (0.60, 0.80, 0.10):

        0.60    0.80    0.10
     +----------------------------
0.60 |  0.36    0.48    0.06
0.80 |  0.48    0.64    0.08
0.80 |  0.06    0.08    0.01
"""
