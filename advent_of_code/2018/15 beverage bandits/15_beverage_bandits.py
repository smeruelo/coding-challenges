#!/usr/bin/python3
# https://adventofcode.com/2018/day/15

from collections import namedtuple

Cell = namedtuple('Cell', 'y x')
Unit = namedtuple('Unit', 'points type')

def parse_data(data):
    board = []
    units = dict()
    for y in range(len(data)):
        board.append(list(data[y]))
        for x in range(len(board[0])):
            if board[y][x] == 'E':
                units[Cell(y, x)] = Unit(200, 'E')
            elif board[y][x] == 'G':
                units[Cell(y, x)] = Unit(200, 'G')
    return board, units

# def print_board(board, units):
#     for row in board:
#         print(''.join(row))
#     print('units:')
#     for cell, unit in sorted(units.items()):
#         print('({},{}): {}, {}'.format(cell.y, cell.x, unit.points, unit.type))

def adjacent(cell, board):
    adj = [Cell(cell.y - 1, cell.x),
           Cell(cell.y + 1, cell.x),
           Cell(cell.y, cell.x - 1),
           Cell(cell.y, cell.x + 1)]
    return filter(lambda c: board[c.y][c.x] != '#', adj)

def turn(cell, board, units, elves_power):
    cell_type = units[cell].type
    enemy_units = list(filter(lambda u: u.type != cell_type, units.values()))
    
    def attackable_cells(current):
        return sorted(filter(lambda x: x in units and units[x].type != cell_type,
                             sorted(adjacent(current, board))),
                      key=lambda x: units[x].points)

    def attack(target):
        current_unit = units[target]
        if current_unit.type == 'G':
            power = elves_power
        else:
            power = 3
        new_unit = Unit(current_unit.points - power, current_unit.type)
        if new_unit.points > 0:
            units[target] = new_unit
        else:
            del units[target]
            board[target.y][target.x] = '.'

    def search_path(init_cell):
        to_visit = [(init_cell, [init_cell])]
        discovered = set()
        discovered.add(init_cell)
        equal_len_targets = []
        previous_len = 1
        while to_visit:
            to_visit.sort(key=lambda x: (len(x[1]), x[1]))
            current, path = to_visit.pop(0)
            current_len = len(path)
            if equal_len_targets and current_len != previous_len:
                return sorted(equal_len_targets)[0][1][1]
            if current == init_cell or board[current.y][current.x] == '.':
                if attackable_cells(current):
                    equal_len_targets.append((current, path))
                    previous_len = current_len
                adj = adjacent(current, board)
                for a in adj:
                    if a not in discovered and board[a.y][a.x] != cell_type:
                        to_visit.append((a, path + [a]))
                        discovered.add(a)
        if equal_len_targets:
            return sorted(equal_len_targets)[0][1][1]
        else:
            return None
        
    def move(target):
        u = units[cell]
        b = board[cell.y][cell.x]
        del units[cell]
        board[cell.y][cell.x] = '.'
        units[target] = u
        board[target.y][target.x] = b

    if enemy_units:
        attack_target = attackable_cells(cell)
        if attack_target:
            attack(attack_target[0])
        else:
            move_target = search_path(cell)
            if move_target:
                move(move_target)
                attack_target = attackable_cells(move_target)
                if attack_target:
                    attack(attack_target[0])
        return True
    else:
        return False

def fight(board, units, elves_power = 3):
    rounds = 0
    while True:
        for cell in sorted(units.keys()):
            if cell in units:
                if not turn(cell, board, units, elves_power):
                    return rounds
        rounds += 1    

def count_elves(units):
    return len(list(filter(lambda u: u.type == 'E', units.values())))

def elves_win(num_elves, units):
    return len(list(filter(lambda u: u.type == 'E', units.values()))) == num_elves


if __name__ == '__main__':
    with open('15_beverage_bandits.input') as f:
        data = f.read().split('\n')

    # Part 1
    board, units = parse_data(data)
    rounds = fight(board, units)
    print(sum(map(lambda u: u.points, units.values())) * rounds)

    # Part 2
    losing = True
    power = 4
    while losing:
        board, units = parse_data(data)
        num_elves = count_elves(units)
        rounds = fight(board, units, power)
        if elves_win(num_elves, units):
            losing = False
        else:
            power += 1
    print(sum(map(lambda u: u.points, units.values())) * rounds)
