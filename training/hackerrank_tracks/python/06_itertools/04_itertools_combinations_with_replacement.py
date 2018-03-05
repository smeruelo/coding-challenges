#!/usr/bin/python2
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

if __name__ == '__main__':
    line = raw_input().split()
    s = sorted(line[0])
    k = int(line[1])
    print '\n'.join(sorted(map(lambda t: ''.join(t), list(combinations_with_replacement(s, k)))))
