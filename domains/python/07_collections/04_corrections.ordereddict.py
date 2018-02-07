#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

if __name__ == '__main__':
    d = OrderedDict()
    for _ in range(int(raw_input())):
        product, _, price = raw_input().rpartition(' ')
        if product in d:
            d[product] += int(price)
        else:
            d[product] = int(price)

    for product, price in d.items():
        print product, price
