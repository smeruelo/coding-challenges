#!/usr/bin/python3
# https://abc045.contest.atcoder.jp/tasks/arc061_a

from functools import reduce

def formulas(s):
    formula_list = []
    def aux(current, i):
        if i < len(s):
            aux(current + [s[i]], i + 1)
            aux(current + ['+', s[i]], i + 1)
        else:
            formula_list.append(''.join(current))

    aux([s[0]], 1)
    return formula_list


if __name__ == '__main__':
    s = input()
    print(reduce(lambda x, y: x + eval(y), formulas(s), 0))
