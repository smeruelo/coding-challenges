#!/usr/bin/python3
# https://adventofcode.com/2018/day/7

from collections import defaultdict


def parse_data(data):
    ancestors = defaultdict(set)
    successors = defaultdict(set)
    for line in data:
        successor = line[36]
        ancestor = line[5]
        ancestors[successor].add(ancestor)
        if ancestor not in ancestors:
            ancestors[ancestor] = set()
        successors[ancestor].add(successor)
    return ancestors, successors

def next_steps(steps, done):
    available = []
    for step, ancestors in steps.items():
        if not step in done and not ancestors.difference(done):
            available.append(step)
    return sorted(available)

def duration(step):
    return 60 + ord(step) - 64


if __name__ == '__main__':
    with open('07_the_sum_of_its_parts.input') as f:
        data = f.read().split('\n')
    ancestors, successors = parse_data(data)

    # part 1
    done = set()
    output = ''
    nxt = next_steps(ancestors, done)
    while nxt:
        output += nxt[0]
        done.add(nxt[0])
        nxt = next_steps(ancestors, done)
    print(output)

    # part 2
    workers = [0] * 5
    end = dict()
    done = set()
    second = 0
    for step in next_steps(ancestors, done):
        worker, second = min(enumerate(workers), key=lambda x: x[1])
        workers[worker] = second + duration(step)
        end[step] = second + duration(step)
    while end:
        current_step = min(end, key=lambda x: end[x])
        second = end.pop(current_step)
        done.add(current_step)
        for step in sorted(successors[current_step]):
            if not ancestors[step].difference(done):
                worker, sec = min(enumerate(workers), key=lambda x: x[1])
                second = max(second, sec)
                workers[worker] = second + duration(step)
                end[step] = second + duration(step)
    print(second)
