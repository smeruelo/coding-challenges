#!/usr/bin/env python
# https://www.codechef.com/WICP2002/problems/WICP003

def accum(a):
    s = a[:]
    for i in range(len(s)-2, -1, -1):
        s[i] += s[i+1]
    return s

def find_values(a, n, th):
    acc = accum(a)

    def s(a, m):
        return sum(map(lambda x: max(x - m, 0), a))

    def m(k):
        min_m = 0 if k == 0 else a[k-1]
        max_m = (acc[k] - th) // (n - k)
        return max_m if max_m >= min_m else None

    def max_m():
        max_so_far = 0
        for i in range(len(acc)-1, -1, -1):
            mi = m(i)
            if mi is None:
                continue
            if mi > max_so_far:
                max_so_far = mi
            if mi < max_so_far:
                return max_so_far
        return max_so_far

    maxm = max_m()
    return maxm, s(a, maxm)


for _ in range(int(input())):
    n, th = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    m, s = find_values(a, n, th)
    print(m, s)
