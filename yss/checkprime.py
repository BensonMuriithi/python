"""front end to allow the user to enter a number to determine if it's a prime number.
This module depends on the primetest module for testing"""

import sys
from primetest import isprime

number = raw_input("Enter number to test if it is prime: ")
try:
	print "{} Prime.".format("Is" if isprime(number) else "Not")
except ValueError:
	print "Please enter a number."