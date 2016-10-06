"""Calculate the value q according to the fromula:
Q = Square root of [(2 * C * D)/H]
with the values of C and H fixed as 50 and 30 respectively

Calculate the resultant values Q where D is the numbers entered at the console"""

from math import sqrt

c = 50; h = 30

strings = raw_input("Enter your numbers : ").split()
results = []

for i in strings:
	number = 0
	try:
		number = int(i)
	except ValueError:
		print "Some of the values entered are not numbers."
		exit(1)
		
	results.append((number, sqrt(((2 * c * number) / h))))
	
for i in results:
	print "%d : %d  " % (i[0], i[1]),