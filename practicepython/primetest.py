"""module to test if a number is a prime number or not and return a boolean as the result"""

def isprime(num):
	num = abs(int(num))
	if num < 2:
		return 0
	if num == 2: return 1
	if num % 2 == 0: return 0
	for i in range(3, int(num / 2), 2):
		if not num % i: return 0
	return 1