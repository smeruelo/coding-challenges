#!/usr/bin/python3
# https://abc077.contest.atcoder.jp/tasks/abc077_a

def rotate(grid):
    return list(map(lambda x: x[::-1], grid))[::-1]


if __name__ == '__main__':
    grid = [input(), input()]
    print('YES') if grid == rotate(grid) else print('NO')
