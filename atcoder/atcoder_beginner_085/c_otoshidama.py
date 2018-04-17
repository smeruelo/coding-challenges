#!/usr/bin/python3
# https://abc085.contest.atcoder.jp/tasks/abc085_c

def bills(n, y):
    for bills_10k in range(n + 1):
        for bills_5k in range(n - bills_10k + 1):
            bills_1k = n - bills_10k - bills_5k
            if y == bills_10k * 10000 + bills_5k * 5000 + bills_1k * 1000:
                return [bills_10k, bills_5k, bills_1k]
    return [-1, -1, -1]


if __name__ == '__main__':
    n, y = map(int, input().split())
    print(' '.join(map(str, bills(n, y))))
