from .Suit import Suit


class Card():
    def __init__(self, suit, value):
        if isinstance(suit, Suit) is False:
            raise ValueError
        else:
            self.suit = suit

        if (1 <= value <= 13) is False:
            raise ValueError('Face value is out of range')
        else:
            self.value = value
