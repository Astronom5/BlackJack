if __name__ =='main':
    pass

from random import shuffle
from card import Card

class Deck:
    def __init__(self,list_of_colours,list_of_values):
        self.deck=[]
        for i in range(len(list_of_colours)):
            for j in range(len(list_of_values)):
                self.deck.append(Card(list_of_colours[i], list_of_values[j]))
    def shuffle(self):
        shuffle(self.deck)