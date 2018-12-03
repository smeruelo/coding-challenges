#!/usr/bin/python3
# https://adventofcode.com/2018/day/3

def claim(line):
    data = line.split()
    claim_id = data[0][1:]
    col_begin, row_begin = map(int, data[2][:-1].split(','))
    col_offset, row_offset = map(int, data[3].split('x'))
    return (claim_id, [col_begin, col_begin + col_offset, row_begin, row_begin + row_offset])

def mark_claim(fabric, rectangle):
    col_begin, col_end, row_begin, row_end = rectangle
    for row in range(row_begin, row_end):
        for col in range(col_begin, col_end):
            fabric[row][col] += 1

def count_overlaps(fabric):
    overlaps = 0
    for row in fabric:
        overlaps += sum(map(lambda x: x > 1, row))
    return overlaps

def overlap(fabric, rectangle):
    col_begin, col_end, row_begin, row_end = rectangle
    for row in range(row_begin, row_end):
        for col in range(col_begin, col_end):
            if fabric[row][col] != 1:
                return True
    return False


if __name__ == '__main__':
    fabric = [[0] * 1000 for _ in range(1000)]
    with open('03_no_matter_how_you_slice_it.input') as f:
        data = f.read().split('\n')

    # part 1
    for line in data:
        _, rectangle = claim(line)
        mark_claim(fabric, rectangle)
    print(count_overlaps(fabric))

    # part 2
    for line in data:
        claim_id, rectangle = claim(line)
        if not overlap(fabric, rectangle):
            print(claim_id)
            break
