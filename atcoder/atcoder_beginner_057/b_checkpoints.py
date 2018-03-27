#!/usr/bin/python3
# https://abc057.contest.atcoder.jp/tasks/abc057_b

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def nearest(x, y, checkpoints):
    distances = list(map(lambda c: distance(x, y, c[0], c[1]), checkpoints))
    return 1 + distances.index(min(distances))


if __name__ == '__main__':
    n, m = map(int, input().split())
    students = [list(map(int, input().split())) for _ in range(n)]
    checkpoints = [list(map(int, input().split())) for _ in range(m)]
    for x, y in students:
        print(nearest(x, y, checkpoints))
