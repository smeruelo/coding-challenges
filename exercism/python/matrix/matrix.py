# https://exercism.io/my/solutions/2f6e880c131d4a35bdb83063bf5ff996


class Matrix(object):
    """2D array of integers."""

    def __init__(self, matrix_string):
        self._matrix = [[int(i) for i in s.split()]
                        for s in matrix_string.split('\n')]

    def row(self, index):
        """Returns the index-th row of the matrix."""

        if index > 0 and index <= len(self._matrix):
            return self._matrix[index-1]
        else:
            raise MatrixIndexError('Matrix index out of range.')

    def column(self, index):
        """Returns the index-th column of the matrix.

        It assumes all the rows have equal length,
        although input strings are not validated."""

        if index > 0 and index <= len(self._matrix[0]):
            return [self._matrix[j][index-1] for j in range(len(self._matrix))]
        else:
            raise MatrixIndexError('Matrix index out of range.')


class MatrixIndexError(Exception):
    pass
