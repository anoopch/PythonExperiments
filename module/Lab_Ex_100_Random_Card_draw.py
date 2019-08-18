# Python program to shuffle a deck of card using the module random and draw a card

import random


def draw_card():
    card_types = ['Spade', 'Heart', 'Diamond', 'Club']

    # return a random card
    return str(random.randint(1, 14)) + " of " + card_types[random.randint(0, 3)]


print(draw_card())
