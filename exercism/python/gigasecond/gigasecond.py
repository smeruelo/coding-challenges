# https://exercism.io/my/solutions/b67438e9775a4e148ae37db6132a50b7

from datetime import timedelta

GIGASECOND = timedelta(seconds=10**9)


def add(moment):
    return moment + GIGASECOND
