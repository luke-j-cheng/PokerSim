from cards import *
from Nutsearch import *
import random


def main():
    p1 = []
    c1 = random.choice(clublist)
    clublist.remove(c1)
    c2 = random.choice(clublist)
    clublist.remove(c2)
    p1.append(c1)
    p1.append(c2)
    
    

    for i in (p1):
        print(i)
    for j in clublist:
        print(j)

main()