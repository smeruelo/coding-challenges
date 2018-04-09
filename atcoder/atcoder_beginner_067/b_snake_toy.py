#!/usr/bin/python3
# https://abc067.contest.atcoder.jp/tasks/abc067_b

n, k = map(int, input().split())
l = sorted(map(int, input().split()), reverse = True)
print(sum(l[:k]))
