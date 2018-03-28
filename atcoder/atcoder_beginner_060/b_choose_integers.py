#!/usr/bin/python3
# https://abc060.contest.atcoder.jp/tasks/abc060_b
# Laaksonen 21.2

# (k A) mod B = C mod B
# ((k mod B) (A mod B)) mod B = C mod B
#   -------
#     B possible values

def exists(a, b, c):
    for i in range(b):
        if (i * (a % b)) % b == c % b:
            return True
    return False


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print('YES') if exists(a, b, c) else print('NO')

