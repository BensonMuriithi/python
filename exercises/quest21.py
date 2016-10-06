"""Track the movements of a robot from a point (0, 0)
The bot can move UP, DOWN, LEFT or RIGHT and the directions taken will be entered at the console
The program finalizes by printing the floor integer of the distance the bot is at from it's starting point"""

from math import trunc
from math import sqrt
position = [0, 0]

print "Track the movement of brimbot from point (0,0).\n"

while True:
	mvmnt = raw_input("Enter robot movement: ").split()
	
	if not mvmnt: break
	
	if mvmnt[0].upper() == "UP": position[1] += int(mvmnt[1])
	elif mvmnt[0].upper() == "DOWN": position[1] -= int(mvmnt[1])
	elif mvmnt[0].upper() == "RIGHT": position[0] += int(mvmnt[1])
	elif mvmnt[0].upper() == "LEFT": position[0] -= int(mvmnt[1])
	else:
		print "This entry is invalid. It will be disregarded.\n"
		
print "Distance from starting point: %d" % trunc(round(sqrt((position[0]**2) + (position[1]**2))))