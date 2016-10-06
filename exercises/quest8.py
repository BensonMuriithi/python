"""accept a comma seprated sequence of words and sort the words and print them out alos separated by commas"""

raw_words = raw_input("Enter your comma seprated words : ").split(",")

for x in range(0, len(raw_words)):
	while raw_words[x][0] == " ":
		raw_words[x] = raw_words[x][1:]

raw_words.sort()
print ", ".join(raw_words)