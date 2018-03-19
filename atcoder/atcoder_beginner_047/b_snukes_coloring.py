#!/usr/bin/python3
# https://abc047.contest.atcoder.jp/tasks/abc047_b

def area(x2, y2, points):
    x1 = y1 = 0
    for x, y, a in points:
        if a == 1:
            x1 = min(max(x1, x), x2)
        elif a == 2:
            x2 = max(min(x2, x), x1)
        elif a == 3:
            y1 = min(max(y1, y), y2)
        else:
            y2 = max(min(y2, y), y1)
    return (x2 - x1) * (y2 - y1)


if __name__ == '__main__':
    w, h, n = list(map(int, input().split()))
    points = [list(map(int, input().split())) for _ in range(n)]
    print(area(w, h, points))
