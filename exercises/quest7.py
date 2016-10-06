"""Create a two-dimensional array of i rows and j columns and have the element value in the i-th row and j-th column of the array be i*j.
The number of rows and colums to be provided by the user in the console and finally print the array"""

entered = raw_input("Enter the number of rows and columns of array (rows, columns) > ").split(",")
i = 0; j = 0
try:
	i = int(entered[0])
	j = int(entered[1])
except(ValueError):
	print "The values entered must be integers"
	exit(1)

complete = []
if i and j:
	unit = []
	for x in range(0, i):
		for y in range(0, j):
			unit.append(x * y)
		complete.append(unit)
		unit = []
		

print complete