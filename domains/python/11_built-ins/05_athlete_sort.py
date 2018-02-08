#!/usr/bin/python2
# https://www.hackerrank.com/challenges/python-sort-sort/problem

def order(details, k):
    return sorted(details, key = lambda x: x[k])

if __name__ == '__main__':
    num_athletes, num_attributes = map(int, raw_input().split())
    details = [map(int, raw_input().split()) for i in range(num_athletes)]
    k = int(raw_input())
    print '\n'.join([' '.join(map(str, i)) for i in order(details, k)])
