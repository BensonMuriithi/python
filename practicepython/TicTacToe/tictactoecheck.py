"""Determine the winner of any of a game of tic tac toe
	
	The results of the play woll be provided to the program as a
	2 dimensional array of 3 lists which will contain numbers
	indicating the mark on that spot on the board.
	
		1 will represent play by player 1
		2 represent play by player 2
		0 inicates a blank cell
"""

def determine_winner(board):
	"""Returns 0 if there's no winner, 1 or 2 if there's a winnner
		
		As 1 and 2 represent plays by player 1 and player 2 respectively,
		1 or 2 is returned if either player wins.
	"""
	
	#check forward diagonal
	if board[0][0] == board[1][1] == board[2][2]:
		return board[0][0]
	#check backward diagonal
	elif board[0][2] == board[1][1] == board[2][0]:
		return board[0][2]
	
	#check verticals
	for i in xrange(3):
		if board[0][i] == board[1][i] == board[2][i]:
			return board[0][i]
	
	#check horizontals last as they are least likely to win
	for i in xrange(3):
		if board[i][0] and (board[i][0] == board[i][1] == board[i][2]):
			return board[i][0]
	
	return 0

if __name__ == "__main__":
	testboard = [[1,2,2], [2,2,0], [2,1,1]]
	
	winner = determine_winner(testboard)
	if winner:
		print "Player {} won.".format(winner)
	else:
		print "Draw!"
