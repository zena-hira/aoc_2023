import re
from collections import Counter


def one(lines):
    return -1
    s = 0
    for line in lines:
        pattern, raw_nums = line.split()
        nums = list(map(int,raw_nums.split(',')))

        p = r'[.?]*' + r'[.?]+'.join([r'[?#]{' + str(num) + '}' for num in nums]) + r'[.?]*'
        variants = {""}
        for c in pattern:
            v2 = set()
            for v in variants:
                if c in "#.":
                    v2.add(v+c)
                elif c == "?":
                    v2.add(v+".")
                    v2.add(v+"#")
            variants = v2

        s += sum(1 for v in variants if re.fullmatch(p, v))

    return s

def two(lines):
    s = 0
    for line in lines:
        if line == '':
            break
        pattern, raw_nums = line.split()
        nums = list(map(int,raw_nums.split(',')))

        p2 = "?".join([pattern]*5)
        n2 = nums * 5

        s += solve(p2, n2)
    return s

def solve(line, nums):

    states = { (0, line, tuple(nums)) : 1 } # possible spring length, line left, nums left

    count = 0

    while states:
        s2 = states
        states = Counter()
        for curr, curr_count in s2.items():

            len_so_far, line_left, nums_left = curr

            if line_left == "" :
                if len(nums_left) == 0 and len_so_far == 0:
                    count += curr_count

                if len(nums_left) == 1 and len_so_far == nums_left[0]:
                    count += curr_count
                continue

            c = line_left[0]
            rest = line_left[1:]

            if c == ".":
                dot_case(len_so_far, nums_left, rest, states, curr_count)
                continue

            if c == "#":
                hash_case(nums_left, len_so_far, rest, states, curr_count)
                continue

            if c == "?":
                dot_case(len_so_far, nums_left, rest, states, curr_count)
                hash_case(nums_left, len_so_far, rest, states, curr_count)
                continue

    return count


def dot_case(len_so_far, nums_left, rest, states, curr_count):
     if len_so_far != 0 and len(nums_left) > 0 and nums_left[0] == len_so_far:
         states[(0, rest, nums_left[1:])] += curr_count
     elif len_so_far == 0:
         states[(0, rest, nums_left)] += curr_count


def hash_case(nums_left, len_so_far, rest, states, curr_count):
    if len(nums_left) > 0 and nums_left[0] > len_so_far:
        states[(len_so_far + 1, rest, nums_left)] += curr_count