#!/usr/bin/python2
# https://www.hackerrank.com/challenges/arrays-ds/problem

if __name__ == '__main__':
    n = int(raw_input())
    l = raw_input().split()
    print ' '.join([l[i] for i in xrange(n - 1, -1, -1)])
