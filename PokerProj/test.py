inlist = [1, 3, 3, 3, 3, 4, 4, 2]
quadlist = []
score = []
newlist = set(inlist)
for i in newlist:
    num = inlist.count(i)
    if num == 4:
        quadlist.append(i)
if len(quadlist) == 1:
    newlist.remove(quadlist[0])
    quadlist.append(max(newlist))


print(quadlist)