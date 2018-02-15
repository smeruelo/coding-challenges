#!/usr/bin/python2
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

import re

def wrapper(f):
    def fun(l):
        return f(map(lambda s: re.sub(r'^(\+91|91|0)?(\d{5})(\d{5})$', r'+91 \2 \3', s), l))
    return fun

@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    l = [raw_input() for _ in range(int(input()))]
    sort_phone(l)
