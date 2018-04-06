#!/usr/bin/python3
# https://abc063.contest.atcoder.jp/tasks/arc075_a

def max_grade(s):
    sum_grades = sum(s)
    if sum_grades % 10 == 0:
        aux = sorted(filter(lambda x: x % 10 != 0, s))
        if aux:
            return sum_grades - aux[0]
        else:
            return 0
    else:
        return sum_grades


if __name__ == '__main__':
    n = int(input())
    s = [int(input()) for _ in range(n)]
    print(max_grade(s))
