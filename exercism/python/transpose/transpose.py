# https://exercism.io/my/solutions/3fa99efc451846ea88aafe4b3706fb2a


def transpose(l):
    lines = l.split('\n')
    length = len(lines)
    width = max(map(len, lines))

    transposed = [[] for _ in range(width)]
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            for _ in range(i - len(transposed[j])):
                transposed[j].append(' ')
            transposed[j].append(c)
    return '\n'.join(map(lambda x: ''.join(x), transposed))
