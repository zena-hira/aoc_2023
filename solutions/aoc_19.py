import itertools
import math
import re
from typing import List


def parse(lines: List[str]):
    rules, inputs = [list(g) for k, g in itertools.groupby(lines, key=lambda x: x == '') if not k]

    rules_mp = {}
    for rule in rules:
        name, conds, default = re.fullmatch(r'([^{]+){(.*),([^}]+)}', rule).groups()
        cs = []
        for cond in conds.split(','):
            var, sign, val, dest = re.fullmatch(r'(.*)([<>])(.*):(.*)', cond).groups()
            cs.append((var, sign, int(val), dest))
        rules_mp[name] = (cs, default)

    inputs_lst = []
    for input in inputs:
        i = {}
        for pair in input[1:-1].split(','):
            var, val = pair.split('=')
            i[var] = int(val)
        inputs_lst.append(i)

    return rules_mp, inputs_lst

def one(lines):
    rules, inputs = parse(lines)
    return sum(sum(input.values()) for input in inputs if is_accepted(input, rules))

def is_accepted(input, rules):
    curr = 'in'
    while curr not in "AR":
        conds, default = rules[curr]
        for var, sign, limit, dest in conds:
            if interp(sign, input[var], limit):
                curr = dest
                break
        else:
            curr = default
    return curr == 'A'

def interp(sign, input, limit):
    if sign == '<':
        return input < limit
    return input > limit

def two(lines):
    rules, _ = parse(lines)

    count = 0
    q = [('in', {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})]

    while q:
        curr, obj = q.pop()
        if curr == 'A':
            count += calc_score(obj)
            continue
        if curr == 'R':
            continue
        conds, default = rules[curr]

        for var, sign, limit, dest in conds:
            o1, o2 = split_obj(var, sign, limit, obj)
            if o1 is not None:
                q.append((dest, o1))
            if o2 is None:
                break
            obj = o2
        else:
            q.append((default, obj))

    return count

def split_obj(var, sign, limit, obj):
    lo, hi = obj[var]
    if sign == '<':
        if hi < limit:
            return obj, None
        elif lo >= limit:
            return None, obj
        else:
            o_lo = obj.copy()
            o_hi = obj.copy()
            o_lo[var] = (lo, limit-1)
            o_hi[var] = (limit, hi)
            return o_lo, o_hi

    # sign == '>'
    if hi <= limit:
        return None, obj
    elif lo > limit:
        return obj, None
    else:
        o_lo = obj.copy()
        o_hi = obj.copy()
        o_lo[var] = (lo, limit)
        o_hi[var] = (limit+1, hi)
        return o_hi, o_lo




def calc_score(obj):
    return math.prod([ (hi+1)-lo for (lo, hi) in obj.values()])