#!/usr/bin/python2
# https://www.hackerrank.com/challenges/2d-array/problem

def max_hourglass(a):
    def hourglass(i, j):
        return a[i][j] + a[i][j+1] + a[i][j+2] + a[i+1][j+1] + a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]

    maximum = -100
    for i in range(4):
        for j in range(4):
            current = hourglass(i, j)
            maximum = max(maximum, current)
    return maximum


if __name__ == '__main__':
    a = [map(int, raw_input().split()) for i in range(6)]
    print max_hourglass(a)
