import secrets
import string
import random


alphabet_and_nums = string.ascii_letters + "0123456789"

def generate(alphabet_and_nums) -> str:
	"""
	This function is in place to create a new string of characters, numbers and special characters. Strng length is determined by the user in pass_legnth. Default length is 64. 
	
	Create random index
	secrets.randbelow(len(alphbet_and_nums))

	Use random index against our list to generate a new string and join it together after shuffling it 
	newList.append(alphabet_and_nums[random_index])
	new_string = ''.join(random.sample(newList, len(newList)))
	"""

	newList = []
	global new_string
	new_string = ''
	pass_length = int(input('How many characters would you like your new password to be? (0-64) \n'))

	if pass_length <= 64:
		for i in range(0, pass_length):
			random_index = secrets.randbelow(len(alphabet_and_nums))
			newList.append(alphabet_and_nums[random_index])
			new_string = ''.join(random.sample(newList, len(newList)))
			
	else:
		print("Error: Invalid number entered for password length. Please try again. ")
	
	return new_string
	

generate(alphabet_and_nums)
print(f'New Password: {new_string}')
