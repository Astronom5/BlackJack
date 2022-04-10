from game import Game

list_of_colours =['Spade','Heart','Diamond','Clover'] ### transfer it to Deck?
list_of_values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] ### transfer it to Deck?
list_of_nicknames=['Tata', 'Mateusz']
game = Game(list_of_nicknames,list_of_colours,list_of_values,5)
game.play()