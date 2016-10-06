"""Accept antry of any input and calculate the number of letters and decimals in the input"""

entered = raw_input("Enter input : ")

if entered.isalpha() or entered.isdigit():
	print "%s" % ("Letters: %d" % len(entered)) if entered.isalpha() else ("Numbers: %d" % len(entered))
	quit()

numbers = 0
letters = 0
punctuations = 0

for c in entered:
	if c.isalpha(): letters += 1
	elif c.isdigit(): numbers += 1
	elif not c.isspace(): punctuations += 1
	
if letters: print "Letters: %d" % letters
if numbers: print "Numbers: %d" % numbers
if punctuations: print "Punctuations: %d" % punctuations