"""Rudimentary script that could convert binary numbers to decimals while avoiding the int function with base two"""
def binarytoint(number):
	#just in case the number isn't in a string already
	number = str(number)
	
	while number[0] == " ": number = number[1:]
	length = len(number)
	result = 0
	
	for i in range(0, length):
		if number[i] not in "01":
			raise ValueError("Invalid literal for binary: '%s'" % number)
		
	for i in range(0, length):
		if number[i] == "0": continue
		
		if number[i] == "1":
			if i < length - 1: result += 2**(length - 1 - i)
			else: result += 1
			
	return result