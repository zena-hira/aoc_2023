import re
from collections import Counter


def parse(lines):
    cards = []
    for line in lines:
        id, win_nums, my_nums = re.match(r'Card\s+(\d+): (.*) \| (.*)', line).groups()
        win_nums = list(map(int, win_nums.split()))
        my_nums = list(map(int, my_nums.split()))
        cards.append((id, win_nums, my_nums))
    return cards

def one(lines):
    cards = parse(lines)
    s = 0
    for id, win_nums, my_nums in cards:
        ms = len(set(win_nums) & set(my_nums))
        if ms > 0:
            s += 2**(ms-1)
    return s


def two(lines):

    cards = parse(lines)
    cards_by_id = { int(id) : len(set(win_nums) & set(my_nums))  for id, win_nums, my_nums in cards }
    c = Counter(cards_by_id.keys())

    for n in sorted(c.keys()):
        x = c[n]
        for i in range(n+1, n+cards_by_id[n]+1):
            c[i] += x
    return c.total()