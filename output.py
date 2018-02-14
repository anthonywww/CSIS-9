# -*- coding: utf-8 -*-
# Program Name: output.py
# Anthony Waldsmith
# 6/13/2016
# Python Version 2.7
# Description: Program to show console output in Python

# Must import print_function because I didn't update to Python 3.x yet.
from __future__ import print_function


print ('Hello World!') # You can use single quotes
print ("Hello World!") # You can use double quotes as well
print ("he\nllo") # \n Is the new-line character (not carriage return \r)

"""
- VARIABLES are named storage locations for numbers, strings, lists
- STRINGS are another type of data, they are represtented as text that are enclosed in quotations
- NUMBERS can either be a FLOAT (9.3) or a INTEGER (1)
- LISTS can be represented as arrays such as [1,2,3] or ["Anthony","Waldsmith"]
- Always use camelCase when possible.
"""

# declare/initialize a new variable named myName and set it to a string value of "Anthony"
myName = "Anthony"
# declare/initialize a new variable named weight and set it to a floating decimal of 183.5483
weight = 154.334923
# declare/initialize a integer of value 33
age = 18
# delcare/initialize a array of numbers (integers to be more specific)
grades = [100,100,100]
# declare/initialize a array of strings
nameZ = ["Anthony","Waldsmith"]



# The + character can concatinate STRINGS only, so becareful!
print ("Hello", myName + ",")
print ("Your weight is", weight, "and your age is", age)
print ("Your rounded weight is %.1f and your age is %i" %(weight,age))
print ("Arrays/Lists: grades =",grades,"nameZ =",nameZ)
print ("This is how you print", end=' ')
# You can use another \ to escape an escape sequence
print ("on the same line, by passing in the parameter end='value'", end=' ')
print ("you can set the ending character to be a ' ' instead of a '\\n'")



# Output
"""
Hello World!
Hello World!
he
llo
Hello Anthony,
Your weight is 154.334923 and your age is 9001
Your rounded weight is 154.3 and your age is 18
Arrays/Lists: grades = [100, 100, 100] nameZ = ['Anthony', 'Waldsmith']
This is how you print on the same line, by passing in the parameter end='value' you can set the ending character to be a ' ' instead of a '\n'
"""

