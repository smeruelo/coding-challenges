#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

if __name__ == '__main__':
    A = set(raw_input().split())
    print all([A > set(raw_input().split()) for _ in range(int(raw_input()))])
