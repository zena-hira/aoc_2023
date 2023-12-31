from solutions import *
from solutions import aoc_1, aoc_2, aoc_3, aoc_4, aoc_5, aoc_6, aoc_7, aoc_8, aoc_9, aoc_10, aoc_11, aoc_12, aoc_13, \
    aoc_14, aoc_15, aoc_16, aoc_17, aoc_18, aoc_19, aoc_20, aoc_21, aoc_22, aoc_23, aoc_24, aoc_25


def read_in(filename):
    return open(filename).read().splitlines()


lines = list(read_in('inputs/1.txt'))
print('Problem 1 A: ' + str(aoc_1.one(lines)))
print('Problem 1 B: ' + str(aoc_1.two(lines)))

lines = list(read_in('inputs/2.txt'))
print('Problem 2 A: ' + str(aoc_2.one(lines)))
print('Problem 2 B: ' + str(aoc_2.two(lines)))

lines = list(read_in('inputs/3.txt'))
print('Problem 3 A: ' + str(aoc_3.one(lines)))
print('Problem 3 B: ' + str(aoc_3.two(lines)))

lines = list(read_in('inputs/4.txt'))
print('Problem 4 A: ' + str(aoc_4.one(lines)))
print('Problem 4 B: ' + str(aoc_4.two(lines)))

lines = list(read_in('inputs/5.txt'))
print('Problem 5 A: ' + str(aoc_5.one(lines)))
print('Problem 5 B: ' + str(aoc_5.two(lines)))

lines = list(read_in('inputs/6.txt'))
print('Problem 6 A: ' + str(aoc_6.one(lines)))
print('Problem 6 B: ' + str(aoc_6.two(lines)))

lines = list(read_in('inputs/7.txt'))
print('Problem 7 A: ' + str(aoc_7.one(lines)))
print('Problem 7 B: ' + str(aoc_7.two(lines)))

lines = list(read_in('inputs/8.txt'))
print('Problem 8 A: ' + str(aoc_8.one(lines)))
print('Problem 8 B: ' + str(aoc_8.two(lines)))

lines = list(read_in('inputs/9.txt'))
print('Problem 9 A: ' + str(aoc_9.one(lines)))
print('Problem 9 B: ' + str(aoc_9.two(lines)))

lines = list(read_in('inputs/10.txt'))
print('Problem 10 A: ' + str(aoc_10.one(lines)))
print('Problem 10 B: ' + str(aoc_10.two(lines)))

lines = list(read_in('inputs/11.txt'))
print('Problem 11 A: ' + str(aoc_11.one(lines)))
print('Problem 11 B: ' + str(aoc_11.two(lines)))

lines = list(read_in('inputs/12.txt'))
print('Problem 12 A: ' + str(aoc_12.one(lines)))
print('Problem 12 B: ' + str(aoc_12.two(lines)))

lines = list(read_in('inputs/13.txt'))
print('Problem 13 A: ' + str(aoc_13.one(lines)))
print('Problem 13 B: ' + str(aoc_13.two(lines)))

lines = list(read_in('inputs/14.txt'))
print('Problem 14 A: ' + str(aoc_14.one(lines)))
print('Problem 14 B: ' + str(aoc_14.two(lines)))

lines = list(read_in('inputs/15.txt'))
print('Problem 15 A: ' + str(aoc_15.one(lines)))
print('Problem 15 B: ' + str(aoc_15.two(lines)))

lines = list(read_in('inputs/16.txt'))
print('Problem 16 A: ' + str(aoc_16.one(lines)))
print('Problem 16 B: ' + str(aoc_16.two(lines)))

lines = list(read_in('inputs/17.txt'))
print('Problem 17 A: ' + str(aoc_17.one(lines)))
print('Problem 17 B: ' + str(aoc_17.two(lines)))

lines_test = list(read_in('inputs/18_test.txt'))
print('Problem 18 A Test: ' + str(aoc_18.one(lines_test)))
lines = list(read_in('inputs/18.txt'))
print('Problem 18 A: ' + str(aoc_18.one(lines)))
lines_test = list(read_in('inputs/18_test.txt'))
print('Problem 18 B Test: ' + str(aoc_18.two(lines_test)))
lines = list(read_in('inputs/18.txt'))
print('Problem 18 B: ' + str(aoc_18.two(lines)))

lines_test = list(read_in('inputs/19_test.txt'))
print('Problem 19 A Test: ' + str(aoc_19.one(lines_test)))
lines = list(read_in('inputs/19.txt'))
print('Problem 19 A: ' + str(aoc_19.one(lines)))
lines_test = list(read_in('inputs/19_test.txt'))
print('Problem 19 B Test: ' + str(aoc_19.two(lines_test)))
lines = list(read_in('inputs/19.txt'))
print('Problem 19 B: ' + str(aoc_19.two(lines)))


lines_test = list(read_in('inputs/20_test.txt'))
print('Problem 20 A Test: ' + str(aoc_20.one(lines_test)))
lines = list(read_in('inputs/20.txt'))
print('Problem 20 A: ' + str(aoc_20.one(lines)))
lines = list(read_in('inputs/20.txt'))
print('Problem 20 B: ' + str(aoc_20.two(lines)))

lines_test = list(read_in('inputs/21_test.txt'))
print('Problem 21 A Test: ' + str(aoc_21.one(lines_test, steps=6)))
lines = list(read_in('inputs/21.txt'))
print('Problem 21 A: ' + str(aoc_21.one(lines)))
lines = list(read_in('inputs/21.txt'))
print('Problem 21 B: ' + str(aoc_21.two(lines)))

lines_test = list(read_in('inputs/22_test.txt'))
print('Problem 22 A Test: ' + str(aoc_22.one(lines_test)))
lines = list(read_in('inputs/22.txt'))
print('Problem 22 A: ' + str(aoc_22.one(lines)))
lines = list(read_in('inputs/22.txt'))
print('Problem 22 B Test: ' + str(aoc_22.two(lines_test)))
lines = list(read_in('inputs/22.txt'))
print('Problem 22 B: ' + str(aoc_22.two(lines)))

lines_test = list(read_in('inputs/23_test.txt'))
print('Problem 23 A Test: ' + str(aoc_23.one(lines_test)))
lines = list(read_in('inputs/23.txt'))
print('Problem 23 A: ' + str(aoc_23.one(lines)))
lines = list(read_in('inputs/23.txt'))
print('Problem 23 B Test: ' + str(aoc_23.two(lines_test)))
lines = list(read_in('inputs/23.txt'))
print('Problem 23 B: ' + str(aoc_23.two(lines)))

lines_test = list(read_in('inputs/24_test.txt'))
print('Problem 24 A Test: ' + str(aoc_24.one(lines_test, min_bound=7, max_bound=27)))
lines = list(read_in('inputs/24.txt'))
print('Problem 24 A: ' + str(aoc_24.one(lines)))
lines = list(read_in('inputs/24.txt'))
print('Problem 24 B Test: ' + str(aoc_24.two(lines_test)))
lines = list(read_in('inputs/24.txt'))
print('Problem 24 B: ' + str(aoc_24.two(lines)))

lines = list(read_in('inputs/25_test.txt'))
print('Problem 25 A Test: ' + str(aoc_25.one(lines)))
lines = list(read_in('inputs/25.txt'))
print('Problem 25 A: ' + str(aoc_25.one(lines)))
