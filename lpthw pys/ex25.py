#practise and new functions

def break_Words(stuff):
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	#sort the words
	return sorted(words)
	
def print_first_word(words):
	"""prints the first word after popping?? it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""prints the last word after popping it off the list"""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes a sentence and returns a sorted list of its words"""
	words = break_Words(sentence)
	return sort_words(words)
	
def print_first_And_last(sentence):
	words = break_Words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_And_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)