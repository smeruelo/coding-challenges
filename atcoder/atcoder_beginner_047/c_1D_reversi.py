#!/usr/bin/python3
# https://abc047.contest.atcoder.jp/tasks/arc063_a

def reversi(s):
    count = 0
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            count += 1
    return count


if __name__ == '__main__':
    s = input()
    print(reversi(s))
