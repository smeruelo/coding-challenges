#!/usr/bin/pypy3

from collections import defaultdict

def dance(n, grudges):
    g = defaultdict(set)
    for p1, p2 in grudges:
        g[p1].add(p2)
        g[p2].add(p1)
    memo = [[None] * n for _ in range(n)]

    def reachable(p, end):
        oddity = p % 2
        return set([i for i in range(p+1, end+1) if i % 2 != oddity]).difference(g[p])

    def aux(start, end):
        size = end - start + 1
        if size % 2 != 0:
            return 0
        if memo[start][end]:
            return memo[start][end]

        count = 0
        for p in reachable(start, end):
            inner = outter = 1
            if p - start > 1:
                inner =  aux(start + 1, p - 1) % (10 ** 9 + 7)
            if p < end:
                outter = aux(p + 1, end) % (10 ** 9 + 7)
            count += (inner * outter) % (10 ** 9 + 7)
        memo[start][end] = count % (10 ** 9 + 7)
        return memo[start][end]

    return aux(0, n - 1)


if __name__ == '__main__':
    for i in range(int(input())):
        p, g = map(int, input().split())
        grudges = [list(map(int, input().split())) for _ in range(g)]
        print('Case #{}: {}'.format(i + 1, dance(p, grudges)))
