#!/usr/bin/python2
# https://abc042.contest.atcoder.jp/tasks/abc042_a

from itertools import permutations

phrases = tuple(map(int, raw_input().split()))
print 'YES' if phrases in permutations([5, 7, 5], 3) else 'NO'
