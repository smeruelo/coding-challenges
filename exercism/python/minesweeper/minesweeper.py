
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
    
    aux_field = [[0] * cols for _ in range(rows)]

    def in_bounds(i, j):
        return i >= 0 and i < rows and j >= 0 and j < cols

    def add_count(i, j):
        for r in range(i - 1, i + 2):
            for c in range(j - 1, j + 2):
                if in_bounds(r, c):
                    aux_field[r][c] += 1

    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] == '*':
                add_count(i, j)

    for i, row in enumerate(minefield):
        aux_row = ''
        for j, char in enumerate(row):
            if char == '*' or aux_field[i][j] == 0:
                aux_row += char
            else:
                aux_row += str(aux_field[i][j])
        minefield[i] = aux_row

    return minefield
