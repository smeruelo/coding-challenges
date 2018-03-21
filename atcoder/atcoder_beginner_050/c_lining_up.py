#!/usr/bin/python3
# https://abc050.contest.atcoder.jp/tasks/arc066_a

from collections import Counter

def orders(count, n):
    c = 1
    for k, v in count.items():
        if k == 0:
            if (n % 2 == 0 or v != 1):
                return 0
        elif (n - 1 - k) % 2 == 1 or v != 2:
            return 0
        else:
            c *= v
    return(c % (10 ** 9 + 7))


if __name__ == '__main__':
    n = int(input())
    count = Counter(map(int, input().split()))
    print(orders(count, n))
