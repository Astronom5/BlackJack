"""Tests for card module"""
from card import Card

def test_card_creation():
    """Checks if card is properly created"""
    test_card = Card('spades','A')
    assert test_card.colour == 'spades'
    assert test_card.value == 'A'

def test_card_types():
    """Checks if card's value or card's colour types are valid"""
    test_card = Card('spades',2)
    assert isinstance(test_card.colour, str)
    assert isinstance(test_card.value, (str,int))
    