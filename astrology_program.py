# -*- coding: utf-8 -*-
# Program Name: astrology_program.py
# Anthony Waldsmith
# 6/15/16
# Python Version 3.4
# Description: Get birthday and display Zodiac Signs

# Optional import for versions of python <= 2
from __future__ import print_function


# Define verify function
def valid(value, max):
	if (value <= 0):
		return False
	elif (value > max):
		return False
	else:
		return True

# Do this until valid input is given
while True:

	try:
		# Get day as integer
		day = int(input("Please enter day of birth (1-32): "))

		# Validate
		if (not valid(day,32)):
			print("Invalid day of birth must be 1-32, try again.")
			continue

		# Get month as integer
		month = int(input("Please enter month of birth (1-12): "))

		# Validate
		if (not valid(month,12)):
			print("Invalid month, must be 1-12")
			continue

	except ValueError:
		# If there is invalid input (casting exception)
		# Show the user this text in console, then continue the loop
		print("Sorry, I didn't understand that, try again.")
		continue

	else:
		# The value was successfully parsed
		# So break out of the loop
		break


# Message Array(list) format [SIGN , GROUP , COMPATABILITY_1, COMPATABILITY_2]
message = []


# Logic
if ((month == 3 and day >= 21) or (month == 4 and day <= 19)):
	message = ["Aries", "Fire", "Leo", "Sagittarius"]

if ((month == 4 and day >= 20) or (month == 5 and day <= 20)):
	message = ["Taurus", "Earth", "Virgo", "Capricorn"]

if ((month == 5 and day >= 21) or (month == 6 and day <= 21)):
	message = ["Gemini", "Air", "Libra", "Aquarius"]

if ((month == 6 and day >= 22) or (month == 7 and day <= 22)):
	message = ["Cancer", "Water", "Scorpio", "Pisces"]

if ((month == 7 and day >= 23) or (month == 8 and day <= 22)):
	message = ["Leo", "Fire", "Aries", "Sagittarius"]

if ((month == 8 and day >= 23) or (month == 9 and day <= 22)):
	message = ["Virgo", "Earth", "Taurus", "Capricorn"]

if ((month == 9 and day >= 23) or (month == 10 and day <= 23)):
	message = ["Libra", "Air", "Gemini", "Aquarius"]

if ((month == 10 and day >= 24) or (month == 11 and day <= 21)):
	message = ["Scorpio", "Water", "Cancer", "Pisces"]

if ((month == 11 and day >= 22) or (month == 12 and day <= 21)):
	message = ["Sagittarius", "Fire", "Aries", "Leo"]

if ((month == 12 and day >= 22) or (month == 1 and day <= 19)):
	message = ["Capricorn", "Earth", "Taurus", "Virgo"]

if ((month == 1 and day >= 20) or (month == 2 and day <= 18)):
	message = ["Aquarius", "Air", "Gemini", "Libra"]

if ((month == 2 and day >= 19) or (month == 3 and day <= 20)):
	message = ["Pisces", "Water", "Cancer", "Scorpio"]


# Print output
print ()
print ("A birthday of the month number %i and %ith day:" %(month,day))
print ("You are %s, %s group, compatible with %s: %s, %s" %(message[0], message[1], message[0], message[2], message[3]))

"""
Please enter day of birth (1-32): 28
Please enter month of birth (1-12): 6

A birthday of the month number 6 and 28th day:
You are Cancer, Water group, compatible with Cancer: Scorpio, Pisces
"""
