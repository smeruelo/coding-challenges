#!/usr/bin/python3
# https://www.hackerrank.com/challenges/fibonacci-modified/problem

def fibonacci(t0, t1, n):
    fib = [None] * n
    fib[0] = t0
    fib[1] = t1
    for i in range(2, n):
        fib[i] = fib[i-2] + fib[i-1] ** 2
    return fib[-1]


if __name__ == '__main__':
    t0, t1, n = map(int, input().split())
    print(fibonacci(t0, t1, n))
