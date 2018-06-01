#!/usr/bin/python3
# https://abc098.contest.atcoder.jp/tasks/abc098_a

a, b = map(int, input().split())
print(max(a + b, a - b, a * b))
