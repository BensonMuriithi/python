"""Game engine for Tic Tac Toe game.
	
	These functions only initialise and organise the game as well as keep the scores
	of players
"""

from tictactoeplay import play_game

def play():
	"""Handle the initialising of games and keeping score"""
	Player1wins = Player2wins = games = 0
	
	do_play = raw_input("Do you wish to play a game of Tic Tac Toe? (y/n) : ").lower()
	if "y" in do_play:
		while 1:
			games += 1
			winner = play_game()
			
			if winner:
				if winner == 1:Player1wins += 1
				elif winner == 2: Player2wins += 1
				
				print "\nPlayer {} wins.\n".format(winner)
			
			else: print "\nDraw!\n"
			print "\tGames Played\tPlayer 1 wins\tPlayer 2 wins\n\t	{}\t	{}	\t{}".format(games, Player1wins, Player2wins)
			
			again = raw_input("\nWould you like to play again? (y/n) : ").lower()
			if "y" in again:
				continue
			else: break
		
if __name__ == "__main__":
	play()

