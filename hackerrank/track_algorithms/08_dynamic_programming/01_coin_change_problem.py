#!/usr/bin/python3
# https://www.hackerrank.com/challenges/coin-change/problem

def ways(n, m, coins):
    count = [[None] * m for i in range(n + 1)]
    for i in range(m):
        count[0][i] = 1
    coins.sort()

    def solve(x, coin):
        if count[x][coin]:
            return count[x][coin]
        else:
            w = 0
            for c in range(m):
                if coins[c] >= coins[coin] and x - coins[c] >= 0:
                    w += solve(x - coins[c], c)
            count[x][coin] = w
            return w

    solve(n, 0)
    return count[-1][0]


if __name__ == '__main__':
    n, m = map(int, input().split())
    coins = list(map(int, input().split()))
    print(ways(n, m, coins))
