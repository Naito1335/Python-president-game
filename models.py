import random
import names
# pip freeze > requirements.txt


class Card:
    CARD_VALUE = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'V': 8, 'D': 9, 'R': 10, 'A': 11,
                  '2': 12}
    NUMBER = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'V', 'D', 'R', 'A')
    COLOR = ('♥', '♦', '♣', '♠')

    def __init__(self, number, color):
        """Constructor of the card

        Args:
            number: number of the card between 2 and 'A'.
            color: the color of the card ( ♥,♦,♠,♣,).
        """
        self.value = Card.CARD_VALUE[str(number)]
        self.card = [number, color]

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class Deck:

    def __init__(self):
        """Constructor of the deck of 52 cards"""

        self.cards = []
        for color in Card.COLOR:
            for card in Card.NUMBER:
                card = Card(card, color)
                self.cards.append(card)

    def shuffle(self):
        """Function that shuffle the deck randomly"""
        random.shuffle(self.cards)
        return self.cards


class Player:
    name = ''

    def __init__(self, name: str = None):
        """Constructor that sets up a name up for the players"""
        if self.name is not None:
            self.name = name
        else:
            names.get_first_name()

        self.hand = []

    def __str__(self):
        """This function transforms name into a string"""
        return self.name

    def add_to_hand(self):
        """This function adds a card in the hand of the player"""
        self.hand.append()

    def remove_from_hand(self):
        """This function removes a card in the hand of the player"""
        self.hand.remove()

    # def play(self):


class PresidentGame:
    players = []

    def __init__(self):
        """Constructor that initializes the list of players"""
        self.deck = Deck()
        for i in range(3):
            self.players.append(Player())

    def distribute_cards(self):
        """Function that distributes cards evenly among players"""

        for player in self.players:
            for i in range (17):
                player.add_to_hand(self.deck.cards.pop())