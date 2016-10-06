#printing file contents

print "\nThis program prints out the contents of a file."
filename = raw_input("Enter name of file to read > ")
txt = open(filename)
print "\n" + txt.read() + "\n"
txt.close()