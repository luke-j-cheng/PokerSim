from cards import *
from Nutsearch import *
import random


def main():
    players = int(input("Enter number of Players: "))
    while (2 > players) or (players > 8):
        players = int(input("Must be at least two players (max 8 players): "))

    playerhands = []
    
    for i in range (players):
        hand = []
        c1 = random.choice(cardlist)
        cardlist.remove(c1)
        c2 = random.choice(cardlist)
        cardlist.remove(c2)
        hand.append(c1)
        hand.append(c2)
        playerhands.append(hand)
    
    k = 1
    for i in playerhands: 
        print("Hand" , str(k) + ":") 
        for j in i: print (j)
        k += 1
        print('')
main()