#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    heights = set(array)
    sum = 0
    for h in heights:
        sum += h
    return sum / len(heights)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print average(arr)
