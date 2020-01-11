# https://exercism.io/my/solutions/541ee95c33d64217b699fd3e428751a8


def annotate(minefield):

    def validate(minefield):
        if len(minefield) > 0:
            if any([len(row) != len(minefield[0]) for row in minefield]):
                raise ValueError("Not a valid rectangular field")
            if any([cell != '*' and cell != ' ' for row in minefield for cell in row]):
                raise ValueError("Invalid character")

    validate(minefield)
    rows = len(minefield)
    if rows == 0:
        return minefield
    cols = len(minefield[0])
    if cols == 0:
        return minefield
    
    def adjacent_cells(i, j):
        def in_bounds(i, j):
            return i >= 0 and i < rows and j >= 0 and j < cols

        return filter(lambda cell: in_bounds(cell[0], cell[1]),
                      [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                       (i, j - 1), (i, j + 1),
                       (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)])

    for i in range(rows):
        row = ''
        for j in range(cols):
            if minefield[i][j] == ' ':
                mines = sum(map(lambda cell: 1 if minefield[cell[0]][cell[1]] == "*" else 0,
                                adjacent_cells(i, j)))
                row += str(mines) if mines > 0 else ' '
            else:
                row += '*'
        minefield[i] = row

    return minefield
