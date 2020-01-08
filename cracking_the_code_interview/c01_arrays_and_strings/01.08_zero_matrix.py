# Problem: Zero Matrix
# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.


# O(m * n * max{n, m}), extra space (sets, m + n)
def zero_matrix_1(matrix):
    rows = set()
    cols = set()

    # O(m * n)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    # O(m * n * max{n, m})
    # Search in a set, worst case: O(n)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row in rows or col in cols:
                matrix[row][col] = 0

    return matrix


# O(m * n), extra space (vectors, m + n)
def zero_matrix_2(matrix):
    if not matrix:
        return []

    rows = [False] * len(matrix)
    cols = [False] * len(matrix[0])

    # O(m * n)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                rows[row] = True
                cols[col] = True

    # O(m * n)
    # Access a vector: O(1)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if rows[row] or cols[col]:
                matrix[row][col] = 0

    return matrix


# O(m * n), no extra space
# We'll use the first column and the first row to mark the ones that will turn zeros.
def zero_matrix_3(matrix):
    # O(m * n)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    # O(m * n)
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    return matrix
