# https://exercism.io/my/solutions/0b66635e96c4419b97da8e2ec35d7ed3


def is_valid(sides):
    return all(sides) and \
        sides[0] + sides[1] >= sides[2] and \
        sides[1] + sides[2] >= sides[0] and \
        sides[0] + sides[2] >= sides[1]


def is_equilateral(sides):
    return is_valid(sides) and \
        sides[0] == sides[1] and sides[1] == sides[2]


def is_isosceles(sides):
    return is_valid(sides) and \
        (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def is_scalene(sides):
    return is_valid(sides) and \
        sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
