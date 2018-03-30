#!/usr/bin/python3
# https://abc072.contest.atcoder.jp/tasks/abc072_b

s = input()
print(''.join([s[i] if i % 2 == 0 else '' for i in range(len(s))]))
