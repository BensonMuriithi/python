from contextlib import contextmanager

@contextmanager
def open_file(p):
	f = open(p)
	yield f
	f.close()

def xx():
	fs = []
	for i in xrange(20):
		with open_file("E:\\file.txt") as f:
			fs.append(f)
	
	if any((not f.closed for f in fs)):
		print "Yeah! You have some leaks."
	else:
		print "Context manager works brilliantly man!"

if __name__ == "__main__":
	xx()