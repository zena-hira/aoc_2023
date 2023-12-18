import heapq
from collections import defaultdict

nexts = {
    '>': "^v",
    '<': "^v",
    'v': "<>",
    '^': "<>"
}

transitions = {
    '>': ( 0,  1),
    '<': ( 0, -1),
    'v': ( 1,  0),
    '^': (-1,  0)
}


def one(lines):
    mi = len(lines)
    mj = len(lines)

    q = []
    heapq.heappush(q, (0, mi+mj, 0, 0, '>', 2))
    heapq.heappush(q, (0, mi+mj, 0, 0, 'v', 2))

    visited = defaultdict(lambda: 100_000_000_000)

    while q:
        c_state = heapq.heappop(q)

        c_loss, _, ci, cj, cd, cr = c_state

        if visited[(ci,cj,cd,cr)] <= c_loss:
            continue
        visited[(ci, cj, cd, cr)] = c_loss

        if ci == mi - 1 and cj == mj - 1:
            return c_loss

        nds = [(nd, 2) for nd in nexts[cd]]
        if cr > 0:
            nds += [(cd, cr-1)]

        for nd,nr in nds:
            di, dj = transitions[nd]
            ni = ci + di
            nj = cj + dj
            if ni >= 0 and ni < mi and nj >=0 and nj < mj:
                n_loss = c_loss + int(lines[ni][nj])
                ns = (n_loss, (mi+mj)-(ni+nj), ni, nj, nd, nr)
                if visited[(ni, nj, nd, nr)] <= n_loss:
                    continue
                heapq.heappush(q, ns)


def two(lines):
    mi = len(lines)
    mj = len(lines)

    q = []
    heapq.heappush(q, (0, mi + mj, 0, 0, '>', 3, 9))
    heapq.heappush(q, (0, mi + mj, 0, 0, 'v', 3, 9))

    visited = defaultdict(lambda: 100_000_000_000_000)

    while q:
        c_state = heapq.heappop(q)

        c_loss, _, ci, cj, cd, min_r, max_r = c_state

        if visited[(ci, cj, cd, min_r, max_r)] <= c_loss:
            continue
        visited[(ci, cj, cd, min_r, max_r)] = c_loss

        if ci == mi - 1 and cj == mj - 1:
            return c_loss

        nds = []
        if min_r > 0:
            nds += [(cd, min_r - 1, max_r - 1)]
        else:
            nds += [(nd, 3, 9) for nd in nexts[cd]]
            if max_r > 0:
                nds += [(cd, 0, max_r - 1)]

        for nd, n_min_r, n_max_r in nds:
            di, dj = transitions[nd]
            ni = ci + di
            nj = cj + dj
            if ni >= 0 and ni < mi and nj >= 0 and nj < mj:
                n_loss = c_loss + int(lines[ni][nj])
                ns = (n_loss, (mi + mj) - (ni + nj), ni, nj, nd, n_min_r, n_max_r)
                if visited[(ni, nj, nd, n_min_r, n_max_r)] <= n_loss:
                    continue
                heapq.heappush(q, ns)
