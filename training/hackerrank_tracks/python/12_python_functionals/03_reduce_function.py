#!/usr/bin/python2
# https://www.hackerrank.com/challenges/reduce-function/problem

from __future__ import print_function
from fractions import Fraction

def product(fracs):
    result = reduce(lambda x, y: x * y, fracs)
    return result.numerator, result.denominator

if __name__ == '__main__':
    fracs = [Fraction(*map(int, raw_input().split())) for _ in range(int(raw_input()))]
    result = product(fracs)
    print(*result)
