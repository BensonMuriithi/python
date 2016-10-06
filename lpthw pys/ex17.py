#copying files

from os.path import exists

print "This script copies the contents of one file to another."
prompt = "Enter path of file to copy %s > "

from_path = raw_input(prompt % "from");
if exists(from_path) == False:
	print "File does not exist."
	quit()

open(raw_input(prompt % "to"), 'wb').write(open(from_path, 'rb').read())

print "\n\tComplete.\n"