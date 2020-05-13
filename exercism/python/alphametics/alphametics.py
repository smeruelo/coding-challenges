# https://exercism.io/my/solutions/b32e89e49bd945799225bb294a842ef6

from itertools import permutations
from string import ascii_uppercase, digits


def solve(puzzle):
    solutions = []
    letters = tuple(set(ascii_uppercase).intersection(set(puzzle)))
    for p in permutations(digits, len(letters)):
        trans = dict(zip(letters, p))
        try:
            if eval(puzzle.translate(str.maketrans(trans))):
                solutions.append(dict(zip(trans.keys(), map(int, trans.values()))))
        except SyntaxError:
            pass  # When numbers start by 0, but these cases aren't valid anyway

    return None if len(solutions) != 1 else solutions[0]
