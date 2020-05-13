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
        raise StackUnderflowError ('Empty stack.')

def math(op, stack):
    arg2, arg1 = pop(stack), pop(stack)
    stack.append(op(arg1, arg2))

def dup(stack):
    last = pop(stack)
    stack.append(last)
    stack.append(last)

def drop(stack):
    pop(stack)

def swap(stack):
    arg2, arg1 = pop(stack), pop(stack)
    stack.append(arg2)
    stack.append(arg1)

def over(stack):
    arg2, arg1 = pop(stack), pop(stack)
    stack.append(arg1)
    stack.append(arg2)
    stack.append(arg1)

GLOBAL_SYMBOLS = {'+': partial(math, add),
                  '-': partial(math, sub),
                  '*': partial(math, mul),
                  '/': partial(math, floordiv),
                  'dup': dup,
                  'drop': drop,
                  'swap': swap,
                  'over': over}

def define(tokens, local_symbols):
    name, *expr = tokens
    if parse_num(name) is not None:
        raise StackUnderflowError("Can't redifine literals")
    local_symbols[name] = expr

def parse_def(s):
    s.strip()
    if s[0] == ':' and s[-1] == ';':
        tokens = s[1:-2].split()
        if len(tokens) < 2:
            raise ForthSyntaxError ('Syntax error')
        return tokens
    else:
        return None

def parse_cmd(token):
    token = token.lower()
    if token in GLOBAL_SYMBOLS:
        return GLOBAL_SYMBOLS[token]
    return None

def parse_num(token):
    try:
        return int(token)
    except Exception:
        return None

def eval_s(s, stack, local_symbols):
    if (tokens := parse_def(s)) is not None:
        define(tokens, local_symbols)
    else:
        tokens = s.split()
        while tokens != []:
            token = tokens.pop(0)
            if token in local_symbols:
                tokens = local_symbols[token] + tokens
            elif (cmd := parse_cmd(token)) is not None:
                cmd(stack)
            elif (num := parse_num(token)) is not None:
                stack.append(num)
            else:
                raise ForthSyntaxError ('Syntax error')
    return stack

def evaluate(input_data):
    stack = []
    local_symbols = dict()
    for s in input_data:
        stack = eval_s(s, stack, local_symbols)
    return stack
