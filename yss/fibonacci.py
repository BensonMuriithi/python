"""generator function for the fibonacci series upto a limit entered by user"""

def make_series(limit = 0):
	a, b = 0, 1
	if limit:
		while a < limit:
			yield a
			a, b = b, b + a
	else:
		#If it gets here, the calling function should have a controlling for loop
			#else this will run till it is interrupted
		while 1:
			yield a
			a, b = b, b + a