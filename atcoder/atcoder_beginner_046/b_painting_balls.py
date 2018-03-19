#!/usr/bin/python3
# https://abc046.contest.atcoder.jp/tasks/abc046_b


n, k = list(map(int, input().split()))
combinations = k
for _ in range(1, n):
    combinations *= k - 1
print(combinations)
