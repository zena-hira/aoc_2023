def parse(lines):
    cubes = []
    for id, line in enumerate(lines):
        e1, e2 = line.split('~')
        cubes.append((chr(65 +id),
            tuple(map(int,e1.split(','))),
            tuple(map(int,e2.split(',')))
        ))
    return cubes

def one(lines):
    cubes = parse(lines)
    cubes_by_id = { id: (c1, c2) for (id, c1, c2) in cubes}

    space = drop(cubes_by_id)

    count = 0
    for id in cubes_by_id.keys():
        test_cubes_by_id = cubes_by_id.copy()
        del test_cubes_by_id[id]
        if drop(test_cubes_by_id, break_if_something_moves=True) != 123:
            count += 1
    return count

def drop(cubes_by_id, break_if_something_moves=False, track_falls=False):
    todo = set(cubes_by_id.keys())
    space = {}
    falls = set()
    while todo:
        changed = True
        while changed:
            changed = False
            next_todo = set()
            for id in sorted(todo, key=lambda k: cubes_by_id[k][0][2]):
                c1, c2 = cubes_by_id[id]
                if is_at_rest(c1, c2, space):
                    changed = True
                    for (x, y, z) in all_coords(c1, c2):
                        space[(x, y, z)] = id
                else:
                    next_todo.add(id)
            todo = next_todo
        if todo and break_if_something_moves:
            return 123
        if track_falls:
            falls.update(todo)
        drop_todo(todo, cubes_by_id)

    if track_falls:
        return falls
    else:
        return space


def drop_todo(todo, cubes_by_id):
    for id in todo:
        (x1,y1,z1), (x2,y2,z2) = cubes_by_id[id]
        cubes_by_id[id] = ((x1,y1,z1-1), (x2,y2,z2-1))

def is_at_rest(c1, c2, space):
    for (x, y, z) in all_coords(c1, c2):
        if z == 1 or (x, y, z - 1) in space:
            return True
    return False

def all_coords(c1, c2):
    (x1, y1, z1) = c1
    (x2, y2, z2) = c2
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1):
                yield (x,y,z)

def two(lines):
    cubes = parse(lines)
    cubes_by_id = { id: (c1, c2) for (id, c1, c2) in cubes}

    space = drop(cubes_by_id)

    count = 0
    for id in cubes_by_id.keys():
        test_cubes_by_id = cubes_by_id.copy()
        del test_cubes_by_id[id]
        falls = drop(test_cubes_by_id, break_if_something_moves=False, track_falls=True)
        count = len(falls) + count
    return count

