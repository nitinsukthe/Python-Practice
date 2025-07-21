def findPairs(pairs):
    s=set()
    for (x,y) in pairs:
        s.add((x,y))
        if (y,x) in s:
            print((x,y))
pairs=[(1,2),(3,4),(7,12),(12,7)]
findPairs(pairs)
