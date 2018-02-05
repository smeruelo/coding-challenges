#!/usr/bin/python2
# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

if __name__ == '__main__':
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())
    print ' '.join(map(str, product(a, b)))
