#!/usr/bin/pypy3
# https://www.codechef.com/WICP2001/problems/CHEFSUM


def chef_min(a, n):
    s = sum(a)
    prefix = 0
    suffix = s
    prev = 0
    min_so_far = 2 * s
    index_min = 1
    for i in range(n):
        prefix += a[i]
        suffix -= prev
        total = prefix + suffix
        if total < min_so_far:
            min_so_far = total
            index_min = i + 1
        prev = a[i]
    return index_min


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        print(chef_min(a, n))
