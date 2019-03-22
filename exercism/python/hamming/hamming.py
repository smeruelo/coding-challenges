# https://exercism.io/my/solutions/a678ff3fa27d4b15b24aebafb832f210


def distance(strand_a, strand_b):
    """Returns the Hamming distance of two equal length sequences"""

    if len(strand_a) != len(strand_b):
        raise ValueError('DNA strands are not equal in size')
    return sum(map(lambda x, y: x != y, strand_a, strand_b))
