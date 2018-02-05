#!/usr/bin/python2
# https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

def maximize(lists, M):
    maximum = 0
    for i in product(*lists):
        maximum = max(maximum, sum(map(lambda x: x**2, i)) % M)
    return maximum


if __name__ == '__main__':
    K, M = map(int, raw_input().split())
    lists = []
    for _ in range(K):
        lists.append(map(int, raw_input().split()[1:]))
    print maximize(lists, M)

