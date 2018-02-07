#!/usr/bin/python2
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

if __name__ == '__main__':
    n = int(raw_input())
    marks = 0
    Student = namedtuple('Student', raw_input())
    for _ in range(n):
        student = Student(*raw_input().split())
        marks += float(student.MARKS)
    print '{0:.2f}'.format(marks/n)
