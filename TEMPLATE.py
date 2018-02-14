#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: <ENTER PROGRAM NAME>
# <ENTER NAME>
# <ENTER DATE>
# Python Version 3.4
# Description: <ENTER DESCRIPTION>

# Optional import for versions of python <= 2
from __future__ import print_function


# Do this until valid input is given
while True:

	try:
		# Text input
		text = input("Prompt ")
	except ValueError:
		# If there is invalid input (casting exception)
		# Show the user this text in console, then continue the loop
		print("Sorry, I didn't understand that, try again.")
		continue

	else:
		# The value was successfully parsed
		# So break out of the loop
		break
