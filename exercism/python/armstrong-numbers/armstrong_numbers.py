def is_armstrong(number):
    n = str(number)
    return sum(map(lambda d: pow(int(d), len(n)), n)) == number
