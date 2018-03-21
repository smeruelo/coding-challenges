#!/usr/bin/python3
# https://abc050.contest.atcoder.jp/tasks/abc050_b

_ = input()
t = list(map(int, input().split()))
total_time = sum(t)
for _ in range(int(input())):
    p, x = list(map(int, input().split()))
    print(total_time - t[p-1] + x)
