#!/usr/bin/python2
# https://abc091.contest.atcoder.jp/tasks/abc091_b

from collections import Counter

def max_earn(blue_cards, red_cards):
    blue_dict = Counter(blue_cards)
    red_dict = Counter(red_cards)
    maximum = 0
    for (k, v) in blue_dict.items():
        if k in red_dict:
            maximum = max(maximum, v - red_dict[k])
        else:
            maximum = max(maximum, v)
    return maximum


if __name__ == '__main__':
    blue_cards = [raw_input() for _ in xrange(int(raw_input()))]
    red_cards = [raw_input() for _ in xrange(int(raw_input()))]
    print max_earn(blue_cards, red_cards)
