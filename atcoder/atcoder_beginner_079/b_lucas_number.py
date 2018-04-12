#!/usr/bin/python3
# https://abc079.contest.atcoder.jp/tasks/abc079_b

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    prev_prev = 2
    prev = 1
    for i in range(2, n+1):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    return current


if __name__ == '__main__':
    print(lucas(int(input())))
