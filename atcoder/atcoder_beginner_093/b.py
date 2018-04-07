#!/usr/bin/python3
# https://abc093.contest.atcoder.jp/tasks/abc093_b

a, b, k = map(int, input().split())
for i in range(a, min(a + k, b + 1)):
    print(i)
for j in range(max(i + 1, b - k + 1), b + 1):
    print(j)
