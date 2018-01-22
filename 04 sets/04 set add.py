#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    stamps = set()
    for _ in range(int(raw_input())):
        stamps.add(raw_input())
    print len(stamps)
