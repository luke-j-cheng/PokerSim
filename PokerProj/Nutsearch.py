## POKER HAND WIN PICKER ##

from cards import *
from hands import *

#Card Types

def StraightFlush(list): 
    if True:
        return (False, None)
    else:
        return False

def Quads(inlist): 
    hand = []  ## Creates new list hand with the cards containing their numeric values (appears in many following search functions)
    for i in inlist:
        hand.append(i.value)
    quadlist = []
    newlist = set(hand) ## Creates a set of the hand (each numeric value once)
    for value in newlist: ## Searches through each number and counts how often it appears in the hand
        num = hand.count(value)
        if num == 4: ## Adds number to quadlist if four of a kind
            quadlist.append(value)
    if len(quadlist) == 1: ## If there is a four of a kind, search through hand to find highest kicker (tie purposes)
        newlist.remove(quadlist[0]) 
        quadlist.append(max(newlist))
        return (True, QuadWin(quadlist)) # If hand has 4 of a kind, returns True, the value of the quads, and the 5th highcard (tie purposes)
    else:
        return (False, None) # Returns False, None if 4 of a kind NOT in hand

def FullHouse(inlist): 
    hand = [] 
    for i in inlist: 
        hand.append(i.value) ## Takes numeric values from all cards
    threelist = []
    pairlist = []
    score = []
    newlist = set(hand)
    for value in newlist:
        num = hand.count(value)
        if num == 3: ## If count is 3, added to pairlist too in case there are multiple three of kind (can be used for FH)
            threelist.append(value)
            pairlist.append(value)
        elif num == 2: 
            pairlist.append(value)
    if len(threelist) > 0 and len(pairlist) > 0:
        score.append(max(threelist))
        if max(threelist) in pairlist:
            pairlist.remove(max(threelist)) ## Distinguishes Set from Full House
        if len(pairlist) > 0:
            score.append(max(pairlist))
            return(True, FHWin(score)) # Returns
        else:
           return(False, None) 
    else:
        return(False, None)
  
def Flush(inlist): 
    hand = []
    score = []
    value = []
    for i in inlist:
        hand.append(i.suit) ## Adds every card's suit to list
    for suit in suitlist:
        num = hand.count(suit)
        if num >= 5:
            score.append(num)
            flushsuit = suit ## Checks if at least 5 cards are the same suit, sets flushsuit to the suit
    
    if len(score) >= 1:
        for card in inlist: 
            if card.suit == flushsuit:
                value.append(card.value)
        value.sort(reverse=True)
        newval = value[:5] ## Gets the highest number values of the cards that are the same as the flushsuit
        return(True, FlushWin(newval))
    
    else:
        return(False, None)         

def Straight(inlist):
    hand = []
    for i in inlist:
        hand.append(i.value)
    if (14) in hand: ## For Ace's unique straight property (can be used as 12345 or 10JQKA)
        hand.append(1)
    

def Set(inlist):
    hand = []
    for i in inlist: 
        hand.append(i.value)
    score = []
    newlist = set(hand)
    for value in newlist:
        num = hand.count(value)
        if num == 3:
            score.append(value)
            hand.remove(value)
    if len(score) == 1:
        hand.sort(reverse=True)
        score.append(hand[:2])
        return(True, SetWin(score))
    else:
        return(False, None)

def Pair(inlist): #Checks for both Two Pair and Pair
    hand = []
    pairlist = []
    
    for i in inlist:
        hand.append(i.value)
    newlist = set(hand) 
    for value in newlist:
        num = hand.count(value)
        if num == 2:
            pairlist.append(value) ## Adds all values of pairs to pairlist
    
    while len(pairlist) > 2: ## Reduces pairlist to the top 2 pairs (if more than 2)
        pairlist.remove(min(pairlist))
    

    if len(pairlist) == 2: ## Checks if there is a two pair
        pairlist.sort(reverse=True)
        for i in pairlist:
            newlist.remove(i) ## Removes values from set to find highcard
        pairlist.append(max(newlist)) ## Adds necessary highcard
        return(True, TwoPairWin(pairlist))
    
    elif len(pairlist) == 1: ## Checks if there is a pair (if twopair fails)
        newlist.remove(pairlist[0]) ## Removes the pair value from set to find necessary highcards
        for i in range (3):
            pairlist.append(max(newlist))
        return(True, PairWin(pairlist))
    
    else:
        return(False, None)





def HighCard(inlist): #Will be used to break ties by entering modified hands 
    highcard = []
    for card in list:
        highcard.append(card)
    highest = highcard.sort(reverse=True)
    return (HighWin(highest))
    

def nutsearch(list): # Checks possible win conditions in order of best to worst so it will always return best possible hand, (e.g. won't return pair when there's a full house)
    if StraightFlush(list)[0]:
        pass
    elif Quads(list)[0]:
        print("Quads")
    elif FullHouse(list)[0]:
        print("Full House")
    elif Flush(list)[0]:
        print("Flush")
    elif Straight(list)[0]:
        pass
    elif Set(list)[0]:
        print("Set")
    elif Pair(list)[0]:
        print("Pair or Twopair")
    else:
        print("HighCard")



nutsearch(cardlist)