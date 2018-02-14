#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: lockers.py
# Anthony Waldsmith
# 7/6/2016
# Python Version 3.4
# Description: Show how many lockers are open/close after a alternating loop run for each value instance 1000 times.

# Optional import for versions of python <= 2
from __future__ import print_function

step = 0
totalLockers = 1000
locker = []
openLockerCount = 0
closeLockerCount = 0

for i in range(0, totalLockers):
	locker.append(False);

for i in range(totalLockers):
	# Incerement the step
	step += 1
	for j in range(0, totalLockers, step):
		# Set the current locker to the current mode
		locker[j] = not locker[j];

	# Taking into consideration locker[0] should always be open
	locker[0] = True

for i in range(totalLockers):
	if(locker[i] == True):
		openLockerCount += 1
		print("Locker %i is open" %(i))
	else:
		closeLockerCount += 1
		#print("Locker %i is closed" %(i))

print ("There are a total of %i lockers open, and a total of %i lockers closed" %(openLockerCount, closeLockerCount))

"""
Locker 0 is open
Locker 1 is open
Locker 4 is open
Locker 9 is open
Locker 16 is open
Locker 25 is open
Locker 36 is open
Locker 49 is open
Locker 64 is open
Locker 81 is open
Locker 100 is open
Locker 121 is open
Locker 144 is open
Locker 169 is open
Locker 196 is open
Locker 225 is open
Locker 256 is open
Locker 289 is open
Locker 324 is open
Locker 361 is open
Locker 400 is open
Locker 441 is open
Locker 484 is open
Locker 529 is open
Locker 576 is open
Locker 625 is open
Locker 676 is open
Locker 729 is open
Locker 784 is open
Locker 841 is open
Locker 900 is open
Locker 961 is open
There are a total of 32 lockers open, and a total of 968 lockers closed
"""
