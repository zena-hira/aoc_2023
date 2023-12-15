from collections import defaultdict


def one(lines):
    input = lines[2]

    rs = [my_hash(instr) for instr in input.split(',')]
    return sum(rs)

def my_hash(stuff):
    n = 0
    for c in stuff:
        n += ord(c)
        n *= 17
        n %= 256
    return n
def two(lines):
    input = lines[2]

    boxes = defaultdict(list)
    for instr in input.split(','):
        if instr[-1] == '-':
            label = instr[0:-1]
            val = my_hash(label)
            boxes[val] = [ (l,f) for l,f in boxes[val] if l != label ]
        else:
            label, focal = instr.split('=')
            focal = int(focal)
            val = my_hash(label)

            existing = boxes[val]
            if label in [l for l,f in existing]:
                change = { label: focal}
                boxes[val] = [ (l, change.get(l, f)) for l,f in existing ]
            else:
                boxes[val] = existing + [(label, focal)]
    s = 0
    for box_num, lenses in boxes.items():
        for (i, (l, f)) in enumerate(lenses):
            s+= (1 + box_num) * f * (i+1)
    return s