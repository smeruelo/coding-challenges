# https://exercism.io/my/solutions/36868d9cf1774a9380178355cc1c12f6


class Garden(object):

    STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    PLANTS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.students = sorted(students) if students else self.STUDENTS
        self.column = {key: value * 2 for value, key in enumerate(self.students)}

    def plants(self, student):
        """Returns the 4 plants that belong to the given student."""

        i_row1 = self.column[student]
        i_row2 = i_row1 + len(self.diagram) // 2 + 1
        plants = [self.diagram[i_row1], self.diagram[i_row1 + 1],
                  self.diagram[i_row2], self.diagram[i_row2 + 1]]
        return [self.PLANTS[p] for p in plants]
