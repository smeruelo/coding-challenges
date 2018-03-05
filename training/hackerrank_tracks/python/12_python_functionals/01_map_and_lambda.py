#!/usr/bin/python2
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x ** 3

def fibonacci(n):
    fib = []
    for i in range(n):
        if i == 0 or i == 1:
            fib.append(i)
        else:
            fib.append(fib[i - 1] + fib[i - 2])
    return fib

if __name__ == '__main__':
    print map(cube, fibonacci(int(raw_input())))
