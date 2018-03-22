#!/usr/bin/python3
# https://abc052.contest.atcoder.jp/tasks/arc067_a
# Laaksonen 21.1

from collections import Counter

def factors(num):
    f = []
    n = num
    i = 2
    while i * i <= n:
        while n % i == 0:
            f.append(i)
            n //= i
        i += 1
    if n > 1:
        f.append(n)
    return f


if __name__ == '__main__':
    n = int(input())
    d = Counter()
    for i in range(2, n+1):
        d.update(factors(i))
    result = 1
    for k, v in d.items():
        result = (result * (v + 1)) % (10 ** 9 + 7)
    print(result)
