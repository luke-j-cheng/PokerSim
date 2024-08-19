## POKER HAND WIN PICKER ##

from cards import *

#Card Types

def StraightFlush(list):
    if True:
        return (True, score)
    else:
        return False

def Quads(list):
    if True:
        return (True, score)
    else:
        return (False, None)

def FullHouse(list):
    if True:
        return (True, score)
    else:
        return (False, None)

def Flush(list):
    if True:
        return (True, score)
    else:
        return (False, None)

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
        highcard.append(card.value)
    highest = highcard.sort(reverse=True)
    return (True, highest)
    

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
        return (0, HighCard(list)[1])




