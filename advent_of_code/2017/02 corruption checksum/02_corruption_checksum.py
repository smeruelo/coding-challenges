#!/usr/bin/python3
# https://adventofcode.com/2017/day/2

def evenly_divide(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] % l[j] == 0:
                return l[i] // l[j]

if __name__ == '__main__':
    with open('02_corruption_checksum.input') as f:
        data = [list(map(int, l.split())) for l in f.readlines()]

    # part 1
    print(sum([max(row) - min(row) for row in data]))

    # part 2
    print(sum([evenly_divide(row) for row in data]))
