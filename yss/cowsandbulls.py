"""Cows and Bulls game.
	a random 4 digit number is generated and the user is asked to guess the 4 digit number
	for each guess if any correct number is entered in it's right location, the player gets a "cow"
	any correct digit guessed but out of position wins the player a "bull"
	
	The game continues until the player gets the number correct or quits"""
	
import random, itertools

def get_guess():
	"""Handles getting the input from the player
	
	Checks if the input is of the required length(4) and that the input is a positive integer
	Also handle quiting the game when 'q' is entered
	"""
	
	i = None
	try:
		entry = raw_input(">>> ")
		i = str(abs(int(entry)))
		if "q" in entry.lower():
			quit()
		if len(i) < 4:
			raise ValueError
	except ValueError:
		print "Invalid entry."
		return get_guess()
	
	return i
	
def cow_in_position(pos, l):
	#to check if that digit in the guess has been awarded a cow
	for x in l:
		if x[0] == pos:
			return 1
	return 0
	
def times_in_list(num, l):
	return len([0 for x in l if x[1] == num])

def play(correct):
	print "Enter a 4-digit number ('q' to quit):"
	#print correct
	###if you wanted to test it yourself
	bulls, cows = [], []
	while 1:
		snumber = get_guess()
		if snumber == correct:
			#save processing if the user is already correct
			#if changed implement changes to end of loop as well.
			print "4 cows, 0 bulls.\n"
			break
		
		for c, i in itertools.izip(snumber, range(0, len(snumber))):
			if correct[i] == c:
				cows.append((i, c))
		
		for c, i in itertools.izip(snumber, range(0, len(snumber))):
			#if this digit is not present in correct or it already has a cow, don't bother
			if c not in correct or cow_in_position(i, cows): continue
			
			#to make sure that if a player enteres a number like 7777 doesn't get a point
			#for every digit. if an equal digit has already been granted a point
			#and there are no more equivalent digits in the correct number, don't award a bull
			#award if there's still an equal digit in the correct number that hasn't been compared against
			
			if (times_in_list(c, cows) + times_in_list(c, bulls)) < correct.count(c):
				bulls.append((i, c))
				
		print "%d cows, %d bulls" % (len(cows), len(bulls))
		bulls, cows = [], []
		
if __name__ == "__main__":
	print "\nWelcome to the Cows and Bulls  Game!\n"
	play(str(random.randint(1000, 9999)))