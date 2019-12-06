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
    moves = []
    for x,y in wireMoves:
        if x == 0:
            fromTo = (pos[1],pos[1]+y)
            moves.append(['v',pos[0], min(fromTo), max(fromTo)])
        if y == 0:
            fromTo = (pos[0],pos[0]+x)
            moves.append(['h',pos[1], min(fromTo), max(fromTo)])
        pos[1] += y
        pos[0] += x
    return moves

def getIntersections(wireLineData1, wireLineData2):

    intersections = []

    for orientation1, fixedKoord1, lo1, hi1 in wireLineData1:
        for orientation2, fixedKoord2, lo2, hi2 in wireLineData2:
            if orientation2 ==orientation1:
                continue
            if isBetween(fixedKoord1, lo2, hi2) and isBetween(fixedKoord2, lo1, hi1):
                if orientation1 == 'v':
                    intersections.append((fixedKoord1, fixedKoord2))
                else:
                    intersections.append((fixedKoord2, fixedKoord1))
            
            

    return intersections

def doDaThang(file):

    wires = getMoveData(file)

    horVertLineData1 = getHorAndVertLineData(wires[0])
    horVertLineData2 = getHorAndVertLineData(wires[1])

    intersections = getIntersections(horVertLineData1, horVertLineData2)
    print(intersections)

    manhattanDist = lambda tupel: tupel[0] + tupel[1]

    return min(map(manhattanDist, intersections))

doDaThang('03/input-test3.txt')

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
