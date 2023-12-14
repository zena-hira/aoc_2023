import math


def parse(lines):
    return [ (int(time), int(distance)) for (time,distance) in list(zip(lines[0].split(), lines[1].split()))[1:]]

def one(lines):
    return math.prod((count_options(time, distance) for time, distance in parse(lines)))

def count_options(time, distance):
    s = 0
    for i in range(time):
        if (time - i) * i > distance:
            s += 1
    return s


def two(lines):
    return count_options(49877895, 356137815021882)


