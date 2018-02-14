#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: dice.py
# Anthony Waldsmith
# 6/16/2016
# Python Version 3.4
# Description: Dice game, roll and try to get the highest number vs the computer

# Optional import for versions of python <= 2
from __future__ import print_function

# import utilities/libraries
import sys
import random
import time


# Define typewriter effect function
def coolprint(text):
	# Here it takes each letter (character) from text and sets it to the variable char
	for char in text:
		# Here we add a short delay
		time.sleep(0.03)
		# This is essentially the same as print ("text",end=' ') however that function does not handle spaces very well.
		# so using this function deeper in python allows me to directly write each character individually.
		sys.stdout.write(char)
		# This pushes the text out to the stdout stream (in this case the console is the output)
		sys.stdout.flush()


coolprint ("== B E A T   T H E   C O M P U T E R! ==\n")
print ()

while True:

	# Generate rolls
	c_die1 = random.randint(1,6)
	c_die2 = random.randint(1,6)
	p_die1 = random.randint(1,6)
	p_die2 = random.randint(1,6)

	coolprint ("You rolled a %i and %i (total = %i)\n" %(p_die1,p_die2,p_die1+p_die2))

	# Get input from user
	rollagain = input("Re-roll? (Y/N): ")

	# Test if it's valid
	if (rollagain.lower() != "y" and rollagain.lower() != "n"):
		print ()
		coolprint ("Sorry, I didn't understand that, re-rolling anyways...\n")
		continue
	else:
		if (rollagain.lower() == "y"):
			print ()
			coolprint ("Re-rolling ...\n")
			print ()
			continue
		else:
			break


coolprint ("The computer rolled %i and %i (total = %i) " %(c_die1,c_die2,c_die1+c_die2))

time.sleep (0.3)

for i in range(3):
	coolprint (".")
	time.sleep(0.3)

print ()
print ()

if ((p_die1+p_die2) > (c_die1+c_die2)):
	coolprint ("Congradulations! You won.\n")
elif ((p_die1+p_die2) < (c_die1+c_die2)):
	coolprint ("So sorry, You lost.\n")
else:
	coolprint ("It's a tie!\n")




"""
== B E A T   T H E   C O M P U T E R! ==

You rolled a 5 and 2 (total = 7)
Re-roll? (Y/N): y

Re-rolling ...

You rolled a 5 and 4 (total = 9)
Re-roll? (Y/N): y

Re-rolling ...

You rolled a 6 and 6 (total = 12)
Re-roll? (Y/N): n
The computer rolled 3 and 3 (total = 6) ...

Congradulations! You won.
"""
