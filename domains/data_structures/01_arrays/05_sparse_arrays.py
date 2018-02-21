#!/usr/bin/python2
# https://www.hackerrank.com/challenges/sparse-arrays/problem

def count(query, strings):
    c = 0
    for s in strings:
        if query == s:
            c += 1
    return c


if __name__ == '__main__':
    strings = [raw_input() for _ in range(int(raw_input()))]
    for _ in range(int(raw_input())):
        query = raw_input()
        print count(query, strings)
