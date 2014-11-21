class Player(object):

	def __init__(self, name):
		self.name = name
		self.hand = None
		self.points = 0
		
	def discard(self):
		top_card = self.hand.pop()
		return top_card