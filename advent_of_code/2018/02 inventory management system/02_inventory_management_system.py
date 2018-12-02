#!/usr/bin/python3
# https://adventofcode.com/2018/day/2

from collections import Counter

def checksum(boxes):
    threes = twoes = 0
    for box in boxes:
        d = Counter(box)
        if 3 in d.values():
            threes += 1
        if 2 in d.values():
            twoes += 1
    return threes * twoes

def common(boxes):
    for box1 in boxes:
        for box2 in boxes:
            different = list(map(lambda x, y: int(x != y), list(box1), list(box2)))
            if sum(different) == 1:
                return ''.join(map(lambda x, y: x if not y else '', list(box1), different))


if __name__ == '__main__':
    with open('02_inventory_management_system.input') as f:
        boxes = f.read().split('\n')
    print(checksum(boxes))
    print(common(boxes))
