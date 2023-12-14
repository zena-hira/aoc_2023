from collections import defaultdict


def parse(lines):
    maze = defaultdict(set)
    start = None

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            cpos = (i,j)
            c = lines[i][j]
            if c == 'S':
                start = (i,j)
            if c == '|':
                maze[cpos] = { (i-1, j), (i+1, j) }
            if c == '-':
                maze[cpos] = { (i, j-1), (i, j+1) }
            if c == 'L':
                maze[cpos] = { (i-1, j), (i, j+1) }
            if c == 'J':
                maze[cpos] = { (i-1, j), (i, j-1) }
            if c == '7':
                maze[cpos] = { (i+1, j), (i, j-1) }
            if c == 'F':
                maze[cpos] = { (i+1, j), (i, j+1) }
    return start, maze

def one(lines):
    start, maze = parse(lines)
    (si, sj) = start

    paths = {}
    for c in [(si-1, sj), (si+1, sj), (si, sj-1), (si, sj+1)]:
        p = find_path_to(start, c, maze)
        if p:
            return (p[0]+1) // 2


def find_path_to(start, c, maze):

    l = 0

    current = c
    prev = start
    loop_coords = {start, c}

    while True:
        nexts = maze[current]

        if prev not in nexts:
            return None

        next_as_set = nexts - {prev}
        if len(next_as_set) == 0:
            return None

        prev = current
        current = list(next_as_set)[0]
        loop_coords.add(current)
        l += 1

        if current == start:
            return l, loop_coords
        if current == c:
            return None

def two(lines):
    start, maze = parse(lines)
    (si, sj) = start

    coords = None
    for c in [(si-1, sj), (si+1, sj), (si, sj-1), (si, sj+1)]:
        p = find_path_to(start, c, maze)
        if p:
            coords = p[1]
            break

    count = 0
    for i in range(len(lines)):
        am_inside = False
        for j in range(len(lines[0])):
            if (i,j) in coords:
                if lines[i][j] in "JL|S":   # s is map specific
                    am_inside = not am_inside
                #print('.',end='')
            else:
                count += (1*am_inside)
                #print("OI"[1*am_inside], end='')
        #print()
    return count
