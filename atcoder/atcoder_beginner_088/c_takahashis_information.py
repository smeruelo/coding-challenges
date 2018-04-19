#!/usr/bin/python3
# https://abc088.contest.atcoder.jp/tasks/abc088_c

def six_integers(c):
    return c[0][1] - c[0][0] == c[1][1] - c[1][0] == c[2][1] - c[2][0] and \
        c[0][2] - c[0][1] == c[1][2] - c[1][1] == c[2][2] - c[2][1] and \
        c[0][2] - c[0][0] == c[1][2] - c[1][0] == c[2][2] - c[2][0] and \
        c[1][0] - c[0][0] == c[1][1] - c[0][1] == c[1][2] - c[0][2] and \
        c[2][0] - c[1][0] == c[2][1] - c[1][1] == c[2][2] - c[1][2] and \
        c[2][0] - c[0][0] == c[2][1] - c[0][1] == c[2][2] - c[0][2]


if __name__ == '__main__':
    c = [list(map(int, input().split())) for _ in range(3)]
    print('Yes') if six_integers(c) else print('No')
