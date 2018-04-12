#!/usr/bin/python3
# https://abc078.contest.atcoder.jp/tasks/arc085_a

n, m = map(int, input().split())
print(((m * 1900) + (n - m) * 100) * (2 ** m))
