#!/usr/bin/python2
from itertools import permutations

for _ in range(input()):
    s, c = map(int, raw_input().split())
    a = 0
    t = 0
    n = s * c
    for x in permutations(range(n)):
        t += 1
        x = [i/s for i in x]
        k = False
        q = False
        for i in range(n - 1):
            if x[i] == 0 and x[i + 1] == 0:
                k = True
            if x[i] == 1 and x[i + 1] == 1:
                q = True
        if k and q: a += 1
    print a / float(t)
