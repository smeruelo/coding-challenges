#!/usr/bin/python3
# https://adventofcode.com/2018/day/13

def parse_data(data):
    canvas = []
    carts = []
    for y in range(len(data)):
        row = []
        for x in range(len(data[y])):
            c = data[y][x]
            if c == '>' or c == '<':
                carts.append((x, y, c, 0))
                c = '-'
            elif c == 'v' or c == '^':
                carts.append((x, y, c, 0))
                c = '|'
            row.append(c)
        canvas.append(row)
    return canvas, carts

def current_map(canvas, carts):
    current = [row[:] for row in canvas]
    for x, y, direction, turn in carts:
        current[y][x] = direction
    return current

TURNS = [{('<', '-'): '<', ('<', '/'): 'v', ('<', '\\'): '^', ('<', '+'): 'v',
          ('>', '-'): '>', ('>', '/'): '^', ('>', '\\'): 'v', ('>', '+'): '^',
          ('v', '|'): 'v', ('v', '/'): '<', ('v', '\\'): '>', ('v', '+'): '>',
          ('^', '|'): '^', ('^', '/'): '>', ('^', '\\'): '<', ('^', '+'): '<'},
         {('<', '-'): '<', ('<', '/'): 'v', ('<', '\\'): '^', ('<', '+'): '<',
          ('>', '-'): '>', ('>', '/'): '^', ('>', '\\'): 'v', ('>', '+'): '>',
          ('v', '|'): 'v', ('v', '/'): '<', ('v', '\\'): '>', ('v', '+'): 'v',
          ('^', '|'): '^', ('^', '/'): '>', ('^', '\\'): '<', ('^', '+'): '^'},
         {('<', '-'): '<', ('<', '/'): 'v', ('<', '\\'): '^', ('<', '+'): '^',
          ('>', '-'): '>', ('>', '/'): '^', ('>', '\\'): 'v', ('>', '+'): 'v',
          ('v', '|'): 'v', ('v', '/'): '<', ('v', '\\'): '>', ('v', '+'): '<',
          ('^', '|'): '^', ('^', '/'): '>', ('^', '\\'): '<', ('^', '+'): '>'},]

def tick_1(canvas, carts):
    new_carts = []
    new_x, new_y, new_direction = None, None, None
    new_map = current_map(canvas, carts)
    sorted_carts = sorted(sorted(carts, key=lambda c: c[0]), key=lambda c: c[1])
    for x, y, direction, turn in sorted_carts:
        new_turn = turn
        new_x = x
        new_y = y
        if direction == '>':
            new_x += 1
        elif direction == '<':
            new_x -= 1
        elif direction == 'v':
            new_y += 1
        else:
            new_y -= 1
        if new_map[new_y][new_x] in '<>^v':
            return None, (new_x, new_y)
        new_direction = TURNS[turn][(direction, canvas[new_y][new_x])]
        new_map[new_y][new_x] = new_direction
        if canvas[new_y][new_x] == '+':
            new_turn = (turn + 1) % 3
        new_carts.append((new_x, new_y, new_direction, new_turn))
    return new_carts, None

def tick_2(canvas, carts):
    def remove_cart(position, lst):
        def aux(i, new_lst):
            if i < len(lst):
                x, y, direction, turn = lst[i]
                if position[0] == x and position[1] == y:
                    return new_lst + lst[i+1:]
                else:
                    return aux(i + 1, new_lst + [lst[i]])
            return new_lst
        return aux(0, [])

    new_carts = []
    removed = []
    new_x, new_y, new_direction = None, None, None
    new_map = current_map(canvas, carts)
    sorted_carts = sorted(sorted(carts, key=lambda c: c[0]), key=lambda c: c[1])
    for x, y, direction, turn in sorted_carts:
        new_turn = turn
        new_x = x
        new_y = y
        if (new_x, new_y) not in removed:
            if direction == '>':
                new_x += 1
            elif direction == '<':
                new_x -= 1
            elif direction == 'v':
                new_y += 1
            else:
                new_y -= 1
            if new_map[new_y][new_x] in '<>^v':
                new_carts = remove_cart((new_x, new_y), new_carts)
                removed.append((new_x, new_y))
            else:
                new_direction = TURNS[turn][(direction, canvas[new_y][new_x])]
                new_map[new_y][new_x] = new_direction
                if canvas[new_y][new_x] == '+':
                    new_turn = (turn + 1) % 3
                new_carts.append((new_x, new_y, new_direction, new_turn))
    return new_carts


if __name__ == '__main__':
    with open('13_mine_cart_madness.input') as f:
        data = list(f.read().split('\n'))
    canvas, initial_carts = parse_data(data)

    # part 1
    carts, collision = tick_1(canvas, initial_carts)
    while collision == None:
        current = current_map(canvas, carts)
        carts, collision = tick_1(canvas, carts)
    print('{},{}'.format(collision[0], collision[1]))

    # part 2
    carts = initial_carts
    while len(carts) > 1:
        current = current_map(canvas, carts)
        carts = tick_2(canvas, carts)
    print('{},{}'.format(carts[0][0], carts[0][1]))
