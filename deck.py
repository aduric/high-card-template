from card import Card, Rank, Suit
from random import Random

class Deck(object):

	def __init__(self):
		self.cards = [(x,y) for x in Rank for y in Suit]

	def shuffle(self):
		rand = Random()
		for i in range(0,51):
			r = rand.randint(0,51)
			c = self.cards[i]
			self.cards[i] = self.cards[r]
			self.cards[r] = c
			
	def deal(self, num):
		l = self.cards[:num]
		self.cards = self.cards[num:]
		return l

