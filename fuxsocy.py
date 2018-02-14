#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: fuxsocy.py
# Anthony Waldsmith
# 07/28/2016
# Python Version 3.4
# Description: fuxsocy.py script from Mr.Robot
import sys
import time
import uuid

def main():
	print ("Executing FuxSocy")
	time.sleep(0.5)

	print ("Loading Source of Entropy ...")
	for i in range(0,101):
		printProgress (i, 100, "COMPLETE", 0, 50)
		time.sleep(0.02)
	print ()

	print ("Generating Keys ...")
	for i in range(0,101):
		printProgress (i, 100, "COMPLETE", 0, 50)
		time.sleep(0.05)

	printSlow ("Loading target files ...")
	printSlow ("Beginning crypto operations ...")

	print ("Encrypting /bin")
	time.sleep(2)
	print ("Encrypting /boot")
	time.sleep(2)
	print ("Encrypting /dev")
	time.sleep(2)
	print ("Encrypting /run")
	time.sleep(2)
	print ("Encrypting /etc")
	time.sleep(2)
	print ("Encrypting /var")
	time.sleep(2)
	print ("Encrypting /root")
	time.sleep(2)
	print ("Encrypting /usr")
	time.sleep(2)
	print ("Encrypting /srv")
	time.sleep(2)
	print ()

	print ("Locking FileSystems ...")
	for i in range(0,101):
		printProgress (i, 100, "COMPLETE", 0, 50)
		time.sleep(0.01)

	print ()
	print ("Proxying Network ...")
	for i in range(0,101):
		printProgress (i, 100, "COMPLETE", 0, 50)
		time.sleep(0.02)

	# Generate type 4 UUID aka "random" uuid, a fake "key" in this case ;3
	key = uuid.uuid4().hex
	print ("Private Key: %s" %(key))
	print ("Have a nice day! :)")

# Typewriter effect
def printSlow(text):
	for char in text:
		time.sleep(0.04)
		sys.stdout.write(char)
		sys.stdout.flush()
	print ()

def printProgress(iteration, total, finished, decimals, barLength):
	filledLength = int(round(barLength * iteration / total))
	percents = round(100.00 * (iteration / total), decimals)
	bar = '#' * filledLength + ' ' * (barLength - filledLength)
	percent = '%'
	openpar = '('
	closepar = ')'
	if iteration == total:
		percents = finished
		percent = ''
		openpar = ''
		closepar = ''
	# Unicode: █ -
	sys.stdout.write('\r[%s] %s%s%s%s' %(bar, openpar, percents, percent, closepar)),
	sys.stdout.flush()
	if iteration == total:
		sys.stdout.write('\n')
		sys.stdout.flush()




# Begin
main()
