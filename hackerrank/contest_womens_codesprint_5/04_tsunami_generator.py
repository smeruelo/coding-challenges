#!/usr/bin/python2
# https://www.hackerrank.com/contests/womens-codesprint-5/challenges/tsunami

import random

MAX_HEIGHT = 11 * 10**8
MAX_POSITION = 10**9
NUM_ISLANDS = 2 * 10**5
NUM_QUERIES = 2 * 10**5

positions = set()
print NUM_ISLANDS
for island in xrange(NUM_ISLANDS):
    pos = random.randint(0, MAX_POSITION)
    while pos in positions:
        pos = random.randint(0, MAX_POSITION)
    positions.add(pos)
    print pos, random.randint(0, MAX_HEIGHT)

positions = list(positions)
print NUM_QUERIES
for query in xrange(NUM_QUERIES):
    if random.randint(0, 1):
        query_type = 'e'
        island = random.randint(1, NUM_ISLANDS)
    else:
        query_type = 'd'
        island = positions[random.randint(0, len(positions))]
    print query_type, island
