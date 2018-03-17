#!/usr/bin/python2
# https://abc091.contest.atcoder.jp/tasks/abc091_a

a, b, c = map(int, raw_input().split())
print 'Yes' if c <= (a + b) else 'No'
