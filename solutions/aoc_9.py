
def parse(line):
    return list(map(int, line.split()))

def one(lines):
    readings = list(map(parse, lines))
    return sum([extend(reading) for reading in readings])

def extend(readings):
    lasts = []
    while any((r != 0) for r in readings):
        lasts.append(readings[-1])
        readings = [b - a for a, b in zip(readings, readings[1:])]

    c = 0
    for i in reversed(lasts):
        c = i+c
    return c

def two(lines):
    readings = list(map(parse, lines))
    return sum([extend(list(reversed(reading))) for reading in readings])

