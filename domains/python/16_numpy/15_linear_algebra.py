#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-linear-algebra/problem

import numpy

if __name__ == '__main__':
    n = int(raw_input())
    arr = numpy.array([map(float, raw_input().split()) for _ in range(n)])
    print numpy.linalg.det(arr)
