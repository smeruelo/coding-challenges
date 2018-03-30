#!/usr/bin/python3
# https://abc073.contest.atcoder.jp/tasks/abc073_c

n = int(input())
s = set()
for i in range(n):
    ai = int(input())
    if ai in s:
        s.remove(ai)
    else:
        s.add(ai)
print(len(s))
