#!/usr/bin/python3
# https://abc049.contest.atcoder.jp/tasks/abc049_b

h, _ = list(map(int, input().split()))
pixels = [input() for i in range(h)]
for row in [pixels[j//2] for j in range(2*h)]:
    print(row)
