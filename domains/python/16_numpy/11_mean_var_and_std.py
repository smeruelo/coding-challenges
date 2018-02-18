#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem

import numpy

if __name__ == '__main__':
    n, _ = map(int, raw_input().split())
    arr = numpy.array([map(int, raw_input().split()) for _ in range(n)])
    print numpy.mean(arr, axis = 1)
    print numpy.var(arr, axis = 0)
    print numpy.std(arr)
