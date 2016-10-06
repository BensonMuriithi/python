"""count the number of unique words in a text file"""

from re import compile as _compile
from collections import Counter
import os

def word_count(_file):
	"""Count the number of unique words in the file
		use the regex '\w+' and Counter to detect words and count unique ones respectively
		A list of tuples with each tuple containing a unique word and its count is returned
	"""
	with open(_file, 'r') as f:
		return Counter(_compile(r'\w+').findall(f.read().lower())).most_common()

if __name__ == "__main__":
	filename = raw_input("\nEnter a file from which to count words > ").lower()
	while not os.path.isfile(filename):
		print "{} does not exist.".format(filename)
		filename = raw_input("\nEnter a file from which to count words > ").lower()
	
	print
	
	#only for perfection in looks. Certainly not good
	_word_count = word_count(filename)
	longest = max([len(i[0]) for i in _word_count])
	
	for word, count in _word_count:
		print "{0:>{1}s}{2:>7}".format(word, longest+2, count)
	
	print

