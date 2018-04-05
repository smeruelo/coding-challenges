#!/usr/bin/python3
# https://abc061.contest.atcoder.jp/tasks/abc061_b

from collections import defaultdict

n, m = map(int, input().split())
count = defaultdict(int)
for _ in range(m):
    c1, c2 = map(int, input().split())
    count[c1] += 1
    count[c2] += 1
for i in range(1, n + 1):
    print(count[i])
