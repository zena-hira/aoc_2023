from collections import defaultdict
from functools import cache


def parse(lines):

    blocks = set()
    rounds = set()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '.':
                continue
            if c == '#':
                blocks.add((i,j))
            else:
                rounds.add((i,j))
    return blocks, rounds, len(lines), len(lines[0])

def roll_north(blocks, rounds):
    by_j = defaultdict(set)

    rounds2 = set()

    for (i,j) in blocks:
        by_j[j].add(i)

    for (i,j) in sorted(rounds):
        stuff = by_j[j]
        stuff = [x for x in sorted(stuff, reverse=True) if x <= i]
        ti = None
        if len(stuff) == 0:
            ti = 0
        else:
            ti = stuff[0]+1
        by_j[j].add(ti)
        rounds2.add((ti, j))

    return rounds2


def one(lines):
    blocks, rounds, mi, mj = parse(lines)
    rounds2 = roll_north(blocks, rounds)
    return sum(mi-i for (i,j) in rounds2)


def spin(blocks, rounds, mi, mj):

    # north
    for (i,j) in sorted(rounds):
        oi = i
        changed = False
        while i > 0 and (i-1, j) not in rounds and (i-1, j) not in blocks:
            changed = True
            i = i-1
        if changed:
            rounds.remove((oi,j))
            rounds.add((i,j))

    # west
    for (i,j) in sorted(rounds, key=lambda x: x[1]):
        oj = j
        changed = False
        while j > 0 and (i, j-1) not in rounds and (i, j-1) not in blocks:
            changed = True
            j = j-1
        if changed:
            rounds.remove((i, oj))
            rounds.add((i,j))

    # south
    for (i,j) in sorted(rounds, reverse=True):
        oi = i
        changed = False
        while i < mi-1 and (i + 1, j) not in rounds and (i + 1, j) not in blocks:
            changed = True
            i = i + 1
        if changed:
            rounds.remove((oi, j))
            rounds.add((i, j))

    # east
    for (i,j) in sorted(rounds, key=lambda x: x[1], reverse=True):
        oj = j
        changed = False
        while j < mj-1 and (i, j + 1) not in rounds and (i, j + 1) not in blocks:
            changed = True
            j = j + 1
        if changed:
            rounds.remove((i, oj))
            rounds.add((i, j))

def two(lines):
    blocks, rounds, mi, mj = parse(lines)
    blocks = frozenset(blocks)

    seen = {}

    for i in range(1000000000):

        rf = frozenset(rounds)
        if rf in seen:
            prev = seen[rf]
            loop_len = i - prev
            print(i, prev, loop_len)
            remaining = 1000000000 - i
            for j in range(remaining % loop_len):
                spin(blocks, rounds, mi, mj)
            break
        seen[rf] = i

        spin(blocks, rounds, mi, mj)

        # for i in range(mi):
        #     for j in range(mj):
        #         if (i,j) in blocks and (i,j) in rounds:
        #             print('!', end='')
        #         elif (i,j) in blocks:
        #             print('#', end='')
        #         elif (i,j) in rounds:
        #             print('O', end='')
        #         else:
        #             print('.', end='')
        #     print()
        # print()


    return sum(mi-i for (i,j) in rounds)
