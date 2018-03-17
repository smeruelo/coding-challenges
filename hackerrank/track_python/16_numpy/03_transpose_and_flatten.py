#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy

if __name__ == '__main__':
    rows, cols = map(int, raw_input().split())
    lst = [map(int, raw_input().split()) for _ in range(rows)]
    matrix = numpy.array(lst)
    print numpy.transpose(matrix)
    print matrix.flatten()
