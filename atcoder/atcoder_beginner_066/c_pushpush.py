#!/usr/bin/python3
# https://abc066.contest.atcoder.jp/tasks/arc077_a

def unzip(n, a):
    even_pos = [elem for i, elem in enumerate(a) if i % 2 == 0]
    odd_pos = [elem for i, elem in enumerate(a) if i % 2 == 1]
    if n % 2 == 0:
        return odd_pos[::-1] + even_pos
    else:
        return even_pos[::-1] + odd_pos


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, (input().split())))
    print(' '.join(map(str, unzip(n, a))))
