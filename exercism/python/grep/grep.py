import operator


def grep_n(pattern, lines, flags):
    op = operator.eq if '-x' in flags else operator.contains
    if '-i' in flags:
        aux = lambda pattern, line: op(line.lower(), pattern.lower())
    else:
        aux = lambda pattern, line: op(pattern, line)
    if '-v' in flags:
        f = lambda pattern, line: not aux(pattern, line)
    else:
        f = aux

    numbered_lines = map(lambda x: (x[0]+1, x[1]), enumerate(lines))
    return list(filter(lambda x: f(pattern, x[1]), numbered_lines))


def grep(pattern, flags, files):
    output = []
    for file in files:
        with open(file) as f:
            lines = f.read().split('\n')
            results = grep_n(pattern, lines, flags)
            if '-l' in flags:
                if results:
                    output.append(f'{file}\n')
            else:
                file_name = f'{file}:' if len(files) > 1 else ''
                for i, line in results:
                    if line != '':
                        line_number = f'{i}:' if '-n' in flags else ''
                        output.append(f'{file_name}{line_number}{line}\n')
    return ''.join(output)
