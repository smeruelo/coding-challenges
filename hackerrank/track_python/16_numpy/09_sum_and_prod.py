#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy

if __name__ == '__main__':
    n, _ = map(int, raw_input().split())
    arr = numpy.array([map(int, raw_input().split()) for _ in range(n)])
    print numpy.prod(numpy.sum(arr, axis = 0))
