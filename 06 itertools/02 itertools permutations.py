#!/usr/bin/python2
# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

if __name__ == '__main__':
    s, k = raw_input().split()
    print '\n'.join(sorted(map(lambda t: ''.join(t), list(permutations(s, int(k))))))
