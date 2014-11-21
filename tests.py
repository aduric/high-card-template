import unittest
from card import Card, Rank, Suit
from deck import Deck

class HighCardTest(unittest.TestCase):

	def test_deck_shuffle_sufficient_randomization(self):
		deck = Deck()
		result = deck.shuffle()
		self.assertEqual(4, result)

	def test_card_creation(self):
		card = Card(Rank.Ace, Suit.Spade)

		self.assertEqual(Rank.Ace, card.rank)
		self.assertEqual(Suit.Spade, card.suit)
