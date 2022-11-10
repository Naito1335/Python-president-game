class Card:
    card_value = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'V': 8, 'D': 9, 'R': 10, 'A': 11,
                  '2': 12}
    card = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'D', 'R', 'A')
    color = ('♤', '♡', 'T', 'C')


class Deck:
    def __init__(self):
        self.cards = []
        for color in Card.color:
            for card in Card.card:
                card = Card(card, color)
                self.cards.append(card)

#     def __repr__(self):
#         return repr(self.cards)
#
#
# print(repr(Deck()))
