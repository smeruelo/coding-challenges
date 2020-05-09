#!/usr/bin/pypy3

from collections import deque

def reachable(src, terrain):
    def valid(pos):
        n = len(terrain)
        m = len(terrain[0])
        y, x = pos
        return y >= 0 and y < n and x >= 0 and x < m and terrain[y][x] != '#'
        
    y, x = src[0], src[1]
    jumps = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    if terrain[y][x] == '*':
        jumps = map(lambda p: (2 * p[0], 2 * p[1]), jumps)
    dest = map(lambda p: (p[0] + y, p[1] + x), jumps)
    return filter(valid, dest)

def shortest_path(src, target, terrain):
    queue = deque([(src, 0)])
    discovered = [src]
    while queue:
        current_pos, distance = queue.pop()
        if current_pos == target:
            return distance
        for pos in reachable(current_pos, terrain):
            if pos not in discovered:
                queue.appendleft((pos, distance + 1))
                discovered.append(pos)
    return None

def locations(terrain):
    for row, cells in enumerate(terrain):
        col = cells.find('S')
        if col != -1:
            knight = (row, col)
        col = cells.find('P')
        if col != -1:
            princess = (row, col)
        col = cells.find('D')
        if col != -1:
            destination = (row, col)
    return (knight, princess, destination)

def save_princess(terrain):
    knight, princess, destination = locations(terrain)
    path1 = shortest_path(knight, princess, terrain)
    if path1:
        path2 = shortest_path(princess, destination, terrain)
        if path2:
            return str(path1 + path2)
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    for i in range(int(input())):
        n, m = map(int, input().split())
        terrain = [input() for _ in range(n)]
        print('Case #{}: {}'.format(i + 1, save_princess(terrain)))
