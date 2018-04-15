#!/usr/bin/python3
# https://abc094.contest.atcoder.jp/tasks/abc094_b

def min_toll(x, n, tolls):
    toll_to_0 = toll_to_n = 0
    for i in range(1, x):
        toll_to_0 += i in tolls
    for i in range(x + 1, n + 1):
        toll_to_n += i in tolls
    return min(toll_to_0, toll_to_n)


if __name__ == '__main__':
    n, _, x = map(int, input().split())
    tolls = list(map(int, input().split()))
    print(min_toll(x, n, tolls))
