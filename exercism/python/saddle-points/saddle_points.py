# https://exercism.io/my/solutions/3eb1436fb16a4c1b88d3345b0f572316


def irregular(matrix):
    """Returns True if not all rows of the given matrix have the same length."""

    if matrix == []:
        return False
    l = len(matrix[0])
    return any([len(row) != l for row in matrix])


def saddle_points(matrix):
    """Returns a set of positions in the given matrix where its values are saddle points."""

    if matrix == []:
        return set()

    if irregular(matrix):
        raise ValueError('Matrix rows are not equal in size.')

    rows_max = [matrix[row][0] for row in range(len(matrix))]
    cols_min = matrix[0]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > rows_max[row]:
                rows_max[row] = matrix[row][col]
            if matrix[row][col] < cols_min[col]:
                cols_min[col] = matrix[row][col]

    saddle_points = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == rows_max[row] and matrix[row][col] == cols_min[col]:
                saddle_points.add((row + 1, col + 1))
    return saddle_points
