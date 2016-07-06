
def scan(sentence):
	"""Example of a module that would clasify natural text input within certain realms of a program."""
	directions = ["direction", "north", "south", "east", "west", "up", "down", "left", "right", "back"]
	verbs = ["verb", "go", "stop", "kill", "eat"]
	stop_words = ["stop", "the", "in", "of", "from", "at", "it"]
	nouns = ["noun", "door", "bear", "princess", "cabinet"]
	punctuations = "! . , ; : ? _"
	
	words = sentence.split()
	result = []
	counter = 0
	
	for word in words:
		word = word.lower()
		while word[-1] in punctuations.split():
			word = word[0: -1]
		counter += 1
		for l in directions, verbs, stop_words, nouns:
			if word in l:
				result.append((l[0], words[counter - 1]))
				break
				
		if len(result) < counter:
			try:
				n = int(word)
				result.append(("number", n))
			except ValueError:
				result.append(("error", words[counter - 1]))
	
	return result