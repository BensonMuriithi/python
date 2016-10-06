"""Program to compute the factorial(s) of a set of given number(s)
The results are printed separated by commas on a single line"""

string = raw_input("Enter your number(s) for factorial(s) : ")
separated = string.split()
results = []

for i in separated:
	number = None
	try:
		number = int(i)
	except ValueError:
		print "Some of the values entered are not numbers."
		exit(1)
		
	fact = 1
	while number > 0:
		fact *= number
		number -= 1
		
	results.append((int(i), fact))
	
for i in results:
	print "%d: %d  " % (i[0], i[1]),