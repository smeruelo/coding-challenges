#!/usr/bin/python3
# https://abc081.contest.atcoder.jp/tasks/arc086_a

from collections import Counter

_, k = map(int, input().split())
balls = Counter(map(int, input().split()))
print(sum(sorted(balls.values(), reverse=True)[k:]))
