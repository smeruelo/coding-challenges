#!/usr/bin/python3
# https://abc096.contest.atcoder.jp/tasks/abc096_c

def paintable(grid, rows, columns):
    def isolated(r, c):
        if r > 0 and grid[r-1][c] == '#':
            return False
        if r < rows - 1 and grid[r+1][c] == '#':
            return False
        if c > 0 and grid[r][c-1] == '#':
            return False
        if c < columns - 1 and grid[r][c+1] == '#':
            return False
        return True

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == '#' and isolated(r, c):
                return False
    return True


if __name__ == '__main__':
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    if paintable(grid, h, w):
        print('Yes')
    else:
        print('No')
