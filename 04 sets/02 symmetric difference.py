#!/usr/bin/python2
# https://www.hackerrank.com/challenges/symmetric-difference/problem

def symmetric_difference(a, b):
    # return a.difference(b).union(b.difference(a))
    return a ^ b

if __name__ == '__main__':
    _ = raw_input()
    a = set(map(int, raw_input().split()))
    _ = raw_input()
    b = set(map(int, raw_input().split()))
    for i in sorted(symmetric_difference(a, b)):
        print i
