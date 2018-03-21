#!/usr/bin/python3
# https://abc051.contest.atcoder.jp/tasks/abc051_b

k, s = list(map(int, input().split()))
count = 0
for x in range(min(k, s) + 1):
    for y in range(min(k, s-x) + 1):
        if s - x - y <= k:
            count += 1
print(count)
