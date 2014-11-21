import unittest
from card import Card, Rank, Suit
from deck import Deck
from game import HighCardGame
from player import Player

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
		
	def test_player_discard_top_card_no_cards(self):
		pass
		
	def test_player_discard_top_card(self):
		pass
		
	def test_player_increment_points(self);
		pass
		
	def test_game_deal(self):
		highcard = Game(Deck(), Player("player1"), Player("player2"))
		
	def test_game_play_no_cards_left(self):
		pass
		
		
