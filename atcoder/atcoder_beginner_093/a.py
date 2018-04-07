#!/usr/bin/python3
# https://abc093.contest.atcoder.jp/tasks/abc093_a

from itertools import permutations

s = input()
if s in map(lambda x: ''.join(x), permutations('abc')):
    print('Yes')
else:
    print('No')
