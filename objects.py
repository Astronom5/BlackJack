from random import shuffle


class Card:
    def __init__(self,colour,value):
        self.colour = colour
        self.value = value
        print(self.colour, self.value)
    def __str__(self):
        return f'{self.colour},{self.value}'
    def __repr__(self):
        return f'{self.colour} {self.value}'

class Deck:
    def __init__(self,list_of_colours,list_of_values):
        self.deck=[]
        for i in range(len(list_of_colours)):
            for j in range(len(list_of_values)):
                self.deck.append(Card(list_of_colours[i], list_of_values[j]))
    def shuffle(self):
        shuffle(self.deck)


#### Do napisania player, krupier (przewidziane do rozwoju w multiplayer)
class Player:
    def __init__(self,nick):
        self.nick = nick
class Hand:
    cards = None
    def __init__(self):
        self.cards=[]
    def draw(self,deck):
        self.cards.append(deck.pop(0))
    def __repr__(self):
        return f'{self.cards} {self.cards}'
    def power(self):
        


Ace = Card('Spades', 'A')

list_of_colours =['Spade','Heart','Diamond','Clover']
list_of_values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
deck = Deck(list_of_colours,list_of_values)
print(deck.deck)
deck.shuffle()
print(Ace)
my_hand = Hand()
my_hand.draw(deck.deck)
print(my_hand.cards)


