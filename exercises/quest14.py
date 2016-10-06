"""Count from a text input the nmber of lower case and upper case letters"""

print "This program counts the number of upper and lowercase letters in text."
text = raw_input("Enter your text: ")

result = {"lower": 0, "upper": 0}

for c in text:
	if c.isupper(): result["upper"] += 1
	elif c.islower(): result["lower"] += 1
	
print "Lower case: %d\nUpper case: %d" % (result["lower"], result["upper"])