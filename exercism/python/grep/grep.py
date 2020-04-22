# https://exercism.io/my/solutions/54ca434a98e443afa2d945741195bb91

import operator


def matches(pattern, line, flags):
    if '-i' in flags:
        line = line.lower()
        pattern = pattern.lower()
    op = operator.eq if '-x' in flags else operator.contains
    result = op(line, pattern)
    return not result if '-v' in flags else result


def grep(pattern, flags, files):
    output = []
    for file in files:
        with open(file) as f:
            file_name = f'{file}:' if len(files) > 1 else ''
            for i, line in enumerate(f):
                if line != '' and matches(pattern, line[:-1], flags):
                    if '-l' in flags:
                        output.append(f'{file}\n')
                        break
                    else:
                        line_number = f'{i+1}:' if '-n' in flags else ''
                        output.append(f'{file_name}{line_number}{line}')
    return ''.join(output)
