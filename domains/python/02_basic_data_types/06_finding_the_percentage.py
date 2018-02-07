#!/usr/bin/python2
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for i in range(n):
        line = raw_input().split()
        name, scores = line[0], map(float, line[1:])
        student_marks[name] = scores

    query_name = raw_input()
    mark1, mark2, mark3 = student_marks[query_name]
    average = (mark1 + mark2 + mark3) / 3
    print("{0:.2f}".format(round(average, 2)))
