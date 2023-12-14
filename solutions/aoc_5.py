import itertools
from collections import defaultdict
import re

def parse(lines):
    init_seeds = list(map(int, lines[0].split(': ')[1].split()))
    conversion_chain = {}
    conversion_map = defaultdict(list)

    current = None
    for line in lines[1:]:
        if line == '':
            continue

        if m := re.match(r'([a-z]+)-to-([a-z]+) map:', line):
            fr, to = m.groups()
            conversion_chain[fr] = to
            current = fr
            continue

        dest, src, l = list(map(int, line.split()))
        conversion_map[current].append((dest, src, l))

    return (init_seeds, conversion_chain, conversion_map)

def one(lines):
    (init_seeds, conversion_chain, conversion_map) = parse(lines)
    conversion_map_sorted = { k: sorted(
        [(src, dest, l) for (dest, src, l) in v]
    ) for k,v in conversion_map.items() }

    return min(chase_to_end(seed, conversion_chain, conversion_map_sorted) for seed in init_seeds)


def chase_to_end(seed, conversion_chain, conversion_map_sorted):
    n = seed
    current = "seed"

    while current != "location":
        n = one_step(n, conversion_map_sorted[current])
        current = conversion_chain[current]
    return n


def one_step(n, mps):
    for (src, dest, l) in mps:
        if src <= n < src+l:
            return n-src+dest
    return n


def two(lines):
    (init_seeds, conversion_chain, conversion_map) = parse(lines)
    conversion_map_sorted = { k: sorted(
        [(src, dest, l) for (dest, src, l) in v]
    ) for k,v in conversion_map.items() }

    seeds = [ tuple(init_seeds[i:i+2]) for i in range(0, len(init_seeds), 2) ]

    return min(chase_to_end2(seeds, conversion_chain, conversion_map_sorted))[0]


def chase_to_end2(seeds, conversion_chain, conversion_map_sorted):
    current = "seed"

    q = set(seeds)
    while current != "location":
        n_q = set()
        for seed in q:
            n_q.update(one_step2(seed, conversion_map_sorted[current]))
        current = conversion_chain[current]
        q = n_q
    return q

def one_step2(seed, mps):
    sn, sl = seed
    out = set()

    for (src, dest, l) in mps:
        if sn + sl < src:
            out.add((sn, sl))
            sl = 0
            break
        if sn < src:
            out.add( (sn, src-sn) )
            sn = src
            sl = sl - (src-sn)
        if src <= sn < src + l:
            l_used = min(sl, src+l - sn)
            out.add((sn - src + dest, l_used))
            if sl == l_used:
                sl = 0
                break
            sn = sn + l_used
            sl = sl - l_used

    if sl > 0:
        out.add((sn, sl))
    return out