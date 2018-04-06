#!/usr/bin/python3
# https://abc064.contest.atcoder.jp/tasks/abc064_b

_ = input()
a = sorted(map(int, input().split()))
print(a[-1] - a[0])
