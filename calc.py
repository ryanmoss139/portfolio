#!/usr/bin/env python3 

""" Calculator Notes

Create add() function
Create subtract() function
Create divide() function
Create multiply() function

"""

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

# Create our options to present to the user
option1 = "[a] Add \n"
option2 = "[s] Subtract \n"
option3 = "[d] Divide \n"
option4 = "[m] Multiply \n"

# Present options to the user and take a selection as input
option = input("Please select an option:\n{option1}{option2}{option3}{option4} \n> ".format(option1=option1, option2=option2, option3=option3, option4=option4))
option.lower()

# Create our add(self) function 
def add(num1, num2):
	return num1 + num2 

# Create our add(self) function 
def subtract(num1, num2):
	return num1 - num2 

# Create our add(self) function 
def divide(num1, num2):
	return num1 / num2 

# Create our add(self) function 
def multiply(num1, num2):
	return num1 * num2 



if option == 'a':
	add_result = add(num1, num2)
	print("\n {num1} + {num2} = {add_result}".format(num1=num1, num2=num2, add_result=add_result))
elif option == 's':
	subtract_result = subtract(num1, num2)
	print("\n {num1} - {num2} = {subtract_result}".format(num1=num1, num2=num2, subtract_result=subtract_result))
elif option == 'd':
	divide_result = divide(num1, num2)
	print("\n {num1} / {num2} = {divide_result}".format(num1=num1, num2=num2, divide_result=divide_result))
elif option =='m':
	multiply_result = multiply(num1, num2)
	print("\n \n > >  {num1} x {num2} = {multiply_result}".format(num1=num1, num2=num2, multiply_result=multiply_result))
else:
	print("Sorry, please try again using a valid option from the menu.")

print("""
	Thanks for using my Calculator :) 

	Calculator coded by: mossydem
	GitHub: github.com/ryanmoss139
	""")