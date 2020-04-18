# https://exercism.io/my/solutions/b67438e9775a4e148ae37db6132a50b7

from datetime import timedelta

GIGASECOND = 1000000000


def add(moment):
    return moment + timedelta(seconds=GIGASECOND)
