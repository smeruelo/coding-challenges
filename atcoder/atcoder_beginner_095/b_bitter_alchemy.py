#!/usr/bin/python3
# https://abc095.contest.atcoder.jp/tasks/abc095_b

n, x = map(int, input().split())
grams = [int(input()) for _ in range(n)]
print(len(grams) + (x - sum(grams)) // min(grams))
