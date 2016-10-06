"""Decorator that takes arguments"""

def decorator(arg1, arg2):
	def real_decorator(f):
		def wrapper(*args, **kwargs):
			print "Congrats. You've made a decorator that takes arguments like %s, %s" % (str(arg1), str(arg2))
			f(*args, **kwargs)
		return wrapper
	return real_decorator
	
@decorator(13,55)
def print_args(*args):
	for i in args: print i,
	
print_args(range(4))
