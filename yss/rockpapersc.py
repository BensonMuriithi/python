"""2 player rock paper scissors game where play is entered from input and compared
to return a result. Congratulate  the victorious player and ask if the players
wish a new game."""

import random

comparator = {
	"rock": (0, -1, 1),
	"paper": (1, 0, -1),
	"scissors": (-1, 1, 0)
}

for_single = ("r", "p", "s")

def compare_play(p1s, p2s):
	x = 0 if "r" in p2s else(1 if "p" in p2s else 2)
	y = "rock" if "r" in p1s else("paper" if "p" in p1s else "scissors")
	return comparator[y][x]

def game():
	while True:
			p1 = raw_input("\nPlayer 1 > ").lower()
			#p2 = raw_input("Player 2 > ").lower()
			p2 = for_single[random.randint(0, 2)]
			print "Player 2 > " + p2
			
			result = compare_play(p1, p2)
			if result: print "\nPlayer %d wins." % (1 if result == 1 else 2); break;
			else: continue

def play():
	print "This is a text based Rock Paper Scissors game."
	print "Enter your input as:\n"
	print "\t'R' for Rock\t'P' for Paper\t'S' for Scissors\n"
	print "\t\tMay the \"best\" player win."
	
	while True:
		game()
		play_again = raw_input("\nWould you like to play again? > ").lower()
		if play_again in ("y", "yes", "yea", "yeah"): continue
		else: break