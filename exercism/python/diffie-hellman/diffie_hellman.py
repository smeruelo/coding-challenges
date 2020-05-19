# https://exercism.io/my/solutions/4baf13522ca34b88928afff624d07cc1

from secrets import choice


def private_key(p):
    return choice(range(2, p))


def public_key(p, g, private):
    return (g ** private) % p


def secret(p, public, private):
    return (public ** private) % p
