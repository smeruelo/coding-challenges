#!/usr/bin/python3

from functools import reduce

MAJOR = [0, 2, 4, 5, 7, 9, 11]
MINOR = [0, 2, 3, 5, 7, 8, 10]
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
VALUES = dict()
for value, note in enumerate(NOTES):
    VALUES[note] = value

def norm_note(note):
    if len(note) == 1:
        return note
    else:
        if note[1] == '#':
            v = (VALUES[note[0]] + 1) % 12
        else:
            v = (VALUES[note[0]] - 1) % 12
        return NOTES[v]

def diff(note, half_steps):
    return NOTES[(VALUES[note] - half_steps) % 12]
    
def scales_note(note):
    return set(list(map(lambda x: 'M' + diff(note, x), MAJOR)) + \
               list(map(lambda x: 'm' + diff(note, x), MINOR)))

def scales_song(song):
    return sorted(reduce(lambda x, y: x.intersection(y), map(scales_note, song)))


if __name__ == '__main__':
    for i in range(int(input())):
        size = int(input())
        if size == 0:
            scales = sorted(list(map(lambda x: 'M' + x, NOTES)) + \
                            list(map(lambda x: 'm' + x, NOTES)))
        else:
            song = set(map(norm_note, input().split()))
            scales = scales_song(song)
        if scales:
            print('Case #{}: {}'.format(i + 1, ' '.join(scales)))
        else:
            print('Case #{}: None'.format(i + 1))
