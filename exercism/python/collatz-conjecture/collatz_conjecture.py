# https://exercism.io/my/solutions/82d18486853742ffbb6be2021558e4ae


def collatz_steps(number):
    def rec(number, steps):
        if number == 1:
            return steps
        nxt = number // 2 if number % 2 == 0 else 3 * number + 1
        return rec(nxt, steps + 1)

    if number < 1:
        raise ValueError('Provided number is not an integer.')

    return rec(number, 0)
