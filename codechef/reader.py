from sys import stdin

def read():
    input_data = stdin.read().split()
    for token in input_data:
        yield token

def tokens(g, n):
    t = []
    for _ in range(n):
        t.append(next(g))
    return t

g = read()
print(next(g))
print(tokens(g, 3))
