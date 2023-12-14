import math
import re

def parse(lines):
    instrs = lines[0]
    tree = {}
    for line in lines[2:]:
        fr, l, r = re.match(r'(...) = .(...), (...).', line).groups()
        tree[fr] = (l, r)
    return instrs, tree

def one(lines):
    instrs, tree = parse(lines)

    curr = 'AAA'
    count = 0
    while True:
        for x in instrs:
            curr = tree[curr][(x == 'R')*1]
            count += 1
            if curr == 'ZZZ':
                return count

def two(lines):
    return two2(lines)
    instrs, tree = parse(lines)

    currs = [key for key in tree.keys() if key[2] == 'A']
    count = 0
    while True:
        for x in instrs:
            currs = [ tree[curr][(x == 'R') * 1] for curr in currs ]
            count += 1
            if all(curr[2] == 'Z' for curr in currs):
                return count

def two2(lines):
    instrs, tree = parse(lines)

    currs = [key for key in tree.keys() if key[2] == 'A']
    cycles = { c: trace_path(c, tree, instrs) for c in currs }

    v = 1
    for count, trace in cycles.values():
        v = math.lcm(v, count)
    return v

def trace_path(c, tree, instrs):
    trace = []
    curr = c
    count = 0
    while True:
        for x in instrs:
            trace.append(curr)
            curr = tree[curr][(x == 'R') * 1]
            count += 1
            if curr[2] == 'Z':
                return count, trace

