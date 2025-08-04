import random

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Player(object):
    def __init__(self):
        self.cards = random.choices(card_deck, k=2)
        self.score = sum(self.cards)

    def draw_card(self):
        """Draws a card and recalculates score"""
        card = random.choice(card_deck)
        self.cards.append(1 if (card == 11 and (sum(self.cards) + card) > 21) else card)
        self.score = sum(self.cards)

    def has_blackjack(self):
        """Checks if player has blackjack (Ace [11 by default] and a 10 card)"""
        return sorted(self.cards) == [10, 11]

    def is_busted(self):
        """Checks if player is busted-- score is over 21"""
        return self.score > 21