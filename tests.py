import unittest
from card import Card, Rank, Suit
from deck import Deck

class HighCardTest(unittest.TestCase):


	def test_deck_creation(self):
		deck = Deck()
		self.assertEquals((Rank.Two, Suit.Diamond), deck.cards[0])


	def test_deck_shuffle_sufficient_randomization(self):
		deck = Deck()
		deck.shuffle()
		self.assertNotEqual((Rank.Two, Suit.Diamond), deck.cards[0])


	def test_card_creation(self):
		card = Card(Rank.Ace, Suit.Spade)

		self.assertEqual(Rank.Ace, card.rank)
		self.assertEqual(Suit.Spade, card.suit)

	def test_card_compare(self):
		card1 = Card(Rank.Ace, Suit.Spade)
		card2 = Card(Rank.King, Suit.Diamond)

		self.assertTrue(card1 > card2)
