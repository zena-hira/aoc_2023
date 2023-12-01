import re


def one(lines):
    s = 0
    for line in lines:
        two = re.match(r'.*?(\d).*(\d)', line)
        one = re.search(r'(\d)', line)
        if two:
            f, l = two.groups()
        else:
            n, = one.groups()
            f = n
            l = n
        x = (int(f)*10 +  int(l))
        s += x
    return s

remap = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
def two(lines):
    pat = r'.*?(one|two|three|four|five|six|seven|eight|nine|\d).*(one|two|three|four|five|six|seven|eight|nine|\d)'
    s = 0
    for line in lines:
        two = re.match(pat, line)
        one = re.search(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line)
        if two:
            f,l = two.groups()
        else:
            n, = one.groups()
            f = n
            l = n

        f = remap.get(f, f)
        l = remap.get(l, l)

        x = (int(f)*10 +  int(l))
        s += x
    return s