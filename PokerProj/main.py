from cards import *
from Nutsearch import *
from hands import *
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
        
        
        # Adds all community cards to player hands and performs nutsearch func on each hand
        num = 0
        nutlist = []
        for player in playerhands:
            for card in board:
                player.append(card)
            num += 1
            print('')
            print("Player" + str(num) + ":")
            print(nutsearch(player))
            nutlist.append(nutsearch(player))
        
        
        print('')

        besthand = WinSearch(nutlist) # Finds best hand 

        # Prints different win messages based on how many players won, if tiebreak was used, if there was a tie
        
        if besthand[2] == False:  
            print("Player" + str(int(besthand[0])) + " wins with a " + str(besthand[1]))
        elif besthand[2] == True:
            if len(besthand[0]) == 1:
                print("Players " + (str(besthand[0])) + " wins with a higher " + str(besthand[1]))
            if len(besthand[0]) > 1:
                print("Players")
                for i in range (len(besthand[0])):
                    print(str(i + 1))
                print("tie with a " + besthand[1])
        print('')
    

        ## Clears hands/board and resets cards for next game 
        ## Only if user requests to keep playing
        enter = input("Press enter to play again or Q to quit: ").strip()
        if enter.lower() == 'q':
            break
        

        for hand in playerhands:
            for card in hand:
                if card not in cardlist:
                    cardlist.append(card)
                

        for card in board:
            cardlist.append(card)
        
        playerhands.clear()
        board.clear()

        
        
                  

if __name__ == main():
    main()