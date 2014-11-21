import unittest
from card import Card
from deck import Deck

class HighCardTest(unittest.TestCase):

	def test_deck_shuffle_sufficient_randomization(self):
		deck = Deck()
		result = deck.shuffle()
		self.assertEqual(4, result)

