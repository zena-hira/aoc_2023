from collections import defaultdict

transitions = {
    '>': ( 0,  1),
    '<': ( 0, -1),
    'v': ( 1,  0),
    '^': (-1,  0)
}

rotates = {
    '>': {'/': (-1,  0, '^'), '\\': ( 1,  0, 'v') },
    '<': {'/': ( 1,  0, 'v'), '\\': (-1,  0, '^') },
    '^': {'/': ( 0,  1, '>'), '\\': ( 0, -1, '<' )},
    'v': {'/': ( 0, -1, '<'), '\\': ( 0,  1, '>' )}
}

def solve(lines, si, sj, sd):
    mi = len(lines)
    mj = len(lines[0])

    beam_locations = defaultdict(set)

    active_beams = [(si, sj, sd)]

    while active_beams:
        ci, cj, cd = active_beams.pop()
        if ci < 0 or ci >= mi or cj < 0 or cj >= mj:
            continue

        if cd in beam_locations[(ci, cj)]:
            continue
        beam_locations[(ci, cj)].add(cd)

        cg = lines[ci][cj]
        if cg == '.' or (cg == '-' and cd in "<>") or (cg == '|' and cd in "^v"):
            di, dj = transitions[cd]
            active_beams.append((ci + di, cj + dj, cd))
            continue

        if cg == '-' and cd in "v^":
            active_beams.extend([(ci, cj - 1, '<'), (ci, cj + 1, '>')])
            continue

        if cg == '|' and cd in '<>':
            active_beams.extend(([(ci + 1, cj, 'v'), (ci - 1, cj, '^')]))
            continue

        (di, dj, nd) = rotates[cd][cg]
        active_beams.append((ci + di, cj + dj, nd))

    return len(beam_locations)


def one(lines):
    return solve(lines, 0, 0, '>')


def two(lines):
    mi = len(lines)
    mj = len(lines[0])

    v1 = max((max(solve(lines, i, 0, '>'), solve(lines, i, mj-1, '<')) for i in range(mi)))
    v2 = max((max(solve(lines, 0, j, 'v'), solve(lines, mi-1, j, '^')) for j in range(mj)))
    return max(v1, v2)