#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-if-else/problem

if __name__ == '__main__':
    n = int(raw_input())
    if  n % 2 == 1 or n in range(6, 21):
        print "Weird"
    else:
        print "Not Weird"
