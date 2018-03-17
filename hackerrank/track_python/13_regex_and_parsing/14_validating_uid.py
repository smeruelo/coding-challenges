#!/usr/bin/python2
# https://www.hackerrank.com/challenges/validating-uid/problem

import re

def validate(uid):
    r1 = re.compile(r'^[a-zA-Z0-9]{10}$')  # 10 alphanumeric chars
    r2 = re.compile(r'(.*[A-Z]){2,}')      # At least 2 uppercase letters
    r3 = re.compile(r'(.*[0-9]){3,}')      # At least 3 digits
    r4 = re.compile(r'.*(.).*\1')          # Duplicated chars
    return bool(re.match(r1, uid)) and \
        bool(re.match(r2, uid)) and \
        bool(re.match(r3, uid)) and \
        not (bool(re.match(r4, uid)))

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print 'Valid' if validate(raw_input()) else 'Invalid'
