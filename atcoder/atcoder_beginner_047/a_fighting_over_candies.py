#!/usr/bin/python3
# https://abc047.contest.atcoder.jp/tasks/abc047_a

a, b, c = list(map(int, input().split()))
print('Yes') if a + b == c or a + c == b or c + b == a else print('No')
