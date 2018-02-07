#!/usr/bin/python2
# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    print wrap(string, max_width)
