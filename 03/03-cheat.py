def get_data():
    with open("03/input.txt", "r") as f:
        data = f.read().rstrip()

    data = [[(x[0], int(x[1:])) for x in line.split(",")]
            for line in data.splitlines()]

    return data


def points(dirs):
    points = []
    x, y = 0, 0
    for d, c in dirs:
        if d == "U":
            points.extend((x, y + i) for i in range(1, c + 1))
            y += c
        if d == "D":
            points.extend((x, y - i) for i in range(1, c + 1))
            y -= c
        if d == "L":
            points.extend((x - i, y) for i in range(1, c + 1))
            x -= c
        if d == "R":
            points.extend((x + i, y) for i in range(1, c + 1))
            x += c
    return points


def points2(dirs):
    delay = {}
    points = []
    steps = 0
    x, y = 0, 0
    for d, c in dirs:
        if d == "U":
            points.extend((x, y + i, steps + i) for i in range(1, c + 1))
            y += c
        if d == "D":
            points.extend((x, y - i, steps + i) for i in range(1, c + 1))
            y -= c
        if d == "L":
            points.extend((x - i, y, steps + i) for i in range(1, c + 1))
            x -= c
        if d == "R":
            points.extend((x + i, y, steps + i) for i in range(1, c + 1))
            x += c
        steps += c
    return points


def part1(data):
    a, b = data
    pa = points(a)
    pb = points(b)

    union = set(pa).intersection(pb)

    result = min(union, key=(lambda pos: abs(pos[0]) + abs(pos[1])))

    return sum(abs(x) for x in result)


def part2(data):
    a, b = data
    pa = points2(a)
    pb = points2(b)

    union = set(x[:2] for x in pa).intersection(x[:2] for x in pb)

    pad = dict((x[:2], x[2]) for x in pa)
    pbd = dict((x[:2], x[2]) for x in pb)

    # union2 = set(x for x in pa)

    result = min(union, key=(lambda pos: pad[pos] + pbd[pos]))

    return pad[result] + pbd[result]

part1(get_data())