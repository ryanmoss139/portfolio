#!/usr/bin/env python3

""" Calculator Notes

Now we have simple functionality, we need to think about how we can improve this 

Import time and use time.sleep() to improve general flow of program for user 

Scan through code and double check it is all readable, noted and clean

"""

import time

# First we introduce any variables we might require later on in the program
# Including a little welcome message of course
welcome_message = """
Welcome to my calculator.
Please enter your first number, followed by your second. 
Once you have done this please select an option from the list provided.
Only enter the letter, not the brackes surrounding or it won't work.
"""
print(welcome_message)

# Take input from the user to store the numbers they want to use
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
time.sleep(1)

# Create our options to present to the user
option1 = "[a] Add \n"
option2 = "[s] Subtract \n"
option3 = "[d] Divide \n"
option4 = "[m] Multiply \n"

# Present options to the user and take a selection as input
option = input(f"\nPlease select an option:\n{option1}{option2}{option3}{option4} \n> ")
option = option.lower()

print("\nProcessing Calculation...")
time.sleep(2)


# Create our add() function 
def add(num1, num2):
	return num1 + num2 

# Create our add() function 
def subtract(num1, num2):
	return num1 - num2 

# Create our add() function 
def divide(num1, num2):
	return num1 / num2 

# Create our add() function 
def multiply(num1, num2):
	return num1 * num2 

def check_sum(num1, num2):
	# Our conditional arguments to test the option input from the user and provide a result
	if option == 'a':
		add_result = add(num1, num2)
		print(f"\nResult: {num1} + {num2} = {add_result}")
	elif option == 's':
		subtract_result = subtract(num1, num2)
		print(f"\nResult: {num1} - {num2} = {subtract_result}")
	elif option == 'd':
		divide_result = divide(num1, num2)
		print(f"\nResult: {num1} / {num2} = {divide_result}")
	elif option =='m':
		multiply_result = multiply(num1, num2)
		print(f"\nResult: {num1} x {num2} = {multiply_result}")
	else:
		# Error message incase the user pressed an incorrect option
		print("Sorry, please try again using a valid option from the menu.")

# Run check function to check the numbers and the option and produce result
check_sum(num1, num2)

time.sleep(2)
# A nice output before the program closes 
print("""
Thanks for using my Calculator :) 

Calculator coded by: Ryan Moss
GitHub: github.com/ryanmoss139
""")
time.sleep(2)