#!/usr/bin/python3

import socket
from random import choice

U2L1 = (-2, -1)
U2R1 = (-2, 1)
U1L2 = (-1, -2)
U1R2 = (-1, 2)
D1L2 = (1, -2)
D1R2 = (1, 2)
D2L1 = (2, -1)
D2R1 = (2, 1)
COMMANDS = {U2L1: '2u1l', U2R1: '2u1r', U1L2: '1u2l', U1R2: '1u2r', D1L2: '1d2l', D1R2: '1d2r', D2L1: '2d1l', D2R1: '2d1r'}
JUMPS = {'2u1l': U2L1, '2u1r': U2R1, '1u2l': U1L2, '1u2r': U1R2, '1d2l': D1L2, '1d2r': D1R2, '2d1l': D2L1, '2d1r': D2R1}
SIZE = 115
LABYRINTH = [[' ']*(SIZE*2+1) for _ in range(SIZE*2+1)]
VISITED = [[False]*(SIZE*2+1) for _ in range(SIZE*2+1)]

def update_labyrinth(cell, view):
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            y = cell[0] + dy
            x = cell[1] + dx
            LABYRINTH[y][x] = view[2+dy][2+dx]
    LABYRINTH[cell[0]][cell[1]] = '.'

def print_labyrinth():
    for i, row in enumerate(LABYRINTH):
        print(i, 'i' + ''.join(row) + 'f')

def read_view(f):
    view = [f.readline()[:-1] for _ in range(5)]
    f.readline()
    return view

def write_move(f, move):
    f.write(f'{move}\n'); f.flush()

def reachable_view_cells(view):
    return list(filter(lambda j: view[2+j[0]][2+j[1]] != '#', JUMPS.values()))

def unvisited(cell):
    return not VISITED[cell[0]][cell[1]]

def visit(cell):
    VISITED[cell[0]][cell[1]] = True

def cell_plus_delta(cell, delta):
    return (cell[0]+delta[0], cell[1]+delta[1])

def dfs(f, previous, delta):
    current = cell_plus_delta(previous, delta)
    visit(current)
    if current == (115, 116):
        print(f.readline())
        print_labyrinth()
        return True

    view = read_view(f)
    update_labyrinth(current, view)
    for d in reachable_view_cells(view):
        if unvisited(cell_plus_delta(current, d)):
            write_move(f, COMMANDS[d])
            if dfs(f, current, d):
                return True
    rev_delta = tuple(map(lambda x: -1*x, delta))
    write_move(f, COMMANDS[rev_delta])
    view = read_view(f)
    return False


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('52.49.91.111', 2003))
    f = s.makefile(mode='rw')

    dfs(f, (SIZE, SIZE), (0, 0))

    f.close()
    s.close()
