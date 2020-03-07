#!/usr/bin/env python
# https://www.codechef.com/WICP2002/problems/WICP007

from itertools import combinations, permutations

MOD = 10**9 + 7

def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def reachable(s):
    "Returns all the strings that can be obtained by 1 swap op from s."
    n = len(s)
    sim = set()
    for i, j in combinations(range(n), 2):
        sim.add(swap(s, i, j))
    return sim

def are_similar(a, b):
    return bool(reachable(a).intersection(reachable(b)))

def count_naive(s):
    return sum(map(lambda x: not are_similar(x[0], x[1]),
                   combinations(map(lambda p: ''.join(p), permutations(s)), 2))) % MOD


for _ in range(int(input())):
    print(count(input()))
