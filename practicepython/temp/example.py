def make_cool(a):
	def shell(func):		
		def wrapper(*args, **kwgs):
			print a
			print "The solution is ",
			print func(*args, **kwgs)
			print "Thank you!"
		
		return wrapper
	
	return shell

@make_cool(1)
def domath(n):
	return n**0.7
	
domath(15)