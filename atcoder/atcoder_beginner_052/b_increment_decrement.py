#!/usr/bin/python3
# https://abc052.contest.atcoder.jp/tasks/abc052_b

n = int(input())
s = input()
x = maximum = 0
for op in s:
    x = x + 1 if op == 'I' else x - 1
    maximum = max(maximum, x)
print(maximum)
