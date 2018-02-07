#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        _, set1 = raw_input(), set(raw_input().split())
        _, set2 = raw_input(), set(raw_input().split())
        print set1 <= set2
