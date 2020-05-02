
def found(x):
    return all(map(lambda i: x % i == i - 1, range(2, 7)))

i = 1
while not found(7 * i):
    i += 1
print(7 * i)
