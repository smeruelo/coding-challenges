#!/usr/bin/python3
# https://abc082.contest.atcoder.jp/tasks/abc082_b

s = input()
t = input()
print('Yes') if sorted(s) < sorted(t, reverse=True) else print('No')
