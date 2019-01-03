#!/usr/bin/python3
# https://adventofcode.com/2018/day/17

from collections import namedtuple
import re

Cell = namedtuple('Cell', 'y x')


def parse_data(data):
    def parse_chunk(chunk):
        axis, v = chunk.split('=')
        if '..' in v:
            begin, end = map(int, v.split('..'))
        else:
            begin = end = int(v)
        return (axis, begin, end)

    clay_coords = []
    for l in data:
        left, right = map(parse_chunk, l.split(', '))
        if left[0] == 'x':
            clay_coords.append((left, right))
        else:
            clay_coords.append((right, left))
    return clay_coords


def init_canvas(clay_coords):
    min_x = min(clay_coords, key=lambda c: c[0][1])[0][1]
    max_x = max(clay_coords, key=lambda c: c[0][2])[0][2]
    min_y = min(clay_coords, key=lambda c: c[1][1])[1][1]
    max_y = max(clay_coords, key=lambda c: c[1][2])[1][2]
    canvas = [['.'] * (max_x - min_x + 3) for _ in range(max_y - min_y + 2)]

    for coord in clay_coords:
        for x in range(coord[0][1] - min_x + 1, coord[0][2] - min_x + 2):
            for y in range(coord[1][1] - min_y + 1, coord[1][2] - min_y + 2):
                canvas[y][x] = '#'
        spring = Cell(0, 500 - min_x + 1)
        canvas[0][spring.x] = '+'
    return (canvas, spring)


def find_wall(row, point, rev=False):
    def rev_index(i):
        return len(row) - i - 1

    try:
        if rev:
            return rev_index(row[::-1].index('#', rev_index(point.x)))
        else:
            return row.index('#', point.x)
    except ValueError:
        return None


def floor(row, left, right):
    for i in range(left, right + 1):
        if row[i] != '#' and row[i] != '~':
            return False
    return True


def fill(canvas, point):
    left = find_wall(canvas[point.y], point, rev=True)
    right = find_wall(canvas[point.y], point)
    if left and right and floor(canvas[point.y+1], left, right):
        for x in range(left + 1, right):
            canvas[point.y][x] = '~'
        return True
    return False


done = set()


def flow(canvas, src):
    if src in done:
        return
    done.add(src)

    def overflow(point, rev=False):
        current = point
        while (
            canvas[current.y][current.x] != '#' and
            (canvas[current.y+1][current.x] == '~' or canvas[current.y+1][current.x] == '#')
        ):
            canvas[current.y][current.x] = '~'
            current = Cell(current.y, current.x - 1) if rev else Cell(current.y, current.x + 1)
        if (rev and canvas[current.y][current.x] != '#') or (not rev and canvas[current.y][current.x] != '#'):
            canvas[current.y][current.x] = '+'
            flow(canvas, current)

    current = Cell(src.y + 1, src.x)
    while current.y < len(canvas) and canvas[current.y][current.x] != '#':
        canvas[current.y][current.x] = '|'
        current = Cell(current.y + 1, current.x)
    if current.y >= len(canvas):
        return
    else:
        current = Cell(current.y - 1, current.x)
        while fill(canvas, current):
            current = Cell(current.y - 1, current.x)

        overflow(current, rev=True)
        overflow(current)


def print_canvas(canvas):
    for line in canvas:
        print(''.join(line))
    print()


def count_water(canvas):
    water = 0
    for row in canvas:
        water += row.count('~')
        water += row.count('|')
    return water


def count_retained_water(canvas):
    # We'll ignore water among spring and wall or among two springs
    regex = re.compile('(\+~+[#\+]|[#\+]~+\+)')
    water = 0
    for row in canvas:
        water += row.count('~')
        for match in re.finditer(regex, ''.join(row)):
            water -= len(match.group(0)) - 2
    return water


if __name__ == '__main__':
    with open('17_reservoir_research.input') as f:
        clay_coords = parse_data(f.readlines())
    canvas, spring = init_canvas(clay_coords)

    flow(canvas, spring)
    print(count_water(canvas))
    print(count_retained_water(canvas))
