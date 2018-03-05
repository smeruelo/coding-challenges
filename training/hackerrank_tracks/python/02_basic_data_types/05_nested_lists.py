#!/usr/bin/python2
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n = int(raw_input())
    students = []
    for i in range(n):
        name = raw_input()
        grade = float(raw_input())
        students.append([name, grade])
    students.sort(key = lambda x: x[1])
    students_without_lowest = filter(lambda x: x[1] != students[0][1], students)
    names_seconds = [e[0] for e in students_without_lowest if e[1] == students_without_lowest[0][1]]
    names_seconds.sort()
    for name in names_seconds:
        print name
