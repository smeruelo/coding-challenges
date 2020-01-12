# https://exercism.io/my/solutions/deb03998ae1745ef8a402102be9f0f2a

CHARS = {' _ | ||_|   ': '0',
         '     |  |   ': '1',
         ' _  _||_    ': '2',
         ' _  _| _|   ': '3',
         '   |_|  |   ': '4',
         ' _ |_  _|   ': '5',
         ' _ |_ |_|   ': '6',
         ' _   |  |   ': '7',
         ' _ |_||_|   ': '8',
         ' _ |_| _|   ': '9'}


def ocr(char_grid):
    """Converts a 4x3 grid into a char."""

    char = ''.join(char_grid)
    if char in CHARS:
        return CHARS[char]
    return '?'


def chunks(four_row_grid):
    """Divides a 4-row grid of n chars into a list of n 4-row grids of one char."""

    def row_to_chunks(row):
        return [row[i:i+3] for i in range(0, len(row), 3)]

    if four_row_grid and len(four_row_grid[0]) % 3 != 0:
        raise ValueError('Invalid number of columns.')
    rows_chuncked = map(row_to_chunks, four_row_grid)
    return map(lambda *args: list(args), *rows_chuncked)


def grid_to_lines(n_row_grid):
    """Divides a big_grid into a list of 4-rows grids."""

    if len(n_row_grid) % 4 != 0:
        raise ValueError('Invalid number of rows.')
    return [n_row_grid[i:i+4] for i in range(0, len(n_row_grid), 4)]


def convert(input_grid):
    return ','.join(map(lambda line: ''.join(map(ocr, chunks(line))),
                        grid_to_lines(input_grid)))
