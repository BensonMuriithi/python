"""create a dict that will contain th key value pair of (i, i * i) whereby i is an integer provided to the program and print the resulting dictionary"""

n = int(raw_input("Enter number : "))
d = {}

for i in range(1, n+1):
	d[i] = i*i
	
print d