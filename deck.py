from card import Card, Rank, Suit

class Deck(object):

	def __init__(self):
		self.cards = [(x,y) for x in Rank for y in Suit]

	def shuffle(self):
		pass
