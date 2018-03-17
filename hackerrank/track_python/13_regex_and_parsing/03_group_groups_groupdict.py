#!/usr/bin/python2
# https://www.hackerrank.com/challenges/re-group-groups/problem

import re

if __name__ == '__main__':
    match = re.search(r"([0-9a-zA-Z])\1", raw_input())
    print match.group(1) if match else '-1'
