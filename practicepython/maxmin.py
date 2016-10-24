"""Custom max and min functions
	
	My functions to replicate the results of max and min
	The functions so far aren't as fast as those of Python's
"""

from operator import lt, gt

def _max_or_min(operation, *args):
	if len(args) is 1:
		try:
			return _max_or_min(operation, *args[0])
		except TypeError:
			return args[0]
	
	max_pos = 0
	for i in xrange(1, len(args)):
		if operation(args[i], args[max_pos]):
			max_pos = i
	
	return args[max_pos]

def getmax(*args):
	"""
	Return greatest value among the values provided
	If a collection is provided, the function works on that collection
	instead. However if multiple collections are provided, they will be
	treated as single values.
	"""
	return _max_or_min(gt, *args)

def getmin(*args):
	"""
	Return least value among the values provided
	If a collection is provided, the function works on that collection
	instead. However if multiple collections are provided, they will be
	treated as single values.
	"""
	return _max_or_min(lt, *args)


if __name__ == "__main__":
	text = raw_input("Enter values to get which is the largest and smallest : ")
	items = text.split(",")
	if len(items) < 2: items = text.split()
	
	for i in xrange(len(items)):
		try:
			items[i] = int(items[i])
		except ValueError:
			items[i] = items[i].strip()
	
	print "The largest value is :", getmax(*items)
	print "The least value is :", getmin(*items)

