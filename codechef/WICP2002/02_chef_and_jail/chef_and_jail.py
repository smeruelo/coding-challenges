#!/usr/bin/env python
# https://www.codechef.com/WICP2002/problems/CHJAIL

from sys import stdin

def read():
    input_data = stdin.read().split()
    for token in input_data:
        yield token

def tokens(g, n):
    t = []
    for _ in range(n):
        t.append(next(g))
    return t


def escapable(jail, m, n, target):

    def next_rooms(room):
        return filter(lambda r: r[0] <= target[0] and r[1] <= target[1],
                      [(room[0], room[1]+1), (room[0]+1, room[1]), (room[0]+1, room[1]+1)])

    def aux(room, power):
        if room == target:
            return power >= 0
        if power > 0:
            for r in next_rooms(room):
                if aux(r, power - jail[r[0]][r[1]]):
                    return True
        return False

    return aux((0, 0), jail[0][0])


reader = read()
for _ in range(int(next(reader))):
    m, n, x, y = map(int, tokens(reader, 4))
    jail = []
    for row in range(m):
        jail.append(list(map(int, tokens(reader, n))))
    if escapable(jail, m, n, (y-1, x-1)):
        print('Escape')
    else:
        print('Died')
