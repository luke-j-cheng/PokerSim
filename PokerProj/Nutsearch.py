## POKER HAND WIN PICKER ##

from cards import *

#Card Types

def StraightFlush(list):
    if True:
        return (True, score)
    else:
        return False

def Quads(inlist):
    hand = []
    for i in inlist:
        hand.append(i.value)
    quadlist = []
    score = []
    newlist = set(hand)
    for value in newlist:
        num = hand.count(value)
        if num == 4:
            quadlist.append(value)
    if len(quadlist) == 1:
        newlist.remove(quadlist[0])
        quadlist.append(max(newlist))
        return (True, quadlist)
    else:
        return (False, None)

def FullHouse(inlist):
    hand = []
    for i in inlist: 
        hand.append(i.value)
    threelist = []
    pairlist = []
    score = []
    newlist = set(hand)
    for value in newlist:
        num = hand.count(value)
        if num == 3:
            threelist.append(value)
            pairlist.append(value)
        elif num == 2: 
            pairlist.append(value)
    if len(threelist) > 0 and len(pairlist) > 0:
        score.append(max(threelist))
        if max(threelist) in pairlist:
            pairlist.remove(max(threelist))
        score.append(max(pairlist))
        return(True, score)
    else:
        return(False, None)

    

def Flush(inlist):
    hand = []
    score = []
    value = []
    for i in inlist:
        hand.append(i.suit)
    for suit in suitlist:
        num = hand.count(suit)
        if num >= 5:
            score.append(num)
            flushsuit = suit
    if len(score) >= 1:
        for card in inlist:
            if card.suit == flushsuit:
                value.append(card.value)
        value.sort(reverse=True)
        newval = value[:5]
        return(True, newval)
    else:
        return(False, None)
                       
                         
            
        
            
   


def Straight(list):
    if True:
        return (True, score)
    else:
        return (False, None)

def Set(list):
    if True:
        return (True, score)
    else:
        return (False, None)



def Pair(list):
    paircheck = []
    paircount = 0
    highest = []
    for i in list:
        if i not in paircheck:
            paircheck.append(i)
        else:
            paircount += 1
            highest.append(i)
    if paircount > 2:
        paircount = 2

    
    
    
    if paircount != 0:
        return (True, paircount, highest)
    else:
        return (False, None)

def HighCard(list): #Will be used to break ties by entering modified hands 
    highcard = []
    for card in list:
        highcard.append(card)
    highest = highcard.sort(reverse=True)
    return (highest)
    

#Nutsearch returns a list - first value is the score of the hand, second is the value of the score (i.e. for a pair of Nines, value is [2, 9])
def nutsearch(list):
    if StraightFlush(list)[0]:
        pass
    elif Quads(list)[0]:
        pass
    elif FullHouse(list)[0]:
        pass
    elif Flush(list)[0]:
        pass
    elif Straight(list)[0]:
        pass
    elif Set(list)[0]:
        pass
    elif Pair(list)[0]:
        pass
    else:
        return (0, HighCard(list))



print(FullHouse(spadelist))