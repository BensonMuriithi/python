#variables and format strings

x = "There are %d types of people." % 10
binary = "binary"
dont = "don't"
y = "Those who know %s and those who %s." % (binary, dont)

print x;print y #2 separate print statements

print "I said: %r." % x
print "I also said: %r." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious #the hilarious var is what's represented by the format variable within joke_evaluation

w = "This is the left side of..."
e = "a string with a right side."

print w + e #join the variables as they are and print them with and space between them