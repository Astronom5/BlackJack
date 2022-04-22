"""Tests for hand module"""

from hand import Hand
from deck import Deck

#Variables used in tests
list_of_colours =['Spade','Heart','Diamond','Clover']
list_of_ace = ['A']



def test_power_counting_ace():
    """Tests if game properly counts 2 aces"""
    my_deck = Deck(list_of_colours,list_of_ace)
    my_hand = Hand()
    my_hand.draw(my_deck.deck,2)
    my_hand.power()
    assert my_hand.points == 21
    