from string import whitespace, ascii_letters, ascii_uppercase


def is_question(phrase):
    return '?' in phrase and is_empty(phrase[len(phrase)-phrase[::-1].find('?'):])


def is_yell(phrase):
    return any(map(lambda c: c in ascii_letters, phrase)) and \
        all(map(lambda c: c not in ascii_letters or c in ascii_uppercase, phrase))


def is_empty(phrase):
    return all(map(lambda c: c in whitespace, phrase))


def hey(phrase):
    if is_question(phrase) and is_yell(phrase):
        return "Calm down, I know what I'm doing!"
    if is_question(phrase):
        return 'Sure.'
    if is_yell(phrase):
        return 'Whoa, chill out!'
    if is_empty(phrase):
        return 'Fine. Be that way!'
    return 'Whatever.'
