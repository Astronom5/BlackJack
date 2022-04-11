"""This is hand module for BlakJack game. It is used in player module."""

from deck import Deck


class Hand:
    """Hand abstraction"""
    def __init__(self):
        self.cards=[]
        self.power()
    def draw(self,deck:Deck, number_of_cards:int):
        """
        This method allows to draw defined number of cards from deck

        Args:
            deck (Deck): Deck object used in game
            number_of_cards (int): Amount of cards taken by the player
        """
        for _ in range(number_of_cards):
            self.cards.append(deck.pop(0))
    def __repr__(self):
        return f'{self.cards}'
    def power(self):
        """
        This method updates power of the player's hand and calculate points.
        Rules of calculating points:
        -cards from 2-10 -> amount of points adequate to card's value
        -figures without Ace -> 10 points
        -Ace -> 1 point if there are more than 2 cards, otherwise 11.
                If there are only two aces on the hand then there are counted as 21.
        """
        self.points=0
        if self.cards:
            for card_index in range(len(self.cards)):
                if isinstance(self.cards[card_index].value,int):
                    self.points = self.points + self.cards[card_index].value
                elif self.cards[card_index].value != 'A':
                    self.points = self.points + 10
                elif len(self.cards)>2:
                    self.points +=1
                elif card_index==0 and self.cards[1].value == 'A':
                    self.points +=10
                else:
                    self.points +=11
        else:
            print('Masz pustę rękę, dobierz karty')
