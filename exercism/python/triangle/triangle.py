# https://exercism.io/my/solutions/0b66635e96c4419b97da8e2ec35d7ed3


def triangle(f):
    return lambda sides: all(sides) and \
        sides[0] + sides[1] >= sides[2] and \
        sides[1] + sides[2] >= sides[0] and \
        sides[0] + sides[2] >= sides[1] and f(sides)


@triangle
def is_equilateral(sides):
    return len(set(sides)) == 1


@triangle
def is_isosceles(sides):
    return len(set(sides)) <= 2


@triangle
def is_scalene(sides):
    return len(set(sides)) == 3
