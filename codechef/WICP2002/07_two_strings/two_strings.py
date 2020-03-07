#!/usr/bin/env python
# https://www.codechef.com/WICP2002/problems/WICP007


# P = permutations of string A
# number of pairs: P^2
# S = number of pairs that are similar  --> number of pairs that not = P^2 - S
# T = number of strings similar to A
# It can be shown (?!?) that S = P*T
# So, answer is P^2 - P*T
# T = T0 + T1 + T2 + T3
#   T0: Strings formed from A with no swaps = 1
#   T1: Strings formed from A with one swap.
#   T2: Strings formed from A with two disjoint swaps.
#   T3: Strings formed from A with two overlapping swaps (3 types: 0/1/2 letters in common)

from collections import Counter
from functools import reduce
from math import factorial
from string import ascii_lowercase as alf

MOD = 10**9 + 7


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def calc_p(A, n, f):
    num = f[n]
    den = reduce(lambda x, y: (x * y) % MOD, [f[A[c]] for c in alf])
    #print(num, den, (num * modinv(den, MOD)) % MOD)
    return (num * modinv(den, MOD)) % MOD


def calc_t(A):

    t0 = 1

    t1 = 0
    for i in range(len(alf)):
        for j in range(i):
            t1 += A[alf[i]] * A[alf[j]]

    t2 = 0
    for i in range(len(alf)):
        for j in range(i):
            for k in range(j):
                t2 += 2 * A[alf[i]] * A[alf[j]] * A[alf[k]]

    t3 = 0
    # No letters in common
    for i in range(len(alf)):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    t3 += 3 * A[alf[i]] * A[alf[j]] * A[alf[k]] * A[alf[l]]
    # One letter in common
    for i in range(len(alf)):
        for j in range(len(alf)):
            if i != j:
                for k in range(j):
                    if i != k:
                        t3 += A[alf[i]] * (A[alf[i]]-1) * A[alf[j]] * A[alf[k]]
    # Two letters in common
    for i in range(len(alf)):
        for j in range(i):
            t3 += A[alf[i]] * (A[alf[i]]-1)//2 * A[alf[j]] * (A[alf[j]]-1)//2

    return t0 + t1 + t2 + t3


def calc_factorials(x):
    f = [1]
    for i in range(1, x + 1):
        f.append(f[-1] * i % MOD)
    return f


def count(A):
    letters = Counter(A)
    f = calc_factorials(10 ** 5)
    p = calc_p(letters, len(A), f)
    t = calc_t(letters)
    return (p * p - p * t) % MOD


for _ in range(int(input())):
    print(count(input()))
