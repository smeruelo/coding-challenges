#!/usr/bin/python2
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = raw_input()
    print any(map(str.isalnum, list(s)))
    print any(map(str.isalpha, list(s)))
    print any(map(str.isdigit, list(s)))
    print any(map(str.islower, list(s)))
    print any(map(str.isupper, list(s)))

