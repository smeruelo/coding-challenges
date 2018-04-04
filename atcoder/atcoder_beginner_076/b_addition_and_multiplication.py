#!/usr/bin/python3
# https://abc076.contest.atcoder.jp/tasks/abc076_b

n = int(input())
k = int(input())
value = 1
for _ in range(n):
    value = min(value + k, value * 2)
print(value)
