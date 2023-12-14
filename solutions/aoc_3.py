import math
import re
from collections import defaultdict


def parse(lines):
    numbers = []
    symbol_coords = {}

    for i, line in enumerate(lines):
        for m in re.finditer(r'(\d+)', line):
            numbers.append( (int(m.group(0)), i, *m.span(0)) )
        for m in re.finditer(r'([^.0-9])', line):
            symbol_coords[(i, m.start(0))] = m.group(0)
    return numbers, symbol_coords

def has_adjacent_symbol(x, y, symbol_coords):
    for i in [-1,0,1]:
        for j in [-1, 0, 1]:
            if (x+i, y+j) in symbol_coords:
                return (x+i, y+j)
    return False

def one(lines):
    numbers, symbol_coords = parse(lines)
    s = 0
    for n, row, start, end in numbers:
        if any(has_adjacent_symbol(row, i, symbol_coords) for i in range(start,end)):
            s += n
    return s


def all_ajacent_symbols(x, y, symbol_coords):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (x + i, y + j) in symbol_coords:
                    yield (x + i, y + j)

def two(lines):
    numbers, symbol_coords = parse(lines)

    symbol_neighbours = defaultdict(list)

    for n, row, start, end in numbers:
        sn_coords = set()
        for i in range(start, end):
            for c in all_ajacent_symbols(row, i, symbol_coords):
                sn_coords.add(c)
        for c in sn_coords:
            symbol_neighbours[c].append(n)

    return sum((math.prod(v) for v in symbol_neighbours.values() if len(v) == 2))
