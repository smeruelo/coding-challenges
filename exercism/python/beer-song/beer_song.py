# https://exercism.io/my/solutions/a43b8babd915454c822b5f1bf143ebae


def verse(i):
    VERSE_N = [f'{i} bottles of beer on the wall, {i} bottles of beer.',
               f'Take one down and pass it around, {i - 1} bottle{"s" if i > 2 else ""} of beer on the wall.']
    VERSE_1 = ['1 bottle of beer on the wall, 1 bottle of beer.',
               'Take it down and pass it around, no more bottles of beer on the wall.']
    VERSE_0 = ['No more bottles of beer on the wall, no more bottles of beer.',
               'Go to the store and buy some more, 99 bottles of beer on the wall.']

    if i > 1:
        return VERSE_N
    elif i == 1:
        return VERSE_1
    else:
        return VERSE_0


def recite(start, take=1):
    song = []
    for i in range(start, start - take, -1):
        song.extend(verse(i))
        if i > start - take + 1:
            song.append('')
    return song
