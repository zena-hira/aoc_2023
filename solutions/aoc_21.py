from typing import List
from collections import *


def one(lines, steps=64):
    width = len(lines[0])
    height = len(lines)
    start = find_start(lines)

    next = [start]

    for x in range(steps):
        currs = next
        next = set()
        for n in currs:
            (cj,ci) = n

            for (dj, di) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nj = dj + cj
                ni = di + ci
                if ni >= 0 and ni < width and nj >= 0 and nj < height and lines[nj][ni] in '.S':
                    next.add((nj,ni))

    return len(next)

def find_start(lines):
    width = len(lines[0])
    height = len(lines)
    for i in range(width):
        for j in range(height):
            if lines[j][i] == 'S':
                return (j, i)


def two(lines, steps=26501365):
    width = len(lines[0])
    height = len(lines)
    start = find_start(lines)

    offset = steps % width
    leftover = steps // width

    next = {start: set([(0,0)])}

    reachable_per_loop = []
    for s in range(steps):
        if s % 100 == 0:
            print('.',end='')
        currs = next
        next = defaultdict(set)
        loop_once(width, height, lines, currs, next)

        if s % width == offset:
            v = sum([len(ws) for ws in currs.values()])
            reachable_per_loop.append(v)

        if len(reachable_per_loop) >= 3:
            break

    print(reachable_per_loop)

    m = leftover
    d0 = reachable_per_loop[0]
    d1 = reachable_per_loop[1] - reachable_per_loop[0]
    d2 = reachable_per_loop[2] - reachable_per_loop[1]
    return d0 + (d1*m) + (d2 - d1) * m * (m - 1)//2

def quick_loop(delta_worlds, currs):
    for k, dw in delta_worlds.items():
        currs[k].update({ ((da+a), (db+b)) for (da, db) in dw for (a,b) in currs[k]})

def analyze(width, height, lines, ks):
    currs = { k: {(0,0)} for k in ks}
    next = defaultdict(set)
    loop_once(width, height, lines, currs, next)
    #print(currs)
    #print(next)
    #print(currs.keys() == next.keys())
    #print([(k, len(ws - {(0,0)})) for k, ws in next.items() if len(ws - {(0,0)}) > 0])
    print(len([(k, len(ws - {(0,0)})) for k, ws in next.items() if len(ws - {(0,0)}) > 0]))

    print([(k,ws) for k, ws in next.items() if (0,0) not in ws])
    return {k: (ws - {(0,0)}) for k, ws in next.items() if len(ws - {(0,0)}) > 0}


def loop_once(width, height, lines, currs, next):
    for n, worlds in currs.items():
        (cj, ci) = n

        for (dj, di) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nj = dj + cj
            ni = di + ci

            wi = 0
            wj = 0

            wnj = nj % height
            wni = ni % width

            if lines[wnj][wni] not in ".S":
                continue

            if 0 <= ni < width and 0 <= nj < height:
                next[(nj, ni)].update(set(worlds))
                continue

            if ni < 0:
                wi = -1
            elif ni >= width:
                wi = 1

            if nj < 0:
                wj = -1
            elif nj >= height:
                wj = 1

            next[(wnj, wni)].update({(wj + j, wi + i) for (j, i) in worlds})


