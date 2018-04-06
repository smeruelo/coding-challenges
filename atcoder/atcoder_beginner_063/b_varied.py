#!/usr/bin/python3
# https://abc063.contest.atcoder.jp/tasks/abc063_b

from collections import Counter

s = input()
c = Counter(s)
print('yes') if len(s) == len(c) else print('no')
