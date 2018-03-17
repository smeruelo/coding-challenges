#!/usr/bin/python3
# https://abc044.contest.atcoder.jp/tasks/abc044_b

from collections import Counter

word = input()
c = Counter(word)
counts = c.values()
print('Yes') if all(map(lambda x: x % 2 == 0, counts)) else print('No')
