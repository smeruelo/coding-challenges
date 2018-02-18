#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-dot-and-cross/problem

import numpy

if __name__ == '__main__':
    n = int(raw_input())
    a = numpy.array([map(int, raw_input().split()) for _ in range(n)])
    b = numpy.array([map(int, raw_input().split()) for _ in range(n)])
    print numpy.dot(a, b)
