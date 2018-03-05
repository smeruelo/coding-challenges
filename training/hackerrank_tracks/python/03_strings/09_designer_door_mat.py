#!/usr/bin/python2
# https://www.hackerrank.com/challenges/designer-door-mat/problem

if __name__ == '__main__':
    N, M = map(int,raw_input().split())

    for i in xrange(1, N, 2):
        print '-' * ((M - len('.|.') * i) / 2)  + '.|.' * i + '-' * ((M - len('.|.') * i) / 2)
    print '-' * ((M - len('WELCOME')) / 2) + 'WELCOME' + '-' * ((M - len('WELCOME')) / 2)
    for i in xrange(N-2, -1, -2):
        print '-' * ((M - len('.|.') * i) / 2)  + '.|.' * i + '-' * ((M - len('.|.') * i) / 2)
