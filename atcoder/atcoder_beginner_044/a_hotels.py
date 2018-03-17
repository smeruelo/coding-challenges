#!/usr/bin/python2
# https://abc044.contest.atcoder.jp/tasks/abc044_a


n = int(raw_input())
k = int(raw_input())
x = int(raw_input())
y = int(raw_input())
print min(k, n) * x + (n - k) * y if n > k else min(k, n) * x
