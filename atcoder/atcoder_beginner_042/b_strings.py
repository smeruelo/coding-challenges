#!/usr/bin/python3
# https://abc042.contest.atcoder.jp/tasks/abc042_b

n, _ = map(int, input().split())
words = sorted([input() for _ in range(n)])
print(''.join(words))
