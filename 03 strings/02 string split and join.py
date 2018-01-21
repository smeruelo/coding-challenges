#!/usr/bin/python2
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(s):
    return "-".join(s.split(" "))

if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result
