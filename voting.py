# -*- coding: utf-8 -*-
# Program Name: voting.py
# Anthony Waldsmith
# 6/15/2016
# Python Version 3.4
# Description: A voting verification program

# Optional import for versions of python <= 2
from __future__ import print_function


# Define a verify function for "yes" or "no"
def verify(cond):
	if (cond.lower() != "yes" and cond.lower() != "no"):
		print("Sorry, either pick 'yes' or 'no'")
		return False
	else:
		return True

# Do this until valid input is given
while True:

	try:
		# Take in user age
		age = int(input("How old are you?: "))

		# Take in citizenship
		citizen = input("Are you a U.S. citizen? (Yes/No): ")

		# Verify input
		if(verify(citizen) == False):
			continue

		# Take in if registered
		registered = input("Have you registered to vote? (Yes/No): ")

		# Verify input
		if(verify(registered) == False):
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

# Define end function
def end(message):
	print()
	print(message)
	exit()


# If they are under age
if (age < 18):
	end("You are under age.\nSorry but you cannot vote.\nMaybe in a few years!")

# If they are not a citizen
if (citizen.lower() == "no"):
	end("You must be a U.S. Citizen to vote.\nSorry but you cannot vote.")

# If they are not registered to vote
if (registered.lower() == "no"):
	end("You must be registered to vote.\nSorry but you cannot vote until you register, so GO REGISTER!")

end("You can vote!")



"""
How old are you?: 80 
Are you a U.S. citizen? (Yes/No): yes
Have you registered to vote? (Yes/No): yes

You can vote!
"""
