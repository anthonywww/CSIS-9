# -*- coding: utf-8 -*-
# Program Name: rock_paper_scissors.py
# Anthony Waldsmith
# 6/15/2016
# Python Version 3.4
# Description: Simulated "Rock Paper Scisors" game

# Optional import for versions of python <= 2
from __future__ import print_function

# import random class
import random

# Do this until valid input is given
while True:
	print ("Enter either 'r' 'p' 's' or '1' '2' '3'")
	choice = input("Enter Rock(1), Paper(2), or Scissors(3): ")
	if (choice.lower() == "r" or choice.lower() == "rock" or choice == "1"):
		choice = "rock"
		break
	elif (choice.lower() == "p" or choice.lower() == "paper" or choice == "2"):
		choice = "paper"
		break
	elif (choice.lower() == "s" or choice.lower() == "scissors" or choice == "3"):
		choice = "scissors"
		break
	else:
		print("Unknown choice, try again.")
		continue

# Computer rolls, generate a random number 1 to 3
random = random.randint(1,3)
comp = "Error"
result = "Error"

# Computer random to string
if (random == 1):
	comp = "rock"
elif (random == 2):
	comp = "paper"
else:
	comp = "scissors"

# Game logic
if (choice == comp):
	result = "Tie!"
elif (choice == "rock" and comp == "paper"):
	result = "You lost, Paper covers Rock!"
elif (choice == "rock" and comp == "scissors"):
	result = "You won, Rock breaks Scissors!"
elif (choice == "paper" and comp == "rock"):
	result = "You won, Paper covers Rock!"
elif (choice == "paper" and comp == "scissors"):
	result = "You lost, Scissors cuts Paper!"
elif (choice == "scissors" and comp == "rock"):
	result = "You lost, Rock breaks Scissors!"
elif (choice == "scissors" and comp == "paper"):
	result = "You won, Scissors cuts Paper!"
else:
	result = "Error"

# Print the results to console
print ("You rolled '%s'" %(choice))
print ("The computer rolled '%s'" %(comp))
print ("Result: %s" %(result))


"""
Enter either 'r' 'p' 's' or '1' '2' '3'
Enter Rock(1), Paper(2), or Scissors(3): 4
Unknown choice, try again.
Enter either 'r' 'p' 's' or '1' '2' '3'
Enter Rock(1), Paper(2), or Scissors(3): 3
You rolled 'scissors'
The computer rolled 'paper'
Result: You won, Scissors cut Paper!
"""
