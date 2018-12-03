#!/usr/bin/python3

import math
import os
import random
import re
import sys

def verificaArticulos(origItems, origPrices, items, prices):
    catalog = dict()
    for item, price in zip(origItems, origPrices):
        catalog[item] = price

    count = 0
    for item, price in zip(items, prices):
        if price != catalog[item]:
            count += 1
    return count


if __name__ == '__main__':
    fptr = sys.stdout

    origItems_count = int(input())

    origItems = []

    for _ in range(origItems_count):
        origItems_item = input()
        origItems.append(origItems_item)

    origPrices_count = int(input())

    origPrices = []

    for _ in range(origPrices_count):
        origPrices_item = float(input())
        origPrices.append(origPrices_item)

    items_count = int(input())

    items = []

    for _ in range(items_count):
        items_item = input()
        items.append(items_item)

    prices_count = int(input())

    prices = []

    for _ in range(prices_count):
        prices_item = float(input())
        prices.append(prices_item)

    res = verificaArticulos(origItems, origPrices, items, prices)

    fptr.write(str(res) + '\n')

    fptr.close()
