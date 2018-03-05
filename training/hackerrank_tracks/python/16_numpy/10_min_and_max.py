#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy

if __name__ == '__main__':
    n, _ = map(int, raw_input().split())
    arr = numpy.array([map(int, raw_input().split()) for _ in range(n)])
    print numpy.max(numpy.min(arr, axis = 1))
