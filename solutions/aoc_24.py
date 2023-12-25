import math

from z3 import Int, Solver


def parse(lines):
    hails = []
    for line in lines:
        raw_coord, raw_vec = line.split('@')
        coord = tuple(map(int, raw_coord.split(',')))
        vec = tuple(map(int, raw_vec.split(',')))
        hails.append((coord, vec))
    return hails
def one(lines, min_bound=200000000000000, max_bound=400000000000000):
    hails = parse(lines)

    count = 0
    for i, hail1 in enumerate(hails):
        for hail2 in hails[i+1:]:
            p = intersect_point(hail1, hail2)
            if p is None:
                continue
            (ix, iy) = p
            if min_bound <= ix <= max_bound and min_bound <= iy <= max_bound:
                count += 1

    return count
    exit(1)

def intersect_point(hail1, hail2):
    (x1, y1, _), (dx1, dy1, _) = hail1
    (x2, y2, _), (dx2, dy2, _) = hail2

    a1 = dy1 / dx1
    a2 = dy2 / dx2
    c1 = y1 - a1 * x1
    c2 = y2 - a2 * x2

    if a1 == a2:
        return None

    x = (c2 - c1) / (a1 - a2)
    y = a1 * x + c1

    t1 = (x - x1) / dx1
    t2 = (x - x2) / dx2
    if t1 < 0 or t2 < 0:
        return None

    return x,y


def find_future_2D_segment_in_area(hail, min_bound, max_bound):
    ((x,y,_), (dx, dy, _)) = hail

    xt1 = (min_bound - x) / dx
    xt2 = (max_bound - x) / dx

    if xt1 < 0 and xt2 < 0:
        return None

    xt1 = max(0, xt1)
    xt2 = max(0, xt2)

    yt1 = (min_bound - y) / dy
    yt2 = (max_bound - y) / dy

    if yt1 < 0 and yt2 < 0:
        return None

    yt1 = max(0, yt1)
    yt2 = max(0, yt2)

    xt1, xt2 = sorted([xt1, xt2])
    yt1, yt2 = sorted([yt1, yt2])

    t1 = max(xt1, yt1)
    t2 = min(xt2, yt2)

    if t2 < t1:
        return None

    return (x + t1*dx, y+ t1*dy ), (x + t2*dx, y+t2*dy)

def two(lines):
    hails = parse(lines)

    x, y, z, dx, dy, dz = map(Int, ["x","y","z","dx","dy","dz"])
    s = Solver()

    for (ht, ((hx, hy, hz), (hdx, hdy, hdz))) in enumerate(hails):
        t_ht = Int(f"t_{ht}")
        s.add(t_ht >= 0)
        s.add(hx + t_ht * hdx == x + t_ht * dx)
        s.add(hy + t_ht * hdy == y + t_ht * dy)
        s.add(hz + t_ht * hdz == z + t_ht * dz)

    print(s.check())
    m = s.model()

    return int(f"{m[x]}") + int(f"{m[y]}") + int(f"{m[z]}")
