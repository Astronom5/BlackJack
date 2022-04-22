"""Tests for game module"""

from game import Game

#Variables used in tests (only for proper game creation)
list_of_colours =['Spade','Heart','Diamond','Clover']
list_of_values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
list_of_nicknames=['Tata', 'Mateusz']

def test_croupier_presence():
    """Tests if croupier exists at the end of the list"""
    my_game = Game(list_of_nicknames,list_of_colours,list_of_values,5)
    assert my_game.list_of_players[-1].nick == 'Croupier'
