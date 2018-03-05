#!/usr/bin/python2
# https://www.hackerrank.com/challenges/array-left-rotation/problem

def left_rotation(a, d):
    if d != len(a):
        for _ in range(d):
            a.append(a.pop(0))

if __name__ == '__main__':
    _, d = map(int, raw_input().split())
    a = map(int, raw_input().split())
    left_rotation(a, d)
    print ' '.join(map(str, a))
