#!/usr/bin/python3
# https://abc077.contest.atcoder.jp/tasks/arc084_a

def altars(n, a, b, c):
    up = sorted(a)
    mid = sorted(b)
    down = sorted(c, reverse=True)
    i = j = 0
    up_count = []
    down_count = []
    for midpart in mid:
        while i < n and up[i] < midpart:
            i += 1
        up_count.append(i)
    for midpart in mid[::-1]:
        while j < n and midpart < down[j]:
            j += 1
        down_count.append(j)
    down_count.reverse()
    return sum(map(lambda x, y: x * y, up_count, down_count))


if __name__ == '__main__':
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())
    c = map(int, input().split())
    print(altars(n, a, b, c))
