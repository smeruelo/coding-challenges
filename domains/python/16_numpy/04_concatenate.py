#!/usr/bin/python2
# https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy

if __name__ == '__main__':
    rows1, rows2, _ = map(int, raw_input().split())
    array1 = [map(int, raw_input().split()) for _ in range(rows1)]
    array2 = [map(int, raw_input().split()) for _ in range(rows2)]
    print numpy.concatenate((array1, array2), axis = 0)
