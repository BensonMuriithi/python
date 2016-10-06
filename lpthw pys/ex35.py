#multiple functions and branchin
"""this is a simple text based game"""

#from sys import exit
from string import lower

def gold_room():
	print "This room is full of gold. How many bars do you take?"
	
	gold = int(raw_input("Number of bars > "))
	if gold < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
def bear_room():
	print """
	There is a bear here.
	The bear has a bunch of honey.
	The fat bear is in front of another door.
	How are you going to move the bear?"""
	bear_moved = False
	
	while True:
		action = lower(raw_input("> "))
		if "honey" in action or "take" in action:
			dead("The bear looks at you and slaps your face off.")
		elif "taunt" in action and not bear_moved:
			print "The bear has moved from the door. What do you want to do now."
			bear_moved = True
		elif "taunt" in action and bear_moved:
			dead("The bear gets pissed off and bites your leg off.")
		elif "open" in action and bear_moved:
			gold_room()
		else:
			print "Read game again for an appropriate action."
			
def cthulhu_room():
	print """
	Here you see the great evil Cthulhu.
	He, it, stares at you and you go insane.
	Do you flee while you still can or cut off your head?
	"""
	action = lower(raw_input("> "))
	if "flee" in action:
		start()
	elif "cut" in action and "head" in action:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
def dead(msg):
	print msg, "Good bye!"
	quit()
	#exit(0)
	
def start():
	print """
	You are in a dark rom.
	There is a door to your left and right.
	Which one do you take?
	"""
	
	door = lower(raw_input("> "))
	if "left" in door:
		bear_room()
	elif "right" in door:
		cthulhu_room()
	else:
		dead("You fumble about and a swinging axe swings off with you head!")