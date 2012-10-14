
from random import shuffle

suits = frozenset(['clubs', 'diamonds', 'hearts', 'spades'])
values = frozenset(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

class card:
        def __init__(self, suit, val):
                self.suit = suit
                self.val = str(val)
        
        def __str__(self):
                return "{0}{1}".format(self.val, self.suit)
                
        def __repr__(self):
                return "{0} of {1}".format(self.val, self.suit)
                

class deck:
        def __init__(self):
                self.cards = [card(suit, val) for suit in suits for val in values]
                self.is_shuffled = False

        def __str__(self):
                string = ""
                for card in self.cards:
                        string += '%s of %s, ' % (card.suit, card.val)
                return string

        def shuffle(self):
                shuffle(self.cards)
                self.is_shuffled = True

        def pop(self):
                if len(self.cards) == 0:
                        return None
                return self.cards.pop()
