"""Calculate the value of a+aa+aaa+aaaa where a  is a value entered by at the console"""

num = raw_input("Enter your number: ")

#The number is a string so you can concatenate upon it with + or multiply it
print "%d" % (int(num) + int(num+num) + int(num*3) + int(num*4))