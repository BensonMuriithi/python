
def scan(sentence):
	"""Example of a module that would clasify natural text input within certain realms of a program.
	
	Individual words are categorised according to a lexicon of a certain class or package which would be in stead
	of the lexicon in the below lines.
	
	Each categorised word is put in a tuple with the first element of the tuple being the category of the word
	Words that do not fit in the expected scope are categorised as errors
	The tuples are then placed in a list which is returned."""
	
	
	directions = ["direction", "north", "south", "east", "west", "up", "down", "left", "right", "back"]
	verbs = ["verb", "go", "stop", "kill", "eat"]
	stop_words = ["stop", "the", "in", "of", "from", "at", "it"]
	nouns = ["noun", "door", "bear", "princess", "cabinet"]
	punctuations = "! . , ; : ? _"
	
	words = sentence.split()
	
	#list to hold the tuples
	result = []
	counter = 0
	
	for word in words:
		word = word.lower()
		
		#get rid of any punctuation characters included in the word
		while word[-1] in punctuations.split():
			word = word[0: -1]
		counter += 1
		for l in directions, verbs, stop_words, nouns:
			if word in l:
				result.append((l[0], words[counter - 1]))
				break
				
		if len(result) < counter:
		#if the word hasn't already been categorised and it's tuple added to the list, try it for an integer
			try:
				n = int(word)
				result.append(("number", n))
			except ValueError:
				result.append(("error", words[counter - 1]))
	
	return result