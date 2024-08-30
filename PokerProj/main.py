from cards import *
from Nutsearch import *
import random

def main():
    while True:
        ## Gets an amount of players between 2 and 8        
        players = int(input("Enter number of Players: "))
        while (2 > players) or (players > 8):
            players = int(input("Must be at least two players (max 8 players): "))

        playerhands = []
        board = []
        
        ## Deals unique cards to each player
        for i in range (players):
            hand = []
            c1 = random.choice(cardlist)
            cardlist.remove(c1)
            c2 = random.choice(cardlist)
            cardlist.remove(c2)
            hand.append(c1)
            hand.append(c2)
            playerhands.append(hand)
        

        ## Displays Player Hands for each Player
        k = 1
        for i in playerhands: 
            print("Hand" , str(k) + ":") 
            for j in i: print (j)
            k += 1
            print('')
        
        ## Deals community cards
        f = input("Press Enter to see the Flop: ")
        for i in range (3):
            c = random.choice(cardlist)
            cardlist.remove(c)
            board.append(c)
        print('')
        for i in board:
            print(i)
        print('')
        f = input("Press Enter to see the turn: ")
        c = random.choice(cardlist)
        cardlist.remove(c)
        board.append(c)
        print('')
        print(c)
        print('')


        f = input("Press Enter to see the River: ")
        c = random.choice(cardlist)
        cardlist.remove(c)
        board.append(c)
        print('')
        print(c)
        print('')
        print("Shared Cards: ")
        print('')
        for i in board:
            print(i)
        

        for player in playerhands:
            for card in board:
                player.append(i)
            print(FullHouse(player))
        
    

        ## Clears hands/board and resets cards for next game 
        ## Only if user requests to keep playing
        enter = input("Press enter to play again or Q to quit: ").strip()
        if enter.lower() == 'q':
            break
        
        for hand in playerhands:
            for card in hand:
                cardlist.append(card)
                

        for card in board:
            cardlist.append(card)
        
        playerhands.clear()
        board.clear()

        
        
                  

if __name__ == main():
    main()