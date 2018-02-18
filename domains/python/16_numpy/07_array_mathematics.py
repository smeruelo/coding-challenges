#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy

if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    a = numpy.array([map(int, raw_input().split()) for _ in range(n)])
    b = numpy.array([map(int, raw_input().split()) for _ in range(n)])
    print a + b
    print a - b
    print a * b
    print a / b
    print a % b
    print a ** b
