#!/usr/bin/pypy
# https://www.hackerrank.com/contests/womens-codesprint-5/challenges/tsunami

from math import floor, sqrt, ceil

def evacuate(island_id, islands, sorted_islands, blocks, size_blocks, index_by_pos):
    i = index_by_pos[islands[island_id][1]]
    height = sorted_islands[i][2]
    block = i / size_blocks
    if height == -1:
        return 'DROWNED'
    # check if there's a suitable island to evacuate to in current block
    if blocks[block] > height:
        for j in xrange(i+1, min((block+1)*size_blocks, len(sorted_islands))):
            if sorted_islands[j][2] > height:
                return str(sorted_islands[j][1])
    # check other blocks
    b = block + 1
    while b < len(blocks) and height >= blocks[b]:
        b += 1
    if b < len(blocks):
        # suitable block, find the island
        for j in xrange(b*size_blocks, min((b+1)*size_blocks, len(sorted_islands))):
            if sorted_islands[j][2] > height:
                return str(sorted_islands[j][1])
    return 'IMPOSSIBLE'

def drown(position, sorted_islands, blocks, size_blocks, index_by_pos):
    i = index_by_pos[position]
    b = i / size_blocks
    if sorted_islands[i][2] != -1:
        sorted_islands[i][2] = -1
        blocks[b] = max_in_block(sorted_islands, b, size_blocks)
    pass

def read_islands():
    islands = []
    for i in xrange(n):
        position, height = map(int, raw_input().split())
        islands.append([i, position, height])
    return islands

def max_in_block(sorted_islands, block, size_blocks):
    maximum = -1
    for i in xrange(block*size_blocks, min(block*size_blocks + size_blocks, len(sorted_islands))):
        maximum = max(maximum, sorted_islands[i][2])
    return maximum

def blocks_max(sorted_islands, num_blocks, size_blocks):
    blocks = []
    for b in xrange(num_blocks):
        blocks.append(max_in_block(sorted_islands, b, size_blocks))
    return blocks

def index(sorted_islands):
    indexes = {}
    for index, island in enumerate(sorted_islands):
        indexes[island[1]] = index
    return indexes


if __name__ == '__main__':
    n = int(raw_input())
    size_blocks = int(floor(sqrt(n)))
    num_blocks = int(ceil(n / float(size_blocks)))

    islands = read_islands()
    sorted_islands = sorted(islands, key = lambda x: x[1])
    blocks = blocks_max(sorted_islands, num_blocks, size_blocks)
    index_by_pos = index(sorted_islands)

    for _ in xrange(int(raw_input())):
        query_type, arg = raw_input().split()
        if query_type == 'e':
            print evacuate(int(arg)-1, islands, sorted_islands, blocks, size_blocks, index_by_pos)
        else:
            drown(int(arg), sorted_islands, blocks, size_blocks, index_by_pos)
