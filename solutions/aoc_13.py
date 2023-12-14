import itertools


def one(lines):
    patterns = [list(g) for k, g in itertools.groupby(lines, key=lambda x: x == '') if not k]
    scores = [score(pattern) for pattern in patterns]
    print(scores)
    return sum(scores)

def score(pattern):

    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i+1]:
            if all(a == b for a,b in zip(reversed(pattern[0:i+1]), pattern[i+1:])):
                return 100 * (i+1)

    p_transpose = list(zip(*pattern))

    for i in range(len(p_transpose) - 1):
        if p_transpose[i] == p_transpose[i+1]:
            if all(a == b for a,b in zip(reversed(p_transpose[0:i+1]), p_transpose[i+1:])):
                return i+1

def two(lines):
    patterns = [list(g) for k, g in itertools.groupby(lines, key=lambda x: x == '') if not k]
    scores = [score_2(pattern) for pattern in patterns]
    print(scores)
    return sum(scores)

def score_2(pattern):
    original_score = score(pattern)

    for p2 in all_smudges(pattern):

        for i in range(len(p2) - 1):
            if p2[i] == p2[i + 1]:
                if all(a == b for a, b in zip(reversed(p2[0:i + 1]), p2[i + 1:])):
                    s = 100 * (i + 1)
                    if s != original_score:
                        return s

        p2 = list(zip(*p2))

        for i in range(len(p2) - 1):
            if p2[i] == p2[i + 1]:
                if all(a == b for a, b in zip(reversed(p2[0:i + 1]), p2[i + 1:])):
                    s = i + 1
                    if s != original_score:
                        return s


def all_smudges(pattern):
    p2 = [list(line) for line in pattern]
    for i in range(len(p2)):
        for j in range(len(p2[0])):
            orig = p2[i][j]
            if orig == '#':
                p2[i][j] = '.'
            else:
                p2[i][j] = '#'
            yield p2
            p2[i][j] = orig