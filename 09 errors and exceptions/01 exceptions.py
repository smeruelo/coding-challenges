#!/usr/bin/python2
# https://www.hackerrank.com/challenges/exceptions/problem

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        try:
            arg1, arg2 = map(int, raw_input().split())
            print arg1 / arg2
        except Exception as e:
            print 'Error Code: {}'.format(e)
