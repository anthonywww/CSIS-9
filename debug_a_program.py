# Debug/fix the following program so that it shows the indicated output

# TODO: Fixed spacing, personally I hate spaces, so I use <TAB> which saves time to get around scripts, and makes code easier to see for others
# TODO: This is a dangerous way to get user input, I would strongly recommend against trusting raw user input
# FIXME: Since you are getting user input and expecting an integer, you must cast to an integer int()
num = int(input("Please enter a number: "))

# FIXME: Added parameter 'num' to function
def isEven(num):
# FIXME: If statement requires : after the condition
# FIXME: Invalid syntax, requires conditional comparation operator (==), not assignment operator (=)
	if (num % 2 == 0):
		# FIXME: Misspelled 'return' and remove : after the value to return
		return True
	# FIXME: Removed obsolete code that isn't nessesary for the 'else' statement. Switched to 'else' over 'elif' since you are only returning a boolean
	else:
		return False

def main():
	# FIXME: Invalid syntax, ';' and ',' is not used, use %(var) to pass in arguments.
	# FIXME: Function call is incorrect, should be 'isEven()'
	# FIXME: Missing closing ')' for function call to 'print()'
	print ("The number %i is even: %s"  %(num, isEven(num)))

# FIXME: Requires () to call a function
main()

# FIXME: Removed "=== OUTPUT ===" since this is not from the direct program output
"""'
Enter a number: 5
The number 5 is even: False
"""
