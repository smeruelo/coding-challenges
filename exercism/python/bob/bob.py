# https://exercism.io/my/solutions/a3da23b5f2034f9eb2b6b7dcd9902206


def is_question(phrase):
    return not is_empty(phrase) and phrase.strip()[-1] == '?'


def is_yell(phrase):
    return phrase.isupper()


def is_empty(phrase):
    return not phrase.strip()


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
