from hand import Hand

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