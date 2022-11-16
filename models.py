import random
import names
# pip freeze > requirements.txt


class Card:
    CARD_VALUE = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'V': 8, 'D': 9, 'R': 10, 'A': 11,
                  '2': 12}
    NUMBER = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'D', 'R', 'A')
    COLOR = ('♥', '♦', '♣', '♠')

    def __init__(self, number, color):
        self.value = Card.CARD_VALUE[str(number)]
        self.card = [number, color]

        print(self.card)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class Deck:

    def __init__(self):
        self.cards = []
        for color in Card.COLOR:
            for card in Card.NUMBER:
                card = Card(card, color)
                self.cards.append(card)

    def shuffle(self):

        random.shuffle(self.cards)
        return self.cards


class Player:
    name = ''
    hand = [Card]

    def __init__(self, name: str = None):
        if self.name is not None:
            self.name = name
        else:
            names.get_first_name()

    def __str__(self):
        return self.name
