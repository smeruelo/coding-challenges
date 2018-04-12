#!/usr/bin/python3
# https://abc080.contest.atcoder.jp/tasks/abc080_b

n = input()
print('Yes') if int(n) % sum(map(int, n)) == 0 else print('No')
