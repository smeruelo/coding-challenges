#!/usr/bin/python2
# https://www.hackerrank.com/challenges/python-quest-1/problem

if __name__ == '__main__':
    for i in range(1, input()):
        print i * reduce(lambda x, y: x * 10 + y, [1] * i)
