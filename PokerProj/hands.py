class Hand:
    def __init__(self, name, score, highnum, high):
        self.name = name
        self.score = score
        self.highnum = highnum
        self.high = high
    def __str__(self):
        return f"{self.name}"


class SFWin(Hand):
    def __init__(self, high):
        self.name = "Straight Flush"
        self.score = 9
        self.highnum = 1
        self.high = high

class QuadWin(Hand):
    def __init__(self, high):
        self.name = "Four of a Kind"
        self.score = 8
        self.highnum = 2
        self.high = high

class FHWin(Hand):
    def __init__(self, high):
        assert isinstance(high, list)
        assert len(high) == 2
        self.name = "Full House"
        self.score = 7
        self.highnum = 2
        self.high = high

class FlushWin(Hand):
    def __init__(self, high):
        self.name = "Flush"
        self.score = 6
        self.highnum = 5
        self.high = high

class StraightWin(Hand):
    def __init__(self, high):
        self.name = "Straight"
        self.score = 5
        self.highnum = 1
        self.high = high

class SetWin(Hand):
    def __init__(self, high):
        self.name = "Three of a Kind"
        self.score = 4
        self.highnum = 3
        self.high = high

class TwoPairWin(Hand):
    def __init__(self, high):
        self.name = "Two Pair"
        self.score = 3
        self.highnum = 3
        self.high = high

class PairWin(Hand):
    def __init__(self, high):
        self.name = "Pair"
        self.score = 2
        self.highnum = 4
        self.high = high

class HighWin(Hand):
    def __init__(self, high):
        self.name = "High Card"
        self.score = 1
        self.highnum = 5
        self.high = high