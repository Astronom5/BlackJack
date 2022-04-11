"""Game module for BlackJack game. It integrates all modules."""
from deck import Deck
from player import Player


class Game:
    """Game abstraction"""
    def __init__(self,list_of_nicknames,list_of_colours,list_of_values,number_of_players:int):
        self.max_players = number_of_players
        self.list_of_players = []
        self.deck = Deck(list_of_colours,list_of_values)
        self.deck.shuffle()
        if len(list_of_nicknames)<self.max_players:
            list_of_nicknames.append('Croupier') # Guaranteed croupier at the end of the list
            self.list_of_players = [Player(nick) for nick in list_of_nicknames]
            for player in self.list_of_players:
                player.hand.draw(self.deck.deck,2)
                player.hand.power()
        else:
            print('Too many players, somebody must resign')
    def play(self):
        """This method is responsible for playing logic. The game continues until all players stand.
           After that croupier (player at the end of the list) starts to play.
           Then the end method is called.
        """
        end_flag = 0
        while end_flag !=1:
            end_flag = 1
            for player in self.list_of_players[:-1]:
                if player.decision != 'stand':
                    print('-'*20)
                    print(self)
                    print('-'*20)
                    player.choice()
                    if player.decision != 'stand':
                        player.hand.draw(self.deck.deck,1)
                        end_flag = 0
        while self.list_of_players[-1].hand.points <17:
            self.list_of_players[-1].hand.draw(self.deck.deck,1)
            self.list_of_players[-1].hand.power()
        self.end()
    def __repr__(self):
        return f'{self.list_of_players[:-1]},'\
        + f' Croupier\'s card: {self.list_of_players[-1].hand.cards[0]}'
    def end(self):
        """This is the method that sumarizes results of the game.
        """
        print('-'*20)
        for player in self.list_of_players:
            player.hand.power()
            print(f'{player} and power of it\'s cards is {player.hand.points}')
        print('-'*20)
