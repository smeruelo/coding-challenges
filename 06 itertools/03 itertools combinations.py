#!/usr/bin/python2
# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

if __name__ == '__main__':
    line = raw_input().split()
    s = sorted(line[0])
    k = int(line[1])
    for i in range(1, k + 1):
        print '\n'.join(sorted(map(lambda t: ''.join(t), list(combinations(s, i)))))

