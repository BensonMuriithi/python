#functions

def cheese_and_crackers(cheese, crackers):
	print "We have %d cheeses." % cheese
	print "You have %d boxes of crackers." % crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
def produce(num):
	return num

prompt = "Enter number of %s > "

#we can give functions numbers directly
cheese_and_crackers(20, 30)

#they can also be given variables from the script
cheese = 10; crackers = 50
cheese_and_crackers(cheese, crackers)

#we can do math within the arguments too
cheese_and_crackers(20 + 40, 60 - 8)

#we can also combine math and variables, it's a free environment
cheese_and_crackers(int(raw_input(prompt % "cheese")), produce(int(raw_input(prompt % "crackers"))))