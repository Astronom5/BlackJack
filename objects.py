from random import shuffle


class Card:
    def __init__(self,colour,value):
        self.colour = colour
        self.value = value
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


class Player:
    def __init__(self,nick):
        self.nick = nick
        self.hand = Hand()
    def __repr__(self) -> str:
        return f'{self.nick}, {self.hand}'


class Hand:
    cards = None
    def __init__(self):
        self.cards=[]
    def draw(self,deck, number_of_cards):
        for i in range(number_of_cards):
            self.cards.append(deck.pop(0))
    def __repr__(self):
        return f'{self.cards}'
    def power(self):
        self.points = 0 # Optionally change names between power and points.
        if self.cards != []:
            for x in range(len(self.cards)):
                print(self.cards[x])
        else:
            ####ERROR Exception needed        
        #Needed to be updated Rules : numbers -> number value, figures -> 10 Ace -> 1 or 11, 2 Aces ->21 (if at start)
            pass


class Game:
    pass

list_of_colours =['Spade','Heart','Diamond','Clover'] ### transfer it to Deck?
list_of_values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] ### transfer it to Deck?
deck = Deck(list_of_colours,list_of_values)
print(deck.deck)
deck.shuffle()
Me = Player('Astronom')
Me.hand.draw(deck.deck,10)
print(Me)
Me.hand.power()


