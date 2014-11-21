class HighCardGame(object):

	def __init__(self, deck, player1, player2):
		self.deck = deck
		self.player1 = player1
		self.player2 = player2
		
	def play(self):
	
		deck.shuffle()
		self.play_round()
					
		if self.player1.points > self.player2.points:
			echo "Player " + self.player1.name + " wins!"
		elif self.player1.points > self.player2.points:
			echo "Player " + self.player2.name + " wins!"
		else:
			echo "It's a tie!"

			
	def play_round(self):
	
		self.player1.hand = deck.deal(3)
		self.player2.hand = deck.deal(3)
	
		if self.player1.discard() < self.player2.discard():
			self.player2.points = self.player2.points + 1
		elif self.player1.discard() > self.player2.discard():
			self.player1.points = self.player1.points + 1
			