"""Card module for BlackJack game"""

class Card:
    """Card abstraction"""
    def __init__(self,colour,value):
        self.colour = colour
        self.value = value
    def __str__(self):
        return f'{self.colour},{self.value}'
    def __repr__(self):
        return f'{self.colour} {self.value}'
