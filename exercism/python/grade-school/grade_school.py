class School:
    TOP_GRADE = 15  # Assuming a small and well-known number of grades

    def __init__(self):
        self.__db = [[] for _ in range(self.TOP_GRADE + 1)]

    def add_student(self, name, grade):
        self.__db[grade].append(name)

    def roster(self):
        students = []
        for g in range(self.TOP_GRADE):
            students.extend(sorted(self.__db[g]))
        return students

    def grade(self, grade_number):
        return sorted(self.__db[grade_number])
