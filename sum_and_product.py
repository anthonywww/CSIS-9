# -*- coding: utf-8 -*-
# Program Name: sum_and_product.py
# Anthony Waldsmith
# 6/15/2016
# Python Version 3.4
# Description: Take user input of two numbers, then output a sum and product of those numbers

# Optional import for versions of python < 3
from __future__ import print_function


# Do this until valid input is given
while True:

	try:
		# This takes in first number and casts to float
		num1 = float(input("Input first number: "))
		# This takes in second number and casts to float
		num2 = float(input("Input second number: "))
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
sum = (num1 + num2)
prod = (num1 * num2)

# Print out, I use %.2f to just display it as a smaller decimal rather than showing the full decimal
# knowing that it does not change the answer!
print("Sum of %.2f and %.2f is = %f" %(num1,num2,sum))
print("Product of %.2f and %.2f = %f" %(num1,num2,prod))


"""
Input first number: 74.6642
Input second number: 8192.003
Sum of 74.66 and 8192.00 is = 8266.667200
Product of 74.66 and 8192.00 = 611649.350393
"""
