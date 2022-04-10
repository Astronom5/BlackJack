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