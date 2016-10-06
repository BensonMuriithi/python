#functions and files

from sys import argv

script, filename = argv

def print_whole(file):
	print file.read()
	
def rewind(file):
	file.seek(0)
	
def print_singular_lines(lines, file):
	cur = 1
	while cur <= lines:
		text = file.readline()
		if len(text) > 0:
			print "%d: %s" % (cur, text)
		else:
			return
		cur += 1
		
file = open(filename, 'r')

print "Let's print the whole file first:\n"
print_whole(file)

print "Let's go back to the beginning; seeking."
rewind(file)

print "Let's print three lines now:\n"
print_singular_lines(3, file)
file.close()