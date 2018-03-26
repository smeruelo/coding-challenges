#!/usr/bin/python3
# https://abc054.contest.atcoder.jp/tasks/abc054_b

def contains(a, b, n, m):
    def eq(i, j):
        for row in range(m):
            if b[row] != a[i + row][j:j+m]:
                return False
        return True

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if eq(i, j):
                return True
    return False


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    a = [list(input()) for _ in range(n)]
    b = [list(input()) for _ in range(m)]
    print('Yes') if contains(a, b, n, m) else print('No')
