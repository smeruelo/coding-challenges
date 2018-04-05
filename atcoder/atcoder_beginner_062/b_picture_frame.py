#!/usr/bin/python3
# https://abc062.contest.atcoder.jp/tasks/abc062_b

def boxify(image, w):
    new = ['#' * (w + 2)]
    for row in image:
        new.append('#' + row + '#')
    new.append('#' * (w + 2))
    return new


if __name__ == '__main__':
    h, w = map(int, input().split())
    image = [input() for _ in range(h)]
    for row in boxify(image, w):
        print(row)
