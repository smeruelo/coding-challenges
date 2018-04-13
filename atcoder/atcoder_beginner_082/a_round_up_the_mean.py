#!/usr/bin/python3
# https://abc082.contest.atcoder.jp/tasks/abc082_a

def ceil_div(num, den):
    return ((num - 1) // den) + 1

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(ceil_div(a + b, 2))
