#!/usr/bin/python3
# https://cses.fi/problemset/task/1072


def knights(n):
    def two_in_border(k, border_cells):
        threatened = 0 if k < 3 else 2
        return ((border_cells - 1) * border_cells) // 2 - threatened

    def one_in_border_one_inside(k, border_cells):
        threatened = 0 if k < 3 else 2 + 2 * (10 + 4 * (k - 5))
        return (k - 1) * (k - 1) * border_cells - threatened

    output = [0]
    for k in range(2, n + 1):
        border_cells = (k * 2) - 1
        output.append(two_in_border(k, border_cells) +
                      one_in_border_one_inside(k, border_cells) +
                      output[-1])
    return output


if __name__ == '__main__':
    print('\n'.join(map(str, knights(int(input())))))
