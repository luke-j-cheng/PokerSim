list = [1, 3, 3, 4, 4, 2]
pairlist = []
newlist = set(list)
for i in newlist:
    count = list.count(i)
    if count != 1:
        pairlist.append(count)

if max(pairlist) == 4:
    Quad = True
elif max(pairlist) == 3:
    if 2 in pairlist: 
        fullhouse = True:
    else:
        set = True
elif
    max(pairlist) == 2:
    if len(pairlist) >= 2:
        twopair = True
    else: 
        pair = True
else:
    False