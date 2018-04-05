#!/usr/bin/python3
# https://abc061.contest.atcoder.jp/tasks/abc061_c

def kth_smallest(a, k):
    accum = 0
    for elem in a:
        accum += elem[1]
        if accum >= k:
            return elem[0]


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    print(kth_smallest(a, k))
