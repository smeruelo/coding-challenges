#!/usr/bin/python3
# https://abc103.contest.atcoder.jp/tasks/abc103_a

a = sorted(map(int, input().split()))
cost = 0
for i in range(1, len(a)):
    cost += abs(a[i] - a[i-1])
print(cost)
