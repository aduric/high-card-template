from random import Random

class Player(object):

	def __init__(self, name):
		self.name = name
		self.hand = None
		self.points = 0
		
	def discard(self):
		rand = Random()
		r = rand.randint(0, self.hand.count() - 1)
		c = self.hand[r]
		self.hand.remove(r)
		return c
		