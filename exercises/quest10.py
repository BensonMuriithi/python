"""Accept series of words separated by whitespace and sort the words while removnig duplicate words
print the finished series of words final"""

raw_words = raw_input("\nEnter words separated by whitespace for sorting\n    > ").split()

if raw_words:
	fin_words = []
	for x in range(0, len(raw_words)):
		while raw_words[x][0] == " ": raw_words[x] = raw_words[x][1:]
		
		if raw_words[x] not in fin_words: fin_words.append(raw_words[x])
		
	fin_words.sort()
	print " ".join(fin_words)