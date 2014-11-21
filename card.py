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

class ComparableCardMixin(object):
	def __ne__(self, other):
		return not (self.rank == other.rank and self.suit == other.suit)
	def __lt__(self, other):
		if self.rank == other.rank:
			return self.suit < other.suit
		else:
			return self.rank < other.rank
	def __gt__(self, other):
		if self.rank == other.rank:
			return self.suit > other.suit
		else:
			return self.rank > other.rank
	def __eq__(self, other):
		return (self.rank == other.rank and self.suit == other.suit)
	

class Card(ComparableCardMixin):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
