"""Deck module for BlackJack game."""
from random import shuffle
from card import Card

class Deck:
    """Deck abstraction"""
    def __init__(self,list_of_colours,list_of_values):
        self.deck=[]
        for i in range(len(list_of_colours)):
            for j in range(len(list_of_values)):
                self.deck.append(Card(list_of_colours[i], list_of_values[j]))
    def shuffle(self):
        """
        This method shuffles deck in place
        """
        shuffle(self.deck)
