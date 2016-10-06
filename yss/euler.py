""""Get the sum of all prime numbers less than a specified limit

	The module was written to get the sums of primes below 2 million"""

def isprime(number):
	"""Test if a number is prime"""
	for i in xrange(3, int(number**0.5)+1, 2):
		if not number % i:
			return 0
	return 1

def getprime(limit):
	"""Generator function for prime numbers below limit"""
	yield 2
	num = 3
	while num <= limit:
		if isprime(num):
			yield num
			
		num += 2
		
def count_em(limit=10):
	"""Function to call
		sums primes below limit. If limit parameter is ommitted, it defaults to ten"""
	total = reduce((lambda a, b: a + b), getprime(limit))
	
	print "Sum of primes upto %d is %d" % (limit, total)


if __name__ == "__main__":pass