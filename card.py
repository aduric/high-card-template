from enum import Enum

class Suit(Enum):
	Diamond = 1
	Heart = 2
	Club = 3
	Spade = 4

class Rank(Enum):
	Two = 2
	Three = 3
	Four = 4
	Five = 5
	Six = 6
	Seven = 7
	Eight = 8
	Nine = 9
	Ten = 10
	Jack = 11
	Queen = 12
	King = 13
	Ace = 14

class Card(object):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
