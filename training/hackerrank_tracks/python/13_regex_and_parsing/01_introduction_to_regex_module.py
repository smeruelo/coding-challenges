#!/usr/bin/python3
# https://www.hackerrank.com/challenges/introduction-to-regex/problem

# It doesn't work in python2 !!

import re

def valid_float(s):
    return bool(re.match(r"[+-]?\d*\.\d+$", s))

if __name__ == '__main__':
    for _ in range(int(input())):
        print(valid_float(input()))
