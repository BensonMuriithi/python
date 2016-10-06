"""Compare the performance of my custom search algorithms against python's

	My binarysearch against python's in keyword"""

from clocking import timeit
import imp

bs = imp.load_source("binarysearch2", "../binary search/binarysearch2.py")
mine = imp.load_source("binarysearch", "../binary search/binarysearch.py")
x = list(xrange(0,10000000,3))

y = "Compare the performance of my custom"
z = "perform"
@timeit
def mysearch():
	for i in xrange(10):
		mine.is_in(x, i)
	
@timeit
def pysearch():
	for i in xrange(10):
		i in x

@timeit
def binary2search():
	for i in xrange(1000):
		bs.search(x, i)

@timeit
def binary2str():
	for i in xrange(100000):
		bs.search(y, z)

@timeit
def pystr():
	for i in xrange(100000):
		z in y

if __name__ == "__main__":
	print pysearch()
	print binary2search()
	print pystr()
	print binary2str()

