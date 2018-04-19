#!/usr/bin/python3
# https://abc087.contest.atcoder.jp/tasks/arc090_a

from itertools import accumulate

def candies(a, n):
    top = accumulate(a[0])
    bottom = list(accumulate(a[1][::-1]))
    bottom.reverse()
    return max(map(lambda x, y: x + y, top, bottom))


if __name__ == '__main__':
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    print(candies(a, n))
