#!/usr/bin/python2
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

def is_valid(s):
    return bool(re.match(r'[789]\d{9}$', s))

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print 'YES' if is_valid(raw_input()) else 'NO'
