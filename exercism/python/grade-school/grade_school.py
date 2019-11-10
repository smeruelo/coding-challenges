class School:
    TOP_GRADE = 15  # Assuming a small and well-known number of grades

    def __init__(self):
        self._db = [[] for _ in range(self.TOP_GRADE + 1)]

    @property
    def db(self):
        return self._db

    def add_student(self, name, grade):
        self._db[grade].append(name)

    def roster(self):
        students = []
        for g in range(self.TOP_GRADE):
            students.extend(sorted(self._db[g]))
        return students

    def grade(self, grade_number):
        return sorted(self._db[grade_number])
