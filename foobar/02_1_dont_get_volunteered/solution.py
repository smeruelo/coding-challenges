def cell_to_coords(cell):
    row = cell / 8
    col = cell % 8
    return [row, col]


def coords_to_cell(coords):
    row, col = coords
    return row * 8 + col


def are_valid_coords(coords):
    row, col = coords
    return row >= 0 and row < 8 and col >= 0 and col < 8


def reachable(cell):
    row, col = cell
    jumps = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
    ]
    x = filter(lambda coords: are_valid_coords(coords), jumps)
    return x


def bfs(src, dest):
    visited = [[False] * 8 for i in range(8)]
    pending = [(src, 0)]

    while pending != []:
        current_cell, current_jumps = pending.pop(0)
        row, col = current_cell
        visited[row][col] = True
        if current_cell == dest:
            return current_jumps
        for cell in reachable(current_cell):
            row, col = cell
            if not visited[row][col]:
                pending.append((cell, current_jumps + 1))


def solution(src, dest):
    return bfs(cell_to_coords(src), cell_to_coords(dest))
