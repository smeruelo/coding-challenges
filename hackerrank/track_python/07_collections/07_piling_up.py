#!/usr/bin/python2
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def pile_up(cubes):
    d = deque(cubes)

    def pop_max():
        """ Pops the bigger value in deque's extremes """
        if d[0] > d[len(d) - 1]:
            popped = d.popleft()
        else:
            popped = d.pop()
        return popped

    current = pop_max()
    while len(d) > 0:
        popped = pop_max()
        if popped <= current:
            current = popped
        else:
            return False
    return True


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _ = raw_input()
        cubes = map(int, raw_input().split())
        output = {True: 'Yes', False: 'No'}
        print output[pile_up(cubes)]
