#!/usr/bin/python3
# https://abc095.contest.atcoder.jp/tasks/arc096_a

a, b, c, x, y = map(int, input().split())
print(min([(x * a + y * b), \
           2 * c * min(x, y) + a * max(0, x - y) + b * max(0, y - x), \
           2 * c * max(x, y)]))
