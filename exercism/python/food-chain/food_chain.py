# https://exercism.io/my/solutions/ef94b3398bea4bc891e0bc3ec7ec3e0a


THINGS = {
    1: ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
    2: ("spider", "It wriggled and jiggled and tickled inside her."),
    3: ("bird", "How absurd to swallow a bird!"),
    4: ("cat", "Imagine that, to swallow a cat!"),
    5: ("dog", "What a hog, to swallow a dog!"),
    6: ("goat", "Just opened her throat and swallowed a goat!"),
    7: ("cow", "I don't know how she swallowed a cow!"),
    8: ("horse", "She's dead, of course!")
}

def verse(num):
    fst_animal, fst_response = THINGS[num]
    output = [f'I know an old lady who swallowed a {fst_animal}.', fst_response]
    if num != 8:
        for i in range(num - 1, 0, -1):
            prv_animal, _ = THINGS[i + 1]
            animal, response = THINGS[i]
            dot = '.' if i != 2 else ''
            optional = '' if i != 2 else f' that {response[3:]}'
            output.append(f'She swallowed the {prv_animal} to catch the {animal}{dot}{optional}')
            if i == 1:
                output.append(response)
    return '\n'.join(output)

def recite(start_verse, end_verse):
    return '\n\n'.join((verse(i) for i in range(start_verse, end_verse + 1))).split('\n')
