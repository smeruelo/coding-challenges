# https://exercism.io/my/solutions/8fc392ad3d7b4196809fbc0cfe08e02e
#
# Vertexes:   A --- B
#             |     |
#             D --- C

def print_canvas(strings):
    w = len(strings[0])
    h = len(strings)

    print();
    print(' ' + ''.join([str(i%10) for i in range(w)]))
    for r in range(h):
        print(str(r%10) + strings[r])
    print();


def find_rectangles(row, col, strings):
    w = len(strings[0])
    h = len(strings)

    def find_vertexes_in_row(r, start, end):
        vertexes = []
        for c in range(start, end):
            if strings[r][c] == '+':
                vertexes.append((r, c))
            elif strings[r][c] != '-':
                break
        return vertexes

    def find_vertexes_in_col(c, start, end):
        vertexes = []
        for r in range(start, end):
            if strings[r][c] == '+':
                vertexes.append((r, c))
            elif strings[r][c] != '|':
                break
        return vertexes

    # A = (row, col)
    Bs = find_vertexes_in_row(row, col + 1, w)
    Ds = find_vertexes_in_col(col, row + 1, h)
    CBs = set()
    CDs = set()
    for r, b in Bs:
        CBs.update(find_vertexes_in_col(b, r + 1, h))
    for d, c in Ds:
        CDs.update(find_vertexes_in_row(d, c + 1, w))
    return len(CBs & CDs)


def rectangles(strings):
    # print_canvas(strings)
    count = 0
    for r in range(len(strings)):
        for c in range(len(strings[0])):
            if strings[r][c] == '+':
                count += find_rectangles(r, c, strings)
    return count
