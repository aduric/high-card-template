class HighCardGame(object):

	def __init__(self, deck, player1, player2):
		self.deck = deck
		self.player1 = player1
		self.player2 = player2
		
	def play(self):
		self.deck.shuffle()
		
		cut = 52 / 2;
		self.player1.hand = self.deck[:cut]
		self.player2.hand = self.deck[cut:]
		
		for i in range(1, cut):
			if self.player1.discard() < self.player2.discard():
				self.player2.points = self.player2.points + 1
			elif self.player1.discard() > self.player2.discard():
				self.player1.points = self.player1.points + 1
				
		if self.player1.points > self.player2.points:
			echo "Player " + self.player1.name + " wins!"
		elif self.player1.points > self.player2.points:
			echo "Player " + self.player2.name + " wins!"
		else:
			echo "It's a tie!"
