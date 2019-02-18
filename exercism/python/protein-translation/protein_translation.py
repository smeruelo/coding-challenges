#!/usr/bin/python3
# https://exercism.io/my/solutions/69e228fba81a47139e34d794ef9087c3

from itertools import takewhile
from textwrap import wrap

PROTEINS = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
}


def is_not_stop(s):
    return s != 'STOP'


def proteins(strand):
    codons = wrap(strand, 3)
    translation = [PROTEINS[c] for c in codons]
    return [p for p in takewhile(is_not_stop, translation)]
