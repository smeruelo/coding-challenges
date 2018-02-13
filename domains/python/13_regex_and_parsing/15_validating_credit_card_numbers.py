#!/usr/bin/python2
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re

def validate(card):
    r1 = re.compile(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$')  # Optional but consistent hyphen, start with 456
    r2 = re.compile(r'.*(.)\1{3,}')                          # 4 consecutive repeated chars
    return bool(re.match(r1, card)) and \
        not bool(re.match(r2, re.sub(r'-', lambda x: '', card)))


if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print 'Valid' if validate(raw_input()) else 'Invalid'
