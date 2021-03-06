"""A basic tictactoe game to be played from the console

	Input of the game will be entered as coordinates of the form (x,y)
	where x is the row and y the column and they are both numbers
	with a minimum number of 1 and a maximum of 3
"""

import tictactoecheck as gamechecker
import gameboardtoscreen as gameprinter

def introduceplayers():
	"""Prints a text file that contains introductory information about the game.
	
		Information in the file includes instructions on how to play the game."""
	with open("gameintro.txt", 'r') as f:
		print f.read()
		
def get_playermove(player):
	"""Processes return it as a tuple of coordinates.
	
		If the input is invalid in any way that will affect the game
		The player is notified and the function repeats recursively"""
	
	rr = raw_input("\nPlayer {} >> ".format(player))
	move = rr.split(",")
	try:
		#if coordinates were actually entered
		if len(move) != 2:
			move = rr.split()
			if len(move) != 2:
				raise ValueError
		x, y = int(move[0]), int(move[1])
		
		#the coordinates be within range
		if all((0 < x < 4, 0 < y < 4)):
			return (x, y)
		else:
			print "\nThe first column or row is 1 and the final is 3"
			print "Please re-enter correctly."
			return get_playermove(player)
	except ValueError:
		#if coordinates not entered or not integers
		print "Please enter only the row and column as numbers separated by a comma eg(1, 1)"
		return get_playermove(player)

def play_game():
	"""Handle playing of Tic Tac Toe game"""
	
	introduceplayers()
	
	#just for fun
	board = [[0 for j in xrange(3)] for i in xrange(3)]
	free_slots = 9
	
	a, b = 1, 2
	
	winner = 0
	while free_slots and not winner:
		playermove = get_playermove(a)
		while board[playermove[0]-1][playermove[1]-1]:
			#prevent playing a move that's already played
			print "\nThat move has already been played. Please play another."
			playermove = get_playermove(a)
		
		board[playermove[0]-1][playermove[1]-1] = a
		free_slots -= 1
		a, b = b, a
		
		#print the game to the screen
		gameprinter.printboard(board)
		
		if (9 - free_slots) >= 5:
			#minimum number of moves that can be made for any player to win is 5
				#so start checking for a winner after 5 moves
			winner = gamechecker.determine_winner(board)
		
	
	return winner
