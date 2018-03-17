#!/usr/bin/python2
# https://www.hackerrank.com/challenges/validating-postalcode/problem

import re

code = raw_input()
r1 = re.compile(r'^[1-9][0-9]{5}$')  # 100000 <= code <= 999999
r2 = re.compile(r'(?=(.).\1)')       # alternate repetition

print bool(re.match(r1, code)) and len(re.findall(r2, code)) <= 1
