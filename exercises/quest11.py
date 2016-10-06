"""Assess from a list of coma separated binary numbers provided by the user which numbers are multiples of five
and return those numbers to the user"""

from binary import binarytoint

print "\nEnter a series of binary numbers to test if they are divisible by 5.\n"
numbers = raw_input("Enter numbers in binary : ").split(",")

final = []

for num in numbers:
	if binarytoint(num) % 5 == 0:
		final.append(num)
		
print ", ".join(final)