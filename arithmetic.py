#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: arithmetic.py
# Anthony Waldsmith
# 6/16/2016
# Python Version 3.4
# Description: A program to let a child practice arithmetic skills

# Optional import for versions of python <= 2
from __future__ import print_function

# Imports
import random
import time
import sys

# Define function cool print
def coolprint(text, delay=0.03):
	# Here it takes each letter (character) from text and sets it to the variable char
	for char in text:
		# Here we add a short delay
		time.sleep(delay)
		# This is essentially the same as print ("text",end=' ') however that function does not handle spaces very well.
		# so using this function deeper in python allows me to directly write each character individually.
		sys.stdout.write(char)
		# This pushes the text out to the stdout stream (in this case the console is the output)
		sys.stdout.flush()



# Define function for integer inputting
def intInput(prompt):
	# While the input is invalid keep re-trying
	while True:
		# Try getting user input
		try:
			print ()
			value = int(input(prompt))
		# Catch exception
		except ValueError:
			coolprint("That is not a whole number, try again\n")
			continue
		except NameError:
			coolprint("That is not a whole number, try again\n")
			continue
		except SyntaxError:
			coolprint("That is not a whole number, try again\n")
			continue

		# If the input is valid return (break)
		else:
			return value



# Define function for inputting a question with parameters to cover multiple quesitions
def question(array):

	# Print to the user the first question in the list (array)
	print ()
	coolprint (array[0] + "\n", 0.02)

	# Itterate (loop) through the possible parameters
	for i in range(1, len(array)):
		coolprint("%i) %s\n" %(i, array[i]), 0.02)

	# Get user option
	print ()
	while True:
		# Get user's choice
		val = intInput("Choice: ")

		# If the input is invalid, show it's invalid and try again
		if (val < 1 or val > (len(array)-1)):
			print ()
			coolprint ("Not a valid input, it must be between 1 and %i" %((len(array)-1)))
			continue
		else:
			break

	# Return the input value
	return val


# Quit the application
def bye():
	print ()
	coolprint ("Good Bye!")
	print ()
	exit()



# Define function for +ADDING+
def adding():

	# Generate 2 random whole positive integers
	rnd1 = random.randint(1,9)
	rnd2 = random.randint(1,9)

	# Generate the answer
	ans = (rnd1 + rnd2)

	while True:

		# Prompt the user for an answer with the question
		print ()
		coolprint ("What is %i + %i equal to? \n" %(rnd1, rnd2))
		val = intInput("Answer: ")

		# Check the answer
		if (ans == val):
			print ()
			coolprint ("That is Correct!\n")
			q = ["Would you like to try another?","Yes","No"]
			if(question(q) == 1):
				#  Break out of loop
				break
			else:
				bye()
		else:
			print ()
			coolprint ("That is incorrect, try again:\n")
			continue

	# Call adding again
	adding()


# Define function for -SUBTRACTING-
def subtracting():

	# Generate 2 random whole positive integers
	rnd1 = random.randint(1,9)
	rnd2 = random.randint(1,9)

	# Generate the answer
	ans = (rnd1 - rnd2)

	while True:

		# Prompt the user for an answer with the question
		print ()
		coolprint ("What is %i - %i equal to? \n" %(rnd1, rnd2))
		val = intInput("Answer: ")

		# Check the answer
		if (ans == val):
			print ()
			coolprint ("That is Correct!\n")
			q = ["Would you like to try another?","Yes","No"]
			if(question(q) == 1):
				#  Break out of loop
				break
			else:
				bye()
		else:
			print ()
			coolprint ("That is incorrect, try again:\n")
			continue

	# Call subtracting again
	subtracting()


# Define function for *MULTIPLYING*
def multiplying():

	# Generate 2 random whole positive integers
	rnd1 = random.randint(1,9)
	rnd2 = random.randint(1,9)

	# Generate the answer
	ans = (rnd1 * rnd2)

	while True:

		# Prompt the user for an answer with the question
		print ()
		coolprint ("What is %i * %i equal to? \n" %(rnd1, rnd2))
		val = intInput("Answer: ")

		# Check the answer
		if (ans == val):
			print ()
			coolprint ("That is Correct!\n")
			q = ["Would you like to try another?","Yes","No"]
			if(question(q) == 1):
				#  Break out of loop
				break
			else:
				bye()
		else:
			print ()
			coolprint ("That is incorrect, try again:\n")
			continue

	# Call multiplying again
	multiplying()


# -- BEGIN --
# Display choices and loop
print ("-"*60)
print ("             Welcome to Arithmetic.py!")
print ("-"*60)

# Create list of parameters
q = ["Pick one of the following operations:","Adding","Subtracting","Multiplying"]

# Pass in list (array) of parameters to function question which returns a integer value of the response
choice = question(q)

# Choose operation
if (choice == 1):
	adding()
elif (choice == 2):
	subtracting()
else:
	multiplying()


"""
------------------------------------------------------------
             Welcome to Arithmetic.py!
------------------------------------------------------------

Pick one of the following operations:
1) Adding
2) Subtracting
3) Multiplying


Choice: 1

What is 6 + 8 equal to? 

Answer: -9000

That is incorrect, try again:

What is 6 + 8 equal to? 

Answer: 14

That is Correct!

Would you like to try another?
1) Yes
2) No


Choice: 2

Good Bye!
"""
