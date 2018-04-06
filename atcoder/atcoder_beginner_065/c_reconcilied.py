#!/usr/bin/python3
# https://abc065.contest.atcoder.jp/tasks/arc076_a

def factorial(n):
    fact = 1
    for i in range(n, 0, -1):
        fact = (fact * i) % (10 ** 9 + 7)
    return fact

def arrangements(n, m):
    if abs(n - m) == 1:
        return (factorial(n) * factorial(m)) % (10 ** 9 + 7)
    elif n == m:
        return (factorial(n) * factorial(m) * 2) % (10 ** 9 + 7)
    else:
        return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(arrangements(n, m) % (10 ** 9 + 7))
