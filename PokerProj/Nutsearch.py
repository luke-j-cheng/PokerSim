## POKER HAND WIN PICKER ##

from cards import *
from hands import *

'''
These first few funcitons serve to check if each player meets the criteria for the following hands
Input: List of length 7 consisting of objects from the card class (5 shared cards, 2 unique cards per player)
Process: Varies from function to function
Output: Returns True if the player's cards meet the criteria, as well as the necessary score/values of the hand 
'''

def StraightFlush(inlist): 
    hand = []
    value = []
    score = []
    flush = 0
    for i in inlist:
        hand.append(i.suit) ## Adds every card's suit to list
    for suit in suitlist:
        num = hand.count(suit)
        if num >= 5:
            flush = 1
            flushsuit = suit ## Checks if at least 5 cards are the same suit, sets flushsuit to the suit
            break
    
    if flush == 1:
        for card in inlist: 
            if card.suit == flushsuit:
                value.append(card.value)
        value.sort(reverse=True)

        if (14) in value: ## For Ace's unique straight property (can be used as 12345 or 10JQKA)
            value.append(1)
        newlist = set(value)
        for i in newlist:
            num = i
            count = 0
            for i in range (5):
                if (num - 1) in newlist:
                    count += 1
                    num -= 1
                else:
                    continue 
            if count == 5:
                score.append(num)
        
        if len(score) >= 1:
            print("SF WIN" + str(max(score)))
            return(True, SFWin(max(score)))
        else:
            return(False, None)


    else:   
        return(False, None)

def Quads(inlist): 
    hand = []  ## Hand stores the cards numeric values
    for i in inlist:
        hand.append(i.value)
    quadlist = []
    newlist = set(hand) ## Creates a set of the hand
    for value in newlist: 
        num = hand.count(value)
        if num == 4: ## Adds number to quadlist if four of a kind
            quadlist.append(value)
    if len(quadlist) == 1: ## If there is a four of a kind, search through hand to find highest kicker (tie purposes)
        newlist.remove(quadlist[0]) 
        quadlist.append(max(newlist))
        return (True, QuadWin(quadlist)) # Returns True and values
    else:
        return (False, None)

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
            return(True, FHWin(score)) # Returns True and necessary values
        
        else:
           return(False, None) 
    else:
        return(False, None)
  
def Flush(inlist): 
    hand = []
    value = []
    flush = 0
    
    for i in inlist:
        hand.append(i.suit) ## Adds every card's suit to list
    for suit in suitlist:
        num = hand.count(suit)
        if num >= 5:
            flush = 1
            flushsuit = suit ## Checks if at least 5 cards are the same suit, sets flushsuit to the suit
            break
    if flush == 1: # Gets every card in flushsuit and finds the 5 highest
        for card in inlist: 
            if card.suit == flushsuit:
                value.append(card.value)
        value.sort(reverse=True)
        newval = value[:5] 
        return(True, FlushWin(newval)) #Returns 5 highest cards in flushsuit
    
    else:
        return(False, None)         

def Straight(inlist):
    hand = []
    score = []
    for i in inlist:
        hand.append(i.value)
    if (14) in hand: ## For Ace's unique straight property (can be used as 12345 or 10JQKA)
        hand.append(1)
    newlist = set(hand)
    for i in newlist:
        num = i
        count = 0
        for i in range (5):
            if (num - 1) in newlist:
                count += 1
                num -= 1
            else:
                continue 
        if count == 5:
            score.append(num)
    
    if len(score) >= 1:
        print(max(score))
        return(True, StraightWin(max(score)))
    else:
        return(False, None)

def Set(inlist):
    hand = []
    for i in inlist: 
        hand.append(i.value)
    score = []
    newlist = set(hand)
    for value in newlist:
        num = hand.count(value)
        if num == 3: #Finds if a value appears three times and adds it to list
            score.append(value)
            hand.remove(value)
    if len(score) == 1:
        hand.sort(reverse=True)
        score.append(hand[:2]) # Adds 2 highest cards
        return(True, SetWin(score))
    else:
        return(False, None)

def Pair(inlist):
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



'''
Input: Input is the same as above functions (list of length 7 of objects from card class)
Process: Uses all the above functions to check if a hand is true -- in order form best to worst hand so function finds best possible hand
Output: If a hand's criteria is met, the function returns a class of said hand with the necessary parameters (representing highcards/values)
'''

def nutsearch(list): 
    if StraightFlush(list)[0]:
        return StraightFlush(list)[1]
    elif Quads(list)[0]:
        return Quads(list)[1]
    elif FullHouse(list)[0]:
        return FullHouse(list)[1]
    elif Flush(list)[0]:
        return Flush(list)[1]
    elif Straight(list)[0]:
        return Straight(list)[1]
    elif Set(list)[0]:
        return Set(list)[1]
    elif Pair(list)[0]:
        return Pair(list)[1]
    else:
        highcard = []
        for card in list:
            highcard.append(card.value)  
        highcard.sort(reverse=True)
        newhigh = highcard[:5]
        return (HighWin(newhigh))


'''
Input: Takes in a list of objects that are from the hand class, the number of highcards you need to search through, and the hand you wnat to tiebreak 
(e.g. Hands List, 2 cards, 7 (Full House Score))

Process:
1. Checks if the card in the hand is the same as the score you want to tiebreak, adds to tielist if so (if not adds None - helps determine which player wins)
2. Takes the first two hands in the tielist - goes through each and finds which is better until only one hand is left
3. Finds every player number that has that hand 

Output: Winning Player Numbers (list)
'''
def TieBreak(inlist, number, score):
    handlist = []
    tielist = []
    for i in inlist:
        if i.score == score:
            handlist.append(i.high)
            tielist.append(i.high)
        else:
            handlist.append(None)
    
    while len(tielist) > 1:
        hand1 = tielist[0]            
        hand2 = tielist[1]
        
        count = 0
        for i in range (number):
            if hand1[i] > hand2[i]:
                tielist.remove(hand2)
                break
            elif hand2[i] > hand1[i]:
                tielist.remove(hand1)
                break
            else:
                count += 1

            if count == (number):
                tielist.remove(hand1)

                
    allwinners = []
    
    for i, x in enumerate(handlist):
            if x == tielist[0]:
                allwinners.append(i + 1)
    
    return(allwinners)                   
    
'''
Input: List of objects of the hand parent class (provided by nutsearch func)

Process: 
1. Finds the score for each hand
2. Finds the best score out of all the hands and which player has it
3. If multiple players have the best score, tiebreak is used to find out which hand is better


Output:
If TieBreak used, WinSearch returns the winner(s), the hand name (i.e. Three of a Kind), and True (lets us know that tiebreaker was used)
If TieBreak ISNT used, the function returns the winner, what hand they had, and false (lets us know tiebreaker was NOT used)
'''

def WinSearch(inlist):
    handscore = []
    for i in inlist:
        handscore.append(i.score)
    nuts = max(handscore) ## Finds highest scoring hand
    winnum = handscore.index(nuts) ## Finds who has the highest scoring hand (first player to have it in list)
    
    if handscore.count(nuts) > 1:
        winner = TieBreak(inlist, inlist[winnum].highnum, nuts) ## Runs through tiebreak if many people have same scoring hand
        hand = inlist[winnum].name
        return(winner, hand, True) # Returns winner(s)
    else:   
        hand = inlist[winnum].name
        return (winnum + 1, hand, False) # Returns Winner if they are the only winner






