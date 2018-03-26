#!/usr/bin/python3
# https://abc055.contest.atcoder.jp/tasks/abc055_b

def factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact = (fact * i) % (10 ** 9 + 7)
    return fact


if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
