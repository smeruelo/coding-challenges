#!/usr/bin/python3
# https://abc103.contest.atcoder.jp/tasks/abc103_b

def equals(s, t):
    for i in range(len(s)):
        rotated = s[-i:] + s[0:-i]
        if rotated == t:
            return True
    return False


if __name__ == '__main__':
    s = input()
    t = input()
    print('Yes') if equals(s, t) else print('No')
