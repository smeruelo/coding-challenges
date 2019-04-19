# https://exercism.io/my/solutions/3eb1436fb16a4c1b88d3345b0f572316


def saddle_points(matrix):
    """Returns a set of positions in the given matrix where its values are saddle points."""

    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError('Matrix rows are not equal in size.')

    matrix_t = list(map(list, zip(*matrix)))
    rows_max = [max(row) for row in matrix]
    cols_min = [min(row) for row in matrix_t]

    saddle_points = set()
    for row in range(len(matrix)):
        for col in range(len(matrix_t)):
            if matrix[row][col] == rows_max[row] and matrix[row][col] == cols_min[col]:
                saddle_points.add((row + 1, col + 1))
    return saddle_points
