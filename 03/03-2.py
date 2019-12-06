isBetween = lambda a, lo, hi : lo <= a <= hi

def getMoveVector(move):
    if move[0] == 'U':
        return [0, int(move[1:])]
    if move[0] == 'D':
        return [0, -1 * int(move[1:])]
    if move[0] == 'L':
        return [-1 * int(move[1:]), 0]
    if move[0] == 'R':
        return [int(move[1:]), 0]

def getMoveData(file):
    with open(file, 'r') as f:
        read_data = f.read().split("\n")

    return [[getMoveVector(move) for move in line.split(',')] for line in read_data]

def getHorAndVertLineData(wireMoves):

    pos = [0,0]
    hMoves = []
    vMoves = []
    for x,y in wireMoves:
        if x == 0:
            fromTo = (pos[1],pos[1]+y)
            vMoves.append([pos[0], min(fromTo), max(fromTo)])
        if y == 0:
            fromTo = (pos[0],pos[0]+x)
            hMoves.append([pos[1], min(fromTo), max(fromTo)])
        pos[1] += y
        pos[0] += x
    return (hMoves, vMoves)

def getIntersections(hLines, vLines):

    intersections = []
    for y, lox, hix in hLines:
        for x, loy, hiy in vLines:
            if isBetween(y, loy, hiy) and isBetween(x, lox, hix):
                intersections.append((x,y))
    return intersections

def getIntersectionsWithP2Dist(hLines, vLines):

    intersections = []
    for y, lox, hix in hLines:
        for x, loy, hiy in vLines:
            if isBetween(y, loy, hiy) and isBetween(x, lox, hix):
                intersections.append((x,y))
    return intersections

def doDaThang(file):

    wires = getMoveData(file)

    w1EdgeData = getHorAndVertLineData(wires[0])
    w2EdgeData = getHorAndVertLineData(wires[1])

    # horLinesW1 = w1EdgeData[0]
    # verLinesW2 = w2EdgeData[1]

    # horLinesW2 = w2EdgeData[0]
    # verLinesW1 = w1EdgeData[1]

    intersections = getIntersections(w1EdgeData[0], w2EdgeData[1])
    intersections.extend(getIntersections(w2EdgeData[0], w1EdgeData[1]))
    print(intersections)

    manhattanDist = lambda tupel: tupel[0] + tupel[1]

    return min(map(manhattanDist, intersections))

doDaThang('03/input.txt')

# (x,y) -> (x+dx, y+dy)

# map
# f(x) -> y

# [(-998,0), (-998,662)]

# [(-1500,500), ()]

# [(A,B),(C,D)] if C!=0: -> horizontal move on B
# [(a,b),(c,d)] => c=0, 0 between(a,a+c),    -> vertical move on a -> crossing if  B between(b,b+d) and a between(A,A+C)
# -> crossing at (a,B)

# horMoves1[(B,r(A,A+C)), (), ()]
# verMoves2[(a,r(b,b+d)), (), ()]

# horMoves2[(b,r(a,a+c)), (), ()]
# verMoves1[(A,r(B,B+D)), (), ()]

# # or
# horMoves1[(a,r(a,a+b)), (), ()]
# verMoves2[(a,r(a,a+b)), (), ()]
# # or better:
# horMoves1[(a,lo,hi), (a,lo,hi), ()]
# verMoves2[(a,lo,hi), (a,lo,hi), ()]
# #   # crossings where hm1[i][0] in range(hm2[j][1],hm2[j][1]+hm2[j][2])


# print(list(range(5,-2)))
