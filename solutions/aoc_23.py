import heapq
from collections import defaultdict

dirs = {
    'v': (1,0),
    '>': (0,1),
    '<': (0, -1),
    '^': (-1, 0)
}
def one(lines):

    q = [(0, (0,1), 'v', set())]   # cost, j,i, dir, choices ; we are on a safe square

    max_cost = 0
    while q:
        #print(q)
        cost, c, d, visited = q.pop(0)

        j,i = c

        nj, ni = move(c,d)
        cost += 1

        if nj == len(lines)-1:
            max_cost = max(max_cost, cost)
            continue


        nsquare = lines[nj][ni]
        while nsquare in "<>^v":
            cost += 1
            nj, ni = move((nj,ni), nsquare)
            nsquare = lines[nj][ni]

        opts = []
        for (pd, (pdj, pdi)) in dirs.items():
            pj, pi = nj+pdj, ni+pdi

            if (pj, pi) == (j,i) or (pj, pi) in visited:
                continue

            if (lines[pj][pi] == '<' and pd == '>') or \
                    (lines[pj][pi] == '>' and pd == '<') or \
                    (lines[pj][pi] == 'v' and pd == '^') or \
                    (lines[pj][pi] == '^' and pd == 'v'):
                continue

            if lines[pj][pi] in ".<>^v":
                opts.append((pd, (nj, ni)))

        if len(opts) > 1:
            n_visited = visited.copy()
            n_visited.add((nj, ni))
        else:
            n_visited = visited

        for (pd, pc) in opts:
            q.append((cost, pc, pd, n_visited))

    return max_cost
def move(c, d):
    (x,y) = c
    (dx,dy) = dirs[d]
    return x+dx, y+dy

def two(lines):
    gr, end = build_graph(lines)

    q = [(0, (0, 1), None, frozenset())]  # cost, j,i, previous , choices ; we are on a safe square
    max_cost = 0
    while q:
        cost, c, p, visited = q.pop()

        if c == end:
            prev = max_cost
            max_cost = max(max_cost, cost)
            if prev != max_cost:
                print(max_cost)
            continue

        n_visited = visited | {c}

        for n, dcost in gr[c].items():
            if n == p:
                continue
            if n in visited:
                continue
            q.append((cost + dcost, n, c, n_visited))

    return max_cost

def build_graph(lines):
    gr = defaultdict(dict) # coord -> coord -> cost
    q = [((1,1), (0,1), (0,1), 1)]  # current node, previous node, node to link to, cost so far
    end = None
    while q:
        c, p, l, cost = q.pop()
        cj, ci = c

        if cj == len(lines)-1:
            # reached the end
            gr[c][l] = cost
            gr[l][c] = cost
            end = c
            continue

        opts = []
        for (dj, di) in dirs.values():
            nj, ni = cj+dj, ci+di
            n = (nj, ni)
            if n == p or lines[nj][ni] == '#':
                continue
            opts.append(n)

        if len(opts) > 1:
            if c in gr[l]:
                continue
            gr[l][c] = cost
            for n in opts:
                q.append((n, c, c, 1))

        elif len(opts) == 1:
            n = opts[0]
            q.append((n, c, l, cost+1))

    return gr, end