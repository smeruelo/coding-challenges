#!/usr/bin/python2
# https://www.hackerrank.com/challenges/write-a-function/problem

def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == '__main__':
    n = int(raw_input())
    print leap(n)
