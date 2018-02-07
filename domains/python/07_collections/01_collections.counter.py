#!/usr/bin/python2
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    _ = raw_input()
    shoes = Counter(map(int, raw_input().split()))
    earned = 0
    for _ in range(int(raw_input())):
        size, money = map(int, raw_input().split())
        if shoes[size] > 0:
            shoes[size] -= 1
            earned += money
    print earned
