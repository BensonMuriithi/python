"""Much improved version of the binarysearch module
	
	This version is faster and memory friendly
"""


def search(shtiuff, sumn):
	"""Searches for an element 'sumn' in the list 'shtiuff'
		 
		It's not for performance or effectiveness but for fooling around.
		Shtiuff can be any collection.
		"""
	
	if isinstance(shtiuff, str):
		return __search_string(shtiuff, sumn)
	elif isinstance(shtiuff, dict):
		shtiuff = shtiuff.values()
	
	ceil = len(shtiuff) - 1
	floor = 0
	middle = ceil / 2
	
	shtiuff = sorted(shtiuff)
	while floor != ceil:
		if sumn > shtiuff[middle]:
			floor = middle + 1
		else:
			ceil = middle
		
		middle = floor + ((ceil - floor) / 2)
	
	return shtiuff[floor] == sumn

def __search_string(word, snip):
	"""Perform search in a string. Slower than Python's in keyword for searching a string."""
	length_word = len(word)
	length_snip = len(snip)
	
	if length_snip > length_word:
		return False
	
	p = 0
	while p < length_word:
		if word[p] == snip[0]:
			break
		p += 1
	
	if (length_word - p) < length_snip:
		return False
	
	j = 0
	while j < length_snip:
		if word[p] != snip[j]:
			if (length_word - p) >= length_snip:
				return __search_string(word[p:], snip)
			else:
				return False
		p += 1
		j += 1
	
	return True

