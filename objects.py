class Card:
    def __init__(self,colour,value) -> None:
        self.colour = colour
        self.value = value
        print(self.colour, self.value)
    def __str__(self):
        return f'{self.colour},{self.value}'
    def __repr__(self) -> str:
        return f'{self.colour}, {self.value}'

class Deck:
    def __init__(self,list_of_colours,list_of_values):
        self.deck=[]
        for i in range(len(list_of_colours)):
            for j in range(len(list_of_colours)):
                self.deck.append(Card(list_of_colours[i], list_of_values[j]))
    # def __repr__(self): #### Implement a code that prints a list!
    #     return f'{self.Card.colour}, {self.Card.value}'
list
Ace = Card('Spades', 'A')

list_of_colours =['Spades', 'Trefle']
list_of_values = [2,3]
deck = Deck(list_of_colours,list_of_values)
print(deck.deck)
print(Ace)