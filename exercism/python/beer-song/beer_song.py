# https://exercism.io/my/solutions/a43b8babd915454c822b5f1bf143ebae

LIMIT = 100


def verse(i):
    def bottles_str(i):
        return 'no more bottles' if i < 1 else f'{i} bottle{"s" if i > 1 else ""}'

    def take_str(i):
        return 'one' if i > 1 else 'it'

    before = bottles_str(i)
    after = bottles_str((i - 1) % LIMIT)

    first = f'{before[0].upper()}{before[1:]} of beer on the wall, {before} of beer.'
    if i > 0:
        second = f'Take {take_str(i)} down and pass it around'
    else:
        second = 'Go to the store and buy some more'
    third = f'{after} of beer on the wall.'

    return [first, f'{second}, {third}']


def recite(start, take=1):
    song = []
    for i in range(start, start - take, -1):
        song.extend(verse(i))
        if i > start - take + 1:
            song.append('')
    return song
