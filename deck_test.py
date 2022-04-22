"""Tests for deck module"""
from card import Card
from deck import Deck

#Variables used in tests
list_of_colours =['Spade','Heart','Diamond','Clover']
list_of_values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']


def test_deck_creation():
    """Tests if created deck is valid (has 52 objects in type card)"""
    test_deck = Deck(list_of_colours,list_of_values)
    assert len(test_deck.deck) == 52
    for index in range(len(test_deck.deck)):
        assert isinstance(test_deck.deck[index],Card)

def test_deck_shuffle():
    """Tests if shuffle works properly"""
    test_deck = Deck(list_of_colours,list_of_values)
    cards = test_deck.deck[:]
    test_deck.shuffle()
    assert test_deck.deck != cards
