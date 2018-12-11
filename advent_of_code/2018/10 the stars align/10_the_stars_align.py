#!/usr/bin/python3
# https://adventofcode.com/2018/day/10

def parse_line(line):
    aux1 = line.split('<')
    velocity = tuple(map(int, aux1[2][0:-1].split(',')))
    aux2 = aux1[1].split('>')[0]
    position = tuple(map(int, aux2.split(',')))
    return position, velocity

def print_sky(positions, second):
    min_x = min(positions, key=lambda p: p[0])[0]
    min_y = min(positions, key=lambda p: p[1])[1]
    printable_positions = list(map(lambda p: (p[0] - min_x, p[1] - min_y), positions))
    max_x = max(printable_positions, key=lambda p: p[0])[0]
    max_y = max(printable_positions, key=lambda p: p[1])[1]

    if max_x < 100 and max_y < 15:
        canvas = [['.'] * (max_x + 1) for _ in range(max_y + 1)]
        for x, y in printable_positions:
            canvas[y][x] = '#'
        for row in canvas:
            print(''.join(row))
        print(second)


if __name__ == '__main__':
    with open('10_the_stars_align.input') as f:
        data = f.read().split('\n')

    initial_positions = []
    velocities = []
    for line in data:
        p, v = parse_line(line)
        initial_positions.append(p)
        velocities.append(v)

    positions = initial_positions
    for second in range(1, 20000):
        positions = list(map(lambda p, v: tuple(map(lambda a, b: a + b, p, v)),
                             positions, velocities))
        print_sky(positions, second)
