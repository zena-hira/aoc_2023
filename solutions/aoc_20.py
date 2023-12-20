import math
from collections import defaultdict


def parse(lines):
    machines = {}

    for line in lines:
        raw_name, raw_outputs = line.split(' -> ')
        outputs = raw_outputs.split(', ')
        name = None
        state = None
        tipe = None
        match raw_name[0]:
            case '%':
                name = raw_name[1:]
                tipe = '%'
                state = False
            case '&':
                name = raw_name[1:]
                tipe = '&'
                state = {}
            case 'b':
                name = raw_name
                tipe = 'b'
                state = ()
        machines[name] = (tipe, state, outputs)

    for name, (tipe, state, outputs) in machines.items():
        for output in outputs:
            if output in machines and machines[output][0] == '&':
                machines[output][1][name] = False

    return machines
def one(lines):
    machines = parse(lines)
    c_lo = 0
    c_high = 0
    for i in range(1000):
        cl, hi, _ = press_button_once(machines)
        c_lo += cl
        c_high += hi
    return c_lo * c_high
def press_button_once(machines, start='broadcaster', source='button', target=None):
    q = [(False, start, source)]
    c_low = 0
    c_high = 0
    tripped = False
    while q:
        signal, dest, source = q.pop(0)
        if signal:
            c_high += 1
        else:
            c_low += 1

        if dest not in machines:
            continue

        (tipe, state, outputs) = machines[dest]
        next_state, next_pulse = apply(tipe, state, signal, source)
        machines[dest] = (tipe, next_state, outputs)
        if next_pulse is not None:
            if target and (dest in target) and next_pulse:
                tripped = True
            q.extend((next_pulse, output, dest) for output in outputs)

    return c_low, c_high, tripped

def apply(tipe, state, signal, input_name):
    match tipe:
        case 'b':
            return state, signal
        case '%':
            if signal:
                return state, None
            return not state, not state
        case '&':
            state[input_name] = signal
            if all(state.values()):
                return state, False
            else:
                return state, True


def two(lines):

    lcm = 1
    for start,end in [('nt', 'sp'), ('kx', 'zv'), ('rc', 'xt'), ('mg', 'lk')]:
        count = find_loop_one(start, end, parse(lines))
        lcm = math.lcm(count, lcm)
    return lcm

    machines = parse(lines)
    dests = machines['dg'][1].keys()
    for x in ['nt', 'kx', 'rc', 'mg']:
        print(x)
        print_loops(machines, x, dests)

def find_loop_one(start, end, machines):
    count = 0
    loops = []
    while True:
        _, _, tripped = press_button_once(machines, start='broadcaster', source='button', target=[end])
        count += 1

        if tripped:
            loops.append(count)
            if len(loops) > 2:
                return loops[-2] - loops[-1]

def freeze_machines(machines):
    v = []
    for k in sorted(machines.keys()):
        if k == 'dg':
            continue
        (tipe, state, outputs) = machines[k]
        match tipe:
            case '%': v.append(state)
            case '&':
                for sk in sorted(state.keys()):
                    v.append(state[sk])
    return tuple(v)

def print_loops(machines, x, dests):
    seen = set()
    loop = set()
    q = [x]
    while q:
        curr = q.pop()
        if curr not in machines:
            continue
        if curr in seen:
            loop.add(curr)
            continue
        if curr in dests:
            print('DEST', curr)
        seen.add(curr)
        (tipe, state, outputs) = machines[curr]
        q.extend(outputs)
    print(loop)