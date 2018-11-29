from .Card import Card


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if isinstance(card, Card) is False:
            return False

        self.cards.append(card)

        return True

    def total_cards(self):
        return len(self.cards)
