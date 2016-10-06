"""Custom max and min functions
	
	My functions to replicate the results of max and min
	The functions so far aren't as fast as those of Python's
"""

def getmax(*args):
	"""Return greatest member of the arguments given"""
	start = 0
	limit = len(args)
	i = 1
	
	while i < limit:
		if args[start] < args[i]: start = i
		i += 1
	return args[start]

def getmin(*args):
	"""Return the least of arguments provided"""
	start = 0
	limit = len(args)
	i = 1
	
	while i < limit:
		if args[start] > args[i]: start = i
		i += 1
	return args[start]


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

