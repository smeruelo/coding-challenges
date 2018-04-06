#!/usr/bin/python3
# https://abc064.contest.atcoder.jp/tasks/abc064_c

def color(rating):
    d = {'gray': (1, 399), \
         'brown': (400, 799), \
         'green': (800, 1199), \
         'cyan': (1200, 1599), \
         'blue': (1600, 1999), \
         'yellow': (2000, 2399), \
         'orange': (2400, 2799), \
         'red': (2800, 3199), \
         'any': (3200, 4800)}
    for k, v in d.items():
        if rating >= v[0] and rating <= v[1]:
            return k

def count(colors):
    different_colors = set(colors)
    num_colors = len(different_colors) - ('any' in different_colors)
    anys = colors.count('any')
    if num_colors == 0 and anys > 0:
        minimum = 1
    else:
        minimum = num_colors
    maximum = num_colors + anys
    return (minimum, maximum)


if __name__ == '__main__':
    _ = input()
    ratings = map(int, input().split())
    colors = list(map(lambda x: color(x), ratings))
    minimum, maximum = count(colors)
    print(minimum, maximum)
