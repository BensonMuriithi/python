#simple text editor

from sys import argv

script, filename = argv

print """
We are going to erase %r.
If you DO NOT want that hit CTRL-C (^C).
If you DO want that hit ENTER.
""" % filename

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

#print "Truncating the file.    Goodbye!"
#target.truncate()
print "Now I'm going to ask you for three lines and write them to the file."

i = 1
while i <= 3:
	line = raw_input("line %d: " %i)
	target.write(line)
	target.write("\n")
	i = i + 1

print "and finally, we close the file."
target.close()