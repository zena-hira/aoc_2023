from collections import defaultdict
from itertools import combinations


def parse(lines):
    coords = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                coords.add((i,j))
    return coords, (len(lines), len(lines[0]))

def one(lines):
    coords, (mi, mj) = parse(lines)
    coords_expanded = expand(coords, mi, mj)

    sum = 0
    for ((a,b), (c,d)) in combinations(coords_expanded, 2):
        sum += abs(a-c) + abs(b-d)
    return sum
def expand(coords, mi, mj, inc=1):
    coords_by_i = defaultdict(set)
    coords_out = set()

    for i,j in coords:
        coords_by_i[i].add(j)

    coords_by_j = defaultdict(set)
    increase = 0
    for i in range(mi):
        if i not in coords_by_i:
            increase += inc
        else:
            for j in coords_by_i[i]:
                coords_by_j[j].add(i+increase)

    increase = 0
    for j in range(mj):
        if j not in coords_by_j:
            increase += inc
        else:
            for i in coords_by_j[j]:
                coords_out.add((i, j+increase))
    return coords_out
def two(lines):
    coords, (mi, mj) = parse(lines)
    coords_expanded = expand(coords, mi, mj, inc=(1000000-1))

    sum = 0
    for ((a, b), (c, d)) in combinations(coords_expanded, 2):
        sum += abs(a - c) + abs(b - d)
    return sum

