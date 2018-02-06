#!/usr/bin/python2
# https://www.hackerrank.com/challenges/capitalize/problem

def capitalize(s):
    return ' '.join(map(str.capitalize, s.split(' ')))

if __name__ == '__main__':
    print capitalize(raw_input())
