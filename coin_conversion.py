# -*- coding: utf-8 -*-
# Program Name: coin_conversion.py
# Anthony Waldsmith
# 06/15/16
# Python Version 3.4
# Description: Convert amount into coins

# Optional import for versions of python <= 2
from __future__ import print_function


# Do this until valid input is given
while True:

	try:
		# This takes in a integer
		coins = int(input("Please enter the total amount of coins: "))
	except ValueError:
		# If there is invalid input (casting exception)
		# Show the user this text in console, then continue the loop
		print("Sorry, I didn't understand that, try again, must be a whole number!")
		continue

	else:
		# The value was successfully parsed
		# So break out of the loop
		break

# Quarters conv
quarters = int(coins / 25)
coins = (coins - (quarters * 25))
print ("# of Quarters: %i x 25c = %i cents total" %(quarters,quarters*25))

# Dimes conv
dimes = int(coins / 10)
coins = (coins - (dimes * 10))
print ("# of Dimes: %i x 10c = %i cents total" %(dimes,dimes*10))

# Nickles conv
nickles = int(coins / 5)
coins = (coins - (nickles * 5))
print ("# of Nickles: %i x 5c = %i cents total" %(nickles,nickles*5))

# Pennies conv
pennies = int(coins)
print ("# of Pennies: %i x 1c = %i cents total" %(pennies,pennies*1))


"""
Please enter the total amount of coins: 166
# of Quarters: 6 x 25c = 150 cents total
# of Dimes: 1 x 10c = 10 cents total
# of Nickles: 1 x 5c = 5 cents total
# of Pennies: 1 x 1c = 1 cents total
"""
