#!/usr/bin/python2
# https://www.hackerrank.com/challenges/zipped/problem

def averages(subjects):
    students = zip(*subjects)
    return map(lambda x: sum(x) / n, students)

if __name__ == '__main__':
    _, n = map(int, raw_input().split())
    subjects = [map(float, raw_input().split()) for _ in range(n)]
    for i in averages(subjects):
        print '{0:.1f}'.format(i)
