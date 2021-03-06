"""Unique password generator. Password generated by functions in this module will depend
on the strength specified for the password."""

import random
import string

def main():
	strength = raw_input("How strong do you want your password to be \n \tstrong \tmoderate   or weak > ").lower()
	if "stro" in strength:
		strong_gen()
	elif "mod" in strength:
		moderate_gen()
	elif "weak" in strength:
		weak_gen()
	else:
		try: sys.exit()
		except SystemExit: pass

def strong_gen():
	space = random.randint(0, 1)
	nums = random.randint(1, 3)
	lowers = random.randint(1, 12-2-nums-space)
	caps = random.randint(1, 12-1-nums-space-lowers)
	puncs = 12 - space - nums - lowers - caps
	
	pswd = random.sample(string.lowercase, lowers) + random.sample(string.uppercase, caps) + random.sample(" ", space) + random.sample(string.punctuation, puncs) + random.sample(string.digits, nums)
	random.shuffle(pswd)
	if pswd[-1] == string.whitespace:
		pswd.insert(random.randint(1, len(pswd)-2), pswd.pop())
	elif pswd[0] == string.whitespace:
		pswd.insert(random.randint(1, len(pswd)-2), pswd.pop(0))
	print "".join(pswd)
	
def moderate_gen():
	nums = 1
	space = random.randint(0, 1)
	caps = random.randint(1, 9-nums-space)
	lowers = 9 - nums - space - caps
	
	pswd = random.sample(string.digits, nums) + random.sample(string.uppercase, caps) + random.sample(string.lowercase, lowers) + random.sample(" ", space)
	random.shuffle(pswd)
	if pswd[-1] == string.whitespace:
		pswd.insert(random.randint(1, len(pswd)-2), pswd.pop())
	elif pswd[0] == string.whitespace:
		pswd.insert(random.randint(1, len(pswd)-2), pswd.pop(0))
	
	print "".join(pswd)
	
def weak_gen():
	print random.choice(("Halleluya", "Banana19", "Monkey12", "Alexander", "Cockatoo"))
	
main()