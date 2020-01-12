# https://exercism.io/my/solutions/ce4023b2ca6749b89c8d02cd428b6408
#
# Grammar: WHATIS NUMBER (OPERATION NUMBER)* QUESTIONMARK

from operator import add, mul, floordiv, sub


def parse_whatis(tokens):
    if len(tokens) >= 2 and tokens[0] == 'What' and tokens[1] == 'is':
        return tokens[2:]
    else:
        raise ValueError('Non-math question.')

def parse_number(tokens):
    try:
        return (int(tokens[0]), tokens[1:])
    except Exception:
        raise ValueError('Invalid syntax.')

def parse_power(token):
    if (len(token) >= 3 and
        (token[-2:] == 'st' or token[-2:] == 'nd' or token[-2:] == 'rd' or token[-2:] == 'th')):
        return int(token[:-2])
    else:
        raise ValueError('Invalid syntax.')

def parse_operation(tokens):
    try:
        if tokens[0] == 'plus':
            return (add,) + parse_number(tokens[1:])
        if tokens[0] == 'minus':
            return (sub,) + parse_number(tokens[1:])
        if tokens[0] == 'multiplied' and tokens[1] == 'by':
            return (mul,) + parse_number(tokens[2:])
        if tokens[0] == 'divided' and tokens[1] == 'by':
            return (floordiv,) + parse_number(tokens[2:])
        if (tokens[0] == 'raised' and tokens[1] == 'to' and
              tokens[2] == 'the' and tokens[4] == 'power'):
            return (pow,) + (parse_power(tokens[3]), tokens[5:])
        raise ValueError('Unsupported operation.')
    except Exception:
        raise ValueError('Invalid syntax.')

def answer(question):
    if question[-1] != '?':
        raise ValueError('Not a question')
    tokens = question[:-1].split(' ')

    value, tokens = parse_number(parse_whatis(tokens))
    while tokens:
        f, op2, tokens = parse_operation(tokens)
        value = f(value, op2)
    return value
