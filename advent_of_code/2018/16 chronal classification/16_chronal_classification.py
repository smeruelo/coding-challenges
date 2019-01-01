#!/usr/bin/python3
# https://adventofcode.com/2018/day/16

from collections import namedtuple

Ins = namedtuple('Ins', 'op a b c')


def parse(data, i):
    def parse_regs(line):
        return list(map(int, line.split('[')[1].split(']')[0].split(',')))

    def parse_ins(line):
        op, a, b, c = map(int, line.split())
        return Ins(op, a, b, c)

    return (parse_regs(data[i]), parse_ins(data[i+1]), parse_regs(data[i+2]))


def result(regs, c, value):
    new_regs = regs[:]
    new_regs[c] = value
    return new_regs


def addr(a, b, c, regs):
    return result(regs, c, regs[a] + regs[b])


def addi(a, b, c, regs):
    return result(regs, c, regs[a] + b)


def mulr(a, b, c, regs):
    return result(regs, c, regs[a] * regs[b])


def muli(a, b, c, regs):
    return result(regs, c, regs[a] * b)


def banr(a, b, c, regs):
    return result(regs, c, regs[a] & regs[b])


def bani(a, b, c, regs):
    return result(regs, c, regs[a] & b)


def borr(a, b, c, regs):
    return result(regs, c, regs[a] | regs[b])


def bori(a, b, c, regs):
    return result(regs, c, regs[a] | b)


def setr(a, b, c, regs):
    return result(regs, c, regs[a])


def seti(a, b, c, regs):
    return result(regs, c, a)


def gtir(a, b, c, regs):
    return result(regs, c, 1 if a > regs[b] else 0)


def gtri(a, b, c, regs):
    return result(regs, c, 1 if regs[a] > b else 0)


def gtrr(a, b, c, regs):
    return result(regs, c, 1 if regs[a] > regs[b] else 0)


def eqir(a, b, c, regs):
    return result(regs, c, 1 if a == regs[b] else 0)


def eqri(a, b, c, regs):
    return result(regs, c, 1 if regs[a] == b else 0)


def eqrr(a, b, c, regs):
    return result(regs, c, 1 if regs[a] == regs[b] else 0)


def narrow_down(op_options):
    op = [None] * 16

    def narrowed():
        for i, fs in enumerate(op_options):
            if len(fs) == 1 and not op[i]:
                return i

    while not all(op):
        current = narrowed()
        current_fs = list(op_options[current])[0]
        op[current] = current_fs
        for i, fs in enumerate(op_options):
            if i != current:
                fs.discard(current_fs)
    return op


if __name__ == '__main__':
    with open('16_chronal_classification.input1') as f:
        data = f.readlines()
    with open('16_chronal_classification.input2') as f:
        program = (Ins(*map(int, l.split())) for l in f.readlines())

    fs_names = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori',
                'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']
    fs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    fs_dict = dict(zip(fs_names, fs))

    # Part 1
    samples = 0
    for i in range(0, len(data), 4):
        regs_before, ins, regs_after = parse(data, i)
        if sum(1 for f in fs_names if fs_dict[f](ins.a, ins.b, ins.c, regs_before) == regs_after) >= 3:
            samples += 1
    print(samples)

    # Part 2
    op_options = [set(fs_names) for _ in range(16)]
    for i in range(0, len(data), 4):
        regs_before, ins, regs_after = parse(data, i)
        results = map(lambda f: fs_dict[f](ins.a, ins.b, ins.c, regs_before), fs_names)
        options = [f for f, r in zip(fs_names, results) if r == regs_after]
        op_options[ins.op].intersection_update(options)
    op = narrow_down(op_options)

    regs = [0, 0, 0, 0]
    for ins in program:
        regs = fs_dict[op[ins.op]](ins.a, ins.b, ins.c, regs)
    print(regs[0])
