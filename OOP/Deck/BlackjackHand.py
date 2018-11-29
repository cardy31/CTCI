from .Hand import *


class BlackjackHand(Hand):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.busted = False

    def add_card(self, card):
        if isinstance(card, Card) is False:
            return False

        if self.busted is False:
            self.cards.append(card)

        if self.get_total() < 21:
            return True
        return False

    def get_total(self):
        total = 0
        for card in self.cards:
            total += card.value

        return total
