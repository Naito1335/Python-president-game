class Card:
    CARD_VALUE = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'V': 8, 'D': 9, 'R': 10, 'A': 11,
                  '2': 12}
    NUMBER = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'D', 'R', 'A')
    COLOR = ('♥', '♦', '♣', '♠')

    def __init__(self, number, color):
        value = Card.CARD_VALUE[number]
        self.card = [color,number]

        print(self.card)

    def

class Deck:
    def __init__(self):
        self.cards = []
        for color in Card.COLOR:
            for card in Card.NUMBER:
                card = Card(card, color)
                self.cards.append(card)