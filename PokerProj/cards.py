## Card Classes

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.name} of {self.suit}"


class Ace(Card):
    def __init__(self, suit):
        self.name = "Ace"
        self.suit = suit
        self.value = 14

class Two(Card):
    def __init__(self, suit):
        self.name = "Two"
        self.suit = suit
        self.value = 2

class Three(Card):
    def __init__(self, suit):
        self.name = "Three"
        self.suit = suit
        self.value = 3

class Four(Card):
    def __init__(self, suit):
        self.name = "Four"
        self.suit = suit
        self.value = 4

class Five(Card):
    def __init__(self, suit):
        self.name = "Five"
        self.suit = suit
        self.value = 5

class Six(Card):
    def __init__(self, suit):
        self.name = "Six"
        self.suit = suit
        self.value = 6

class Seven(Card):
    def __init__(self, suit):
        self.name = "Seven"
        self.suit = suit
        self.value = 7

class Eight(Card):
    def __init__(self, suit):
        self.name = "Eight"
        self.suit = suit
        self.value = 8

class Nine(Card):
    def __init__(self, suit):
        self.name = "Nine"
        self.suit = suit
        self.value = 9

class Ten(Card):
    def __init__(self, suit):
        self.name = "Ten"
        self.suit = suit
        self.value = 10

class Jack(Card):
    def __init__(self, suit):
        self.name = "Jack"
        self.suit = suit
        self.value = 11

class Queen(Card):
    def __init__(self, suit):
        self.name = "Queen"
        self.suit = suit
        self.value = 12

class King(Card):
    def __init__(self, suit):
        self.name = "King"
        self.suit = suit
        self.value = 13

cardlist = []
spadelist = []
clublist = []
heartlist = []
diamondlist = []       
    
suitlist = ["Spades", "Diamonds", "Hearts", "Clubs"]
ranklist = [Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King]

for suit in suitlist:
    for rank in ranklist:
        a = rank(suit)
        if suit == "Spades":
            spadelist.append(a)
        elif suit == "Diamonds":
            diamondlist.append(a)
        elif suit == "Hearts":
            heartlist.append(a)
        else:
            clublist.append(a)
        cardlist.append(a)
