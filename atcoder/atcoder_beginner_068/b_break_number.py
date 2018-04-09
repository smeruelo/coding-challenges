#!/usr/bin/python3
# https://abc068.contest.atcoder.jp/tasks/abc068_b

def count_div(n):
    c = 0
    while n % 2 == 0 and n > 1:
        c += 1
        n = n / 2
    return c


if __name__ == '__main__':
    maximum = (0, 0)
    for i in range(int(input()), 0, -1):
        current = count_div(i)
        if current >= maximum[0]:
            maximum = (current, i)
    print(maximum[1])
