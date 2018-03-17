#!/usr/bin/python2
# https://abc091.contest.atcoder.jp/tasks/arc092_a
# Maximum bipartite matching

def friendly_pairs(red_points, blue_points):
    def can_be_friends(r, b):
        return r[0] < b[0] and r[1] < b[1]

    red = sorted(red_points, key=lambda x: (x[1], x[0]), reverse=True)
    blue = sorted(blue_points, key=lambda x: (x[0], x[1]))
    count = 0
    for b in blue:
        potential_friends = filter(lambda x: can_be_friends(x, b), red)
        if potential_friends:
            count += 1
            red.remove(potential_friends[0])
    return count


if __name__ == '__main__':
    n = int(raw_input())
    red_points = [map(int, raw_input().split())  for _ in xrange(n)]
    blue_points = [map(int, raw_input().split())  for _ in xrange(n)]
    print friendly_pairs(red_points, blue_points)
