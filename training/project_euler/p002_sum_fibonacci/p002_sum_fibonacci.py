# https://projecteuler.net/problem=2

def sum_even_fibonacci (n):
    last1 = last2 = 1
    acc = 0
    current = last1 + last2
    while current < n:
        if current % 2 == 0:
            acc += current
        last2 = last1
        last1 = current
        current = last1 + last2
    return acc

def main ():
    print sum_even_fibonacci (4000000)

if __name__ == "__main__":
    main()

