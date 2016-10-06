import random
from urllib import urlopen
import sys

URL = "http://learncodethehardway.org/words.txt" 
Words = []

Phrases = {
	"class %%%(%%%):": "Make a class named %%% that is-a %%%",
	"class %%%(object):\n\tdef __init__(self, ***)" : 
		"class %%% has-a __init__ that takes self and *** as parameters.",
	"class %%%(object):\n\tdef __init__(self, @@@):" : 
		"class %%% has-a __init__ that takes self and @@@ parameters.",
	"*** = %%%()" : "make *** an instance of %%%",
	"***.***(@@@)" : "Call the function *** from *** with the extra parameter @@@",
	"***.*** = ***" : "set the attribute *** in *** to be ***"}

phrases_first = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	phrases_first = True
	

for line in urlopen(URL).readlines():
	Words.append(line.strip())
	
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(Words, snippet.count("%%%"))]
	
	other_names = random.sample(Words, snippet.count("***"))
	results = []
	param_names = [(', '.join(random.sample(Words, random.randint(1, 3)))) for x in snippet.count("@@@")]
	
	"""for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(", ".join(random.sample(Words, param_count)))"""
		
	for sentence in snippet, phrase:
		result = sentence[:]
		
		#deal with fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		#deal woth fake other names.
		for word in other_names:
			result = result.replace("***", word, 1)
			
		#deal woth fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
	return results
	
#keep going until CTRL-Z is hit
try:
	while True:
		snippets = Phrases.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = Phrases[snippet]
			question, answer = convert(snippet, phrase)
			if phrases_first:
				question, answer = answer, question
			
			print question
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer			
except EOFError:
	print "\nBye."