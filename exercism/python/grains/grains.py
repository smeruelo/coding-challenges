# https://exercism.io/my/solutions/409d03d345394ae58b9778d1dca85099


def on_square(number):
    if number < 1 or number > 64:
        raise ValueError('Number must be [1-64].')
    return 2 ** (number - 1)


def total_after(number):
    if number < 1 or number > 64:
        raise ValueError('Number must be [1-64].')
    return (2 ** number) - 1
