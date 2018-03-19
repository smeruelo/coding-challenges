#!/usr/bin/python3
# https://abc046.contest.atcoder.jp/tasks/abc046_a

from collections import Counter

colours = Counter(list(map(int, input().split())))
print(len(list(colours)))
