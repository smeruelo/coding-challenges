#!/usr/bin/python3
# https://adventofcode.com/2017/day/4


def is_valid_1(passphrase):
    words = set(passphrase)
    return len(words) == len(passphrase)


def is_valid_2(passphrase):
    words = set(map(lambda x: ''.join(sorted(x)), passphrase))
    return len(words) == len(passphrase)


if __name__ == '__main__':
    with open('04_high-entropy_passphrases.input') as f:
        passphrases = [l.split() for l in f.readlines()]

    # part 1
    print(sum(map(is_valid_1, passphrases)))

    # part 2
    print(sum(map(is_valid_2, passphrases)))
