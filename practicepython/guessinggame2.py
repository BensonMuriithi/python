"""Guess the number that a user has chosen

	The program will try to get the number guessed by the user
	between 0 and 100 in as few guesses as possible
	
	For each guess, the user will tell the program if the guess is too high or too low or correct
	
	The program will also return the number of attempts it made at
	establishing the number"""

def hone_in():
	"""uses a binary search technique to establish the number guessed by the user
	within a certain range"""
	
	##if one desired to play the game with a range of number different from 0-100
		#they could uncomment the below numbers and ceil variable lines and
		#change the value of numbers to the top of the range desired
	##numbers = 579
	##ceil = numbers/2
	
	ceil = 50
	floor = 0
	guesses = 0
	
	position = None
	while 1:
		guesses += 1
		position = raw_input("> {}  : ".format(ceil)).lower()
		if position not in ("h", "l", "c"):
			print "Please use 'h' for too high, 'l' for too low or 'c' for correct."
			guesses -= 1
			continue
		if "h" in position:
			ceil -= (ceil-floor) /2
		elif "l" in position:
			floor, ceil = ceil, ceil + ((ceil-floor) / 2) + 1
		else:
			print "Ding! Ding!"
			print "It took %d guesses to get it right " % guesses,
			print "{}".format(":)" if guesses <= 7 else ":(")
			break

if __name__ == "__main__":
	print "This program will guess a number you pick between 0 and 100."
	print "For every guess the computer makes please enter\n"
	print "\t'h' if the guess is too high"
	print "\t'l' if the guess is too low"
	print "\tand 'c' if the guess is correct\n"
	
	raw_input("Now choose a number, keep it to yourself and press enter.")
	hone_in()

