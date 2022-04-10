if __name__ =='main':
    pass

class Card:
    def __init__(self,colour,value):
        self.colour = colour
        self.value = value
    def __str__(self):
        return f'{self.colour},{self.value}'
    def __repr__(self):
        return f'{self.colour} {self.value}'
