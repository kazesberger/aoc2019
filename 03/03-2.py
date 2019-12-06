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
            moves.append(['D' if pos[1] < pos[1]+y else 'U', pos[0], min(fromTo), max(fromTo)])
        if y == 0:
            fromTo = (pos[0],pos[0]+x)
            moves.append(['R' if pos[1] < pos[1]+x else 'L', pos[1], min(fromTo), max(fromTo)])
        pos[1] += y
        pos[0] += x
    return moves

def getIntersections(wireLineData1, wireLineData2):

    intersections = []
    dist1 = 0
    dist2 = 0

    for orientation1, fixedKoord1, lo1, hi1 in wireLineData1:
        for orientation2, fixedKoord2, lo2, hi2 in wireLineData2:
            if orientation2 in ['R', 'L'] and orientation1 in ['R', 'L'] or orientation2 in ['D', 'U'] and orientation1 in ['D', 'U']:
                dist2 += (hi2-lo2)
                continue
            if isBetween(fixedKoord1, lo2, hi2) and isBetween(fixedKoord2, lo1, hi1):
                if orientation2 in ['U', 'L']:
                    intersections.append((fixedKoord1, fixedKoord2, hi2 - fixedKoord1 + dist1 + dist2 + fixedKoord2 - lo1))
                else:
                    intersections.append((fixedKoord2, fixedKoord1, fixedKoord1 - lo2 + dist1 + dist2 + fixedKoord1 - lo2))
        dist2 = 0
        dist1 += (hi1-lo1)

    return intersections

# for foo, a, b, c in [['R', 0, 0, 98], ['D', 98, 0, 47]]:
#     print(f'{foo,a,b,c}')

def doDaThang(file):

    wires = getMoveData(file)

    horVertLineData1 = getHorAndVertLineData(wires[0])
    horVertLineData2 = getHorAndVertLineData(wires[1])

    intersections = getIntersections(horVertLineData1, horVertLineData2)
    print(intersections)

    # manhattanDist = lambda tupel: tupel[0] + tupel[1]

    # return min(map(manhattanDist, intersections))

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
