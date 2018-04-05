#!/usr/bin/python3
# https://abc062.contest.atcoder.jp/tasks/abc062_a

def same(x, y):
    for g in [[1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2]]:
        if x in g and y in g:
            return 'Yes'
    return 'No'


if __name__ == '__main__':
    x, y = map(int, input().split())
    print(same(x, y))
