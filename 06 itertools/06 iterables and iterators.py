#!/usr/bin/python2
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

if __name__ == '__main__':
    _ = raw_input()
    letters = raw_input().split()
    size = int(raw_input())
    combos = list(combinations(letters, size))
    p = sum(map(lambda x: 1 if 'a' in x else 0, combos)) / float(len(combos))
    print '{0:.4f}'.format(p)
