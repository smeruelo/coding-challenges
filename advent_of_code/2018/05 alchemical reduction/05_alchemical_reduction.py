#!/usr/bin/python3
# https://adventofcode.com/2018/day/5


def react(old):
    new = [old[0]]
    i = 1
    while i < len(old):
        if old[i] == new[-1].swapcase():
            i += 1
            new.pop()
            if not new and i < len(old):
                new = [old[i]]
                i += 1
        else:
            new.append(old[i])
            i += 1
    return new


if __name__ == '__main__':
    with open('05_alchemical_reduction.input') as f:
        s = f.read()

    # part 1
    new = react(s)
    print(len(new))

    # part 2
    minimum = len(s)
    for c in set(map(lambda x: x.lower(), s)):
        no_c = ''.join(filter(lambda x: x.lower() != c, s))
        minimum = min(minimum, len(react(no_c)))
    print(minimum)
