#!/usr/bin/python3
# https://abc060.contest.atcoder.jp/tasks/arc073_a

n, t = map(int, input().split())
switches = list(map(int, input().split()))
time = 0
for i in range(1, n):
    if switches[i] - switches[i-1] < t:
        time += switches[i] - switches[i-1]
    else:
        time += t
time += t
print(time)
