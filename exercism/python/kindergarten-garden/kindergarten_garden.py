# https://exercism.io/my/solutions/36868d9cf1774a9380178355cc1c12f6


class Garden(object):

    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    PLANTS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=None):
        self._diagram = diagram
        self._students = sorted(students) if students else self.STUDENTS
        self._column = {k: v * 2 for v, k in enumerate(self._students)}

    def plants(self, student):
        """Returns the 4 plants that belong to the given student."""

        # i1 (i2) is the index in diagram for the first child's plant in the first (second) row.
        i1 = self._column[student]
        i2 = i1 + len(self._diagram) // 2 + 1
        plants = [self._diagram[i1], self._diagram[i1+1], self._diagram[i2], self._diagram[i2+1]]
        return [self.PLANTS[p] for p in plants]
