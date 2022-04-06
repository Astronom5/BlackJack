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
        self.decision = None
    def __repr__(self) -> str:
        return f'{self.nick}\'s cards: {self.hand}'
    def choice(self):
        print(f'{self} \nDo You want to hit or stand?')
        decision = None
        while decision != 'hit' and decision != 'stand':
            decision = input('Please write hit or stand: ')
        self.decision = decision



class Hand:
    cards = None
    points = 0
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
                print(self.cards[x]) # Need to be deleted durin cleaning the code
                if isinstance(self.cards[x].value,int):
                    self.points = self.points + self.cards[x].value
                elif self.cards[x].value != 'A':
                    self.points = self.points + 10
                elif len(self.cards)>2:
                    self.points +=1
                elif x==0 and self.cards[1].value == 'A':
                    self.points +=10
                else:
                    self.points +=11
        else:
            print('Masz pustę rękę, dobierz karty')       


class Game:
    def __init__(self,list_of_nicknames,list_of_colours,list_of_values,number_of_players):
        self.max_players = number_of_players
        self.list_of_players = []
        self.deck = Deck(list_of_colours,list_of_values)
        self.deck.shuffle()
        if len(list_of_nicknames)<self.max_players:
            list_of_nicknames.append('Croupier') ## In this case croupier will always be at the end of the list of players
            self.list_of_players = [Player(nick) for nick in list_of_nicknames] ## List comprehension
            for player in self.list_of_players:
                player.hand.draw(self.deck.deck,2)
        else:
            print('Too many players, somebody must resign')
    def play(self):
        end_flag = 0
        while end_flag !=1:
            end_flag = 1
            for player in self.list_of_players[:-1]:
                if player.decision != 'stand':
                    print(self.list_of_players[:-1])
                    player.choice()
                    if player.decision != 'stand':
                        player.hand.draw(self.deck.deck,1)
                        end_flag = 0  
        while self.list_of_players[-1].hand.points <17:
            self.list_of_players[-1].hand.draw(self.deck.deck,1)
            self.list_of_players[-1].hand.power()
    def __repr__(self):
        return f'{self.list_of_players[:-1]}, Croupier\'s card: {self.list_of_players[-1].hand.cards[0]}'



#####Code testing##############
list_of_colours =['Spade','Heart','Diamond','Clover'] ### transfer it to Deck?
list_of_values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] ### transfer it to Deck?
deck = Deck(list_of_colours,list_of_values)
# print(deck.deck)
deck.shuffle()
Me = Player('Astronom')
Me.hand.draw(deck.deck,2)
print(Me)
Me.hand.power()
print(Me.hand.points)
hand=Hand()
hand.power()
game = Game(list_of_colours,list_of_colours,list_of_values,5)
print(game)
print(len(deck.deck))
game.play()
Me.choice()
print(game.list_of_players[-1])



