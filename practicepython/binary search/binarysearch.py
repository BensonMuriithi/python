"""search for a provided number within an ordered list of items"""


def is_in(the_list, num):
	"""Return True or False depending on whether the number specified in 'num' is
	in the Ordered list 'the_list'
	
	The function can be called with list(set(x)) for the_list parameter
	if x has duplicate elements and list() will sort the result
	"""
	length = len(the_list)
	if length > 1:
		middle = length / 2
		if num < the_list[middle]:
			return is_in(the_list[:middle], num)
		else: return is_in(the_list[middle:], num)
	
	return the_list[0] == num


if __name__ == "__main__":pass