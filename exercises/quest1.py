"""Find numbers that are divisible by & and not a multiple of 5 between 2000 and 3200 (both included)
The numbers should then be printed separated by commas in a single line"""

for i in range(2000, 3201):
	if (i % 7 == 0) and not (i % 5 == 0):
		print i,