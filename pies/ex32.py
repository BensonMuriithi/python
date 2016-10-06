#introduction to for loops and lists

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#for loop to go through list items
for number in the_count:
	print "This is count %d" %number
	
for fruit in fruits:
	print "A fruit of type", fruit
	
#lists can also contain items that aren't of the same type
for item in change:
	#when printing items in a mixed list using string formatting, use %r as the type is unknown
	print "I got %r" % item
	
#lists can also be built but one has to start with loops
#an actual list even if it is empty
elements = range(0, 6)

for i in elements:
	print "Element was: %d" % i