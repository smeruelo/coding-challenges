#!/usr/bin/python3
# https://abc084.contest.atcoder.jp/tasks/abc084_b

def valid(a, b, s):
    if len(s) == a + b + 1 and s[a] == '-':
        return all(map(lambda c: c in '0123456789', s[:a] + s[a+1:]))
    else:
        return False


if __name__ == '__main__':
    a, b = map(int, input().split())
    s = input()
    print('Yes') if valid(a, b, s) else print('No')
