# https://exercism.io/my/solutions/139d4dedc67d4b3693ed32e632e032d1

def leap_year(year):
    def multiple(n):
        return year % n == 0
    return multiple(4) and (not multiple(100) or multiple(400))
