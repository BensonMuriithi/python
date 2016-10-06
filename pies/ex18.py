#functions

def print2(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_one(arg):
	print "arg1: %r" % arg
	
def print_none():
	print "I've got no arguments :-("
	
print2("Benson", "Muriithi")
print_two_again("Muriithi", "Benson")
print_one("Benson")
print_none()