import re

transitions = {
    'R': ( 0,  1),
    'L': ( 0, -1),
    'D': ( 1,  0),
    'U': (-1,  0)
}

def walk(lines):
    mp = {}
    ci, cj = 0,0
    for line in lines:
        dir, dist, code = re.fullmatch(r'(.) (\d+) .#(.*).', line).groups()
        dist = int(dist)
        di, dj = transitions[dir]

        for i in range(dist):
            mp[(ci,cj)] = code
            ci += di
            cj += dj

    return mp
def one(lines):
    mp = walk(lines)

    lo_i = min(i for i,j in mp.keys())
    lo_j = min(j for i,j in mp.keys())
    hi_i = max(i for i,j in mp.keys())
    hi_j = max(j for i,j in mp.keys())

    q = [(lo_i-1, lo_j-1)]
    visited = set()
    while q:
        ci, cj = q.pop()
        visited.add((ci,cj))
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni = ci+di
            nj = cj+dj
            if ni < lo_i-1 or ni > hi_i+1 or nj < lo_j - 1 or nj > hi_j+1 or (ni,nj) in mp or (ni,nj) in visited:
                continue
            q.append((ni,nj))

    exp_volume = ((hi_i+2) - (lo_i-1)) * ((hi_j+2) - (lo_j-1))
    return exp_volume - len(visited)

def walk2(lines):

    edges = []
    ci, cj = 0,0
    min_i = 0
    min_j = 0
    max_i = 0
    max_j = 0

    area = 0

    for line in lines:
        dist, dir = re.fullmatch(r'. \d+ .#(.....)(.).', line).groups()
        dist = int(dist, 16)
        di, dj = transitions2[dir]
        ni = ci + (di*dist)
        nj = cj + (dj*dist)

        area += (ci * (dist * dj))

        min_i = min(min_i, ni)
        max_i = max(max_i, ni)
        min_j = min(min_j, nj)
        max_j = max(max_j, nj)
        edges += [((ci, cj), (ni, nj))]
        ci = ni
        cj = nj

    return area, edges, min_i, max_i, min_j, max_j

transitions2 = {
    '0': ( 0,  1),
    '2': ( 0, -1),
    '1': ( 1,  0),
    '3': (-1,  0)
}

def two(lines):
    volume, edges, min_i, max_i, min_j, max_j = walk2(lines)
    perimiter = sum((abs(i2-i1) + abs(j2-j1) for (i1, j1), (i2, j2) in edges))
    area = abs(volume)+ 1+perimiter/2
    return area