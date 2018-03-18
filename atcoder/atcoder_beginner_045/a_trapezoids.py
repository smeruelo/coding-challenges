#!/usr/bin/python3
# https://abc045.contest.atcoder.jp/tasks/abc045_a

a = int(input())
b = int(input())
h = int(input())
print(int((min(a, b) * h) + ((max(a, b) - min(a, b)) * h / 2)))
