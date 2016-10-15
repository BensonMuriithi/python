import itertools

def isprime(n):
	"""
	Test if a number is a prime number or not and return True or False.
	"""
	
	if n < 2:
		return False
	
	for i in xrange(2, int(pow(abs(n), 1.0/2)) + 1):
		if n % i == 0:
			return False
	
	return True

def next_prime(n):
	if n < 2:
		return 2
	for i in itertools.count(n+2 if n%2 else n+1, 2):
		if isprime(i):
			return i
