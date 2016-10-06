"""Functions for printing a TicTacToe gameboard to the console
	
	The gameboard should be represented as a 2 dimensional list of 3 rows and 3 columns
"""

element_process = lambda i: ("X" if i == 1 else ("O" if i == 2 else " "))


def printboard(board):
	print "\n game = [{}]".format("\n\t ".join(["[{}]".format(", ".join(map(element_process, board[x]))) for x in xrange(3)]))

