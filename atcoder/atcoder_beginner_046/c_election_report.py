#!/usr/bin/python3
# https://abc046.contest.atcoder.jp/tasks/arc062_a

from math import ceil

def votes(t, a):
    def ceil(a, b):
        return (a + b - 1) // b

    votes_t = votes_a = 1
    for i in range(len(t)):
        k = max(ceil(votes_t, t[i]), ceil(votes_a, a[i]))
        votes_t = t[i] * k
        votes_a = a[i] * k
    return votes_t + votes_a


if __name__ == '__main__':
    lines = [list(map(int, input().split())) for _ in range(int(input()))]
    t = [l[0] for l in lines]
    a = [l[1] for l in lines]
    print(votes(t, a))
