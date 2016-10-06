#function returns

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" %(a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Math with functions."
age = add(15, 5)
height = subtract(200, 32)
weight = multiply(8, 8)
iq = divide(2720, 16)

print "Age: %d, height: %d, weight %d, IQ: %d" % (age, height, weight, iq)

print "Some outcome:", add(age, subtract(height, multiply(weight, divide(iq, 2)))), ". Good."