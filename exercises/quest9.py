"""accepts lines of text as input and capitalize all characters in the lines and finally print the lines."""

lines = []

print "\nEnter sentences to capitalize. Leave blank to finish.\n"

while True:
	sentence = raw_input("   > ")
	if sentence and sentence != " ":
		lines.append(sentence.upper())
	else:
		break

for line in lines: print line