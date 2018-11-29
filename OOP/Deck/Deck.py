from .Suit import Suit
from.Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.dealt_cards = []

        for suit in Suit:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def shuffle_cards(self):
        return self.cards

    def deal_cards(self, num_of_cards):
        cards_to_deal = []
        for i in range(0, num_of_cards):
            cards_to_deal.append(self.cards.pop())

        self.dealt_cards.append(cards_to_deal)

        return cards_to_deal
