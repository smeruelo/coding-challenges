# https://projecteuler.net/problem=1

def is_multiple (i, j):
    return i != 0 and i % j == 0

def sum (n):
    acc = 0
    for i in range(3, n):
        if is_multiple(i, 3) or is_multiple(i, 5):
            acc += i
    return acc

def main ():
    print sum(1000)

if __name__ == "__main__":
    main()

