"""simple text game"""
#introduction to making decision by exploiting if elif and else

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating cheese cake. What do you do?"
	print "\n1. Take the cake."
	print "2. Scream at the bear."
	
	bear_action = raw_input("> ")
	if bear_action == "1":
		print "The bear eats you face off. Good job sucker!"
	elif bear_action == "2":
		print "The bear eats your legs off. Good try!"
	else:
		print "Well doing %s gets you killed, sorry. Good game!" % bear_action

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Bluberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	if insanity == "1" or insanity == "2":
		print "Your body survives but your brain becomes jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
else:
	print "As you fumble around, the ground beneath you crumbles and you fall \ninto a pit of burning sulphur. Good try!"