from card import Card

def card_creation_test():
    test_card = Card('spades','A')
    assert test_card.colour == 'spades'

    