"""Player module for BlackJack game."""

from hand import Hand

class Player:
    """Player abstraction"""
    def __init__(self,nick):
        self.nick = nick
        self.hand = Hand()
        self.decision = None
    def __repr__(self) -> str:
        return f'{self.nick}\'s cards: {self.hand}'
    def choice(self):
        """
        This is a method that allows a player to make a decision
        wheather to take a card or pass.
        """
        print(f'{self} \nDo You want to hit or stand?')
        decision = None
        while decision not in ('hit','stand'):
            decision = input('Please write hit or stand: ')
        self.decision = decision
