#!/usr/bin/python2
# https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        try:
            regex = re.compile(raw_input())
            print True
        except Exception as e:
            print False
