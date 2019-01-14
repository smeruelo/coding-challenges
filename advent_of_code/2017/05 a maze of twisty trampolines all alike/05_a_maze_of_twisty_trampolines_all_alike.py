#!/usr/bin/python3
# https://adventofcode.com/2017/day/5


if __name__ == '__main__':
    with open('05_a_maze_of_twisty_trampolines_all_alike.input') as f:
        data = list(map(int, f.readlines()))

    # part 1
    instructions = data[:]
    count = 0
    current = 0
    while current < len(instructions):
        offset = instructions[current]
        nxt = current + offset
        instructions[current] += 1
        count += 1
        current = nxt
    print(count)

    # part 2
    instructions = data[:]
    count = 0
    current = 0
    while current < len(instructions):
        offset = instructions[current]
        nxt = current + offset
        if offset >= 3:
            instructions[current] -= 1
        else:
            instructions[current] += 1
        count += 1
        current = nxt
    print(count)
