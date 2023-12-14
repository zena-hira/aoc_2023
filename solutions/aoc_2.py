def parse_one(line):
    game, games = line.split(': ')
    _, id = game.split(' ')
    parts = games.split('; ')
    rs = []
    for part in parts:
        mp = {}
        for one in part.split(', '):
            count, colour = one.split(' ')
            mp[colour] = int(count)
        rs.append(mp)
    return int(id), rs

def parse(lines):
    return [parse_one(line) for line in lines]

one_limits = { 'red': 12, 'green': 13, 'blue': 14 }

def is_valid(obs, limits):
    if not (obs.keys() <= limits.keys()):
        return False

    for key, count in obs.items():
        if count > limits[key]:
            return False
    return True

def one(lines):
    s = 0
    for id, obss in parse(lines):
        if not all([is_valid(obs, one_limits) for obs in obss]):
            continue
        s += id
    return s

def find_min_power(obss):
    r = max([obs.get('red', 0) for obs in obss])
    g = max([obs.get('green', 0) for obs in obss])
    b = max([obs.get('blue', 0) for obs in obss])
    return r*g*b

def two(lines):
    return sum([find_min_power(obss) for id, obss in parse(lines)])