# https://exercism.io/my/solutions/b6eafe07347347c9b4078b9cf03c92aa

from functools import partial
from operator import add, sub, mul, floordiv


class StackUnderflowError(Exception):
    pass


class ForthSyntaxError(Exception):
    pass


def pop(stack):
    try:
        return stack.pop()
    except Exception:
        raise StackUnderflowError('Empty stack.')


def push(num, stack):
    stack.append(num)


def math(op, stack):
    arg2, arg1 = pop(stack), pop(stack)
    push(op(arg1, arg2), stack)


def dup(stack):
    last = pop(stack)
    push(last, stack)
    push(last, stack)


def drop(stack):
    pop(stack)


def swap(stack):
    arg2, arg1 = pop(stack), pop(stack)
    push(arg2, stack)
    push(arg1, stack)


def over(stack):
    arg2, arg1 = pop(stack), pop(stack)
    push(arg1, stack)
    push(arg2, stack)
    push(arg1, stack)


GLOBAL_SYMBOLS = {
    '+': partial(math, add),
    '-': partial(math, sub),
    '*': partial(math, mul),
    '/': partial(math, floordiv),
    'dup': dup,
    'drop': drop,
    'swap': swap,
    'over': over
}


def parse_num(token):
    try:
        return int(token)
    except Exception:
        return None


def parse_def(code, local_symbols):
    try:
        name = next(code)
        if parse_num(name) is not None:
            raise ValueError("Can't redifine literals.")
        expr = []
        while (token := next(code)) != ';':
            # Every word in local definitions will be a primitive word
            if token in local_symbols:
                expr.extend(local_symbols[token])
            else:
                expr.append(token)
        local_symbols[name] = expr
    except StopIteration:
        raise ForthSyntaxError('Syntax error.')


def eval_primitive(token, stack):
    """Evaluates literals or primitive words only."""
    if (num := parse_num(token)) is not None:
        push(num, stack)
    elif token not in GLOBAL_SYMBOLS:
        raise ValueError(f'Undefined word {token}.')
    else:
        GLOBAL_SYMBOLS[token](stack)


def evaluate(input_data):
    # Let's treat source code as an input stream (more like forth really works)
    code = map(str.lower, ' '.join(input_data).split())
    stack = []
    local_symbols = dict()
    try:
        while True:
            token = next(code)
            if token == ':':
                parse_def(code, local_symbols)
            elif token in local_symbols:
                for t in local_symbols[token]:
                    eval_primitive(t, stack)
            else:
                eval_primitive(token, stack)
    except StopIteration:
        return stack
