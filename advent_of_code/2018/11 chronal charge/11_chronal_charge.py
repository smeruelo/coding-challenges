#!/usr/bin/pypy3
# https://adventofcode.com/2018/day/11

def fuel(sn):
    def power(x, y):
        rack_id = x + 10
        aux = ((rack_id * y) + sn) * rack_id
        if aux < 100:
            return -5
        else:
            return int(str(aux)[-3]) - 5

    cells = [[0] * 301 for _ in range(301)]
    for y in range(1, 301):
        for x in range(1, 301):
            cells[y][x] = power(x, y)
    return cells

def largest(cells, size):
    def power_square(col, row, size):
        total = 0
        for row in range(row, row + size):
            total += sum(cells[row][col:col+size])
        return total

    max_power = 0
    max_top_left = (0, 0)
    for row in range(1, 301 - size + 1):
        for col in range(1, 301 - size + 1):
            power = power_square(col, row, size)
            if power > max_power:
                max_power = power
                max_top_left = (col, row)
    return (max_top_left, max_power)


if __name__ == '__main__':
    with open('11_chronal_charge.input') as f:
        sn = int(f.read())
    cells = fuel(sn)

    # part 1
    top_left, power = largest(cells, 3)
    print('{},{}'.format(top_left[0], top_left[1]))

    # part 2
    max_power = 0
    max_top_left = (0, 0)
    max_size = 0
    for size in range(1, 301):
        top_left, power = largest(cells, size)
        if power > max_power:
            max_power = power
            max_top_left = top_left
            max_size = size
    print('{},{},{}'.format(max_top_left[0], max_top_left[1], max_size))
