#!/usr/bin/python3
# https://www.hackerrank.com/challenges/unbounded-knapsack/problem

import sys

sys.setrecursionlimit(3000)


def knapsack(n, target, sizes):
    mem = [[None] * target for _ in range(n)]

    def aux(i, t):
        if i == -1:
            return 0
        if mem[i][t-1]:
            return mem[i][t-1]
        if sizes[i] > t:
            result = aux(i - 1, t)
        else:
            result = max(sizes[i] + aux(i, t - sizes[i]),
                         sizes[i] + aux(i - 1, t - sizes[i]),
                         aux(i - 1, t))
        mem[i][t-1] = result
        return result

    return aux(n - 1, target)


if __name__ == '__main__':
    for _ in range(int(input())):
        n, target = map(int, input().split())
        sizes = list(set(map(int, input().split())))
        print(knapsack(len(sizes), target, sizes))
