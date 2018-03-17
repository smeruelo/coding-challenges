#!/usr/bin/python2
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    A = defaultdict(list)
    for i in range(1, n + 1):
        A[raw_input()].append(i)
    for i in range(m):
        b = raw_input()
        if b in A:
            print ' '.join(map(str, A[b]))
        else:
            print '-1'
