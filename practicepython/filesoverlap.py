"""From two text files, print the numbers or words that appear in both files"""

import os

def get_overlap(_file1, _file2):
	with open(_file1, 'r') as f1, open(_file2, 'r') as f2:
		return set(f1.read().split()).intersection(set(f2.read().split()))

		
if __name__ == "__main__":
	print "\nGet words or numbers that occur in two files.\n"
	
	fname1 = raw_input("Enter the first file >> ").lower()
	while not os.path.isfile(fname1):
		print "File doesn't exist\n"
		fname1 = raw_input("Enter the first file >> ").lower()
		
	fname2 = raw_input("Enter the second file >> ").lower()
	while not os.path.isfile(fname2):
		print "File doesn't exist\n"
		fname2 = raw_input("Enter the second file >> ").lower()
		
	print "\n"
	for s in get_overlap(fname1, fname2): print s + "  ",
	print "\n"

