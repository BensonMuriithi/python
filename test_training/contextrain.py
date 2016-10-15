from threading import Lock
lock = Lock()

def dothis():
	lock.acquire()
	raise Exception("An Exception.")
	lock.release()

try:
	dothis()
except:
	print "Got an exception."

lock.release()
print "Will these go."