#!/usr/bin/python3
# https://abc090.contest.atcoder.jp/tasks/abc090_a

letters = [input() for _ in range(3)]
print(''.join([letters[i][i] for i in range(3)]))
