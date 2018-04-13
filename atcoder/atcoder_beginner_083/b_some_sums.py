#!/usr/bin/python3
# https://abc083.contest.atcoder.jp/tasks/abc083_b

def sum_among_boundaries(i, a, b):
    digits_sum = sum(map(int, str(i)))
    return digits_sum >= a and digits_sum <= b

if __name__ == '__main__':
    n, a, b = map(int, input().split())
    print(sum([i for i in range(1, n + 1) if sum_among_boundaries(i, a, b)]))
