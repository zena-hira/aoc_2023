import itertools
from collections import Counter

rank_map = { card: rank for card, rank in zip("TJQKA", [10,11,12,13,14]) }
def parse(lines):
    for line in lines:
        cards, bid = line.split()
        bid = int(bid)
        cards = [ int(rank_map.get(c, c)) for c in cards ]
        yield cards, bid

def classify(card):
    card_sorted = sorted(card,reverse=True)
    card_groups = itertools.groupby(card_sorted)

    cs = Counter()
    for (rank, group) in card_groups:
        cs[len(list(group))] += 1
    return (tuple(sorted(cs.items(),reverse=True)), tuple(card))


def one(lines):
    all_hands = list(parse(lines))
    sorted_hands = sorted([(classify(card), bid) for card, bid in all_hands])

    return sum((r+1) * bid for r, (stuff, bid) in enumerate(sorted_hands))


rank_map2 = { card: rank for card, rank in zip("TJQKA", [10,0,12,13,14]) }
def parse2(lines):
    for line in lines:
        cards, bid = line.split()
        bid = int(bid)
        cards = [ int(rank_map2.get(c, c)) for c in cards ]
        yield cards, bid

def classify2(card):
    card_sorted = sorted(card,reverse=True)
    card_groups = itertools.groupby(card_sorted)

    rs = Counter()
    cs = Counter()

    for (rank, group) in card_groups:
        c = len(list(group))
        rs[rank] = c
        cs[c] += 1

    js = rs[0]
    if js > 0 and js != 5:
        cs[js] -= 1
        if cs[js] == 0:
            del cs[js]
        biggest_group = max(cs.keys())
        cs[biggest_group] -= 1
        cs[biggest_group+js] += 1
        if cs[biggest_group] == 0:
            del cs[biggest_group]

    return (tuple(sorted(cs.items(),reverse=True)), tuple(card))

def two(lines):
    all_hands = list(parse2(lines))
    sorted_hands = sorted([(classify2(card), bid) for card, bid in all_hands])
    return sum((r + 1) * bid for r, (stuff, bid) in enumerate(sorted_hands))
