"""Read from a text file and count The number of occurences of unique words"""

import os

def getword_list(_file):
	"""Opens the specified text file and returns a list of words from a line
	to prevent overloading if a file is too large."""
	with open(_file, 'r') as f:
		_line = f.readline()
		while _line:
			yield _line.split()
			_line = f.readline()
	
def count_words(_file):
	words = {}
	for l in getword_list(_file):
		for w in l:
			if words.has_key(w): words[w] += 1
			else: words[w] = 1
	
	print "\n"
	for k in words.iterkeys(): print "%s  :  %d" % (k, words[k])
	print "\n"
	
if __name__ == "__main__":
	fname = raw_input("Enter file to count words from >> ").lower()
	while not os.path.isfile(fname):
		print "\nInvalid file name.\n"
		fname = raw_input("Enter file to count words from >> ").lower()
		
	count_words(fname)

