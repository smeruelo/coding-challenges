
# Grammar:
#
# WHATIS NUMBER (OPERATION NUMBER)* QUESTIONMARK

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

def parse_operation(tokens):
    try:
        if tokens[0] == 'plus':
            f = lambda x, y: x + y
            next_token = 1
        elif tokens[0] == 'minus':
            f = lambda x, y: x - y
            next_token = 1
        elif tokens[0] == 'multiplied' and tokens[1] == 'by':
            f = lambda x, y: x * y
            next_token = 2
        elif tokens[0] == 'divided' and tokens[1] == 'by':
            f = lambda x, y: x // y
            next_token = 2
        else:
            raise ValueError('Unsupported operation.')

        op2, rest_tokens = parse_number(tokens[next_token:])
        return (f, op2, rest_tokens)
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
