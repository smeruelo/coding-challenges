#!/usr/bin/pypy3

# From brute force output
sec = [0, 1, 2, 10, 46, 212, 982, 4546, 21038, 97350, 450456, 2084324, 9644454]
# Found out that ratio of an / an-1 tends to a constand value
# So there's a recurrence of the form an = x an-1 + y an-2
# Tried with 2 .. 6 variables, worked for 6
# (https://quickmath.com/webMathematica3/quickmath/equations/solve/advanced.jsp)
# an = 7 an-1 - 13 an-2 + 10 an-3 - 4 an-4 + 5 an-5 - 2 an-6
# x = 7,y = -13,z = 10,u = -4,v = 5,w = -2

def calc_all():
    global sec
    for i in range(13, 2501):
        sec.append(7*sec[i-1] - 13*sec[i-2] + 10*sec[i-3] - 4*sec[i-4] + 5*sec[i-5] - 2*sec[i-6])

def ecuation_system():
    def print_ecuation(n):
        return str(sec[n-1]) + 'x + ' + str(sec[n-2]) + 'y + ' + str(sec[n-3]) + 'z + ' + \
            str(sec[n-4]) + 'u + ' + str(sec[n-5]) + 'v + ' + str(sec[n-6]) + 'w = ' + str(sec[n])

    def check(n, x, y, z, u, v, w):
        return sec[n-1]*x + sec[n-2]*y + sec[n-3]*z + sec[n-4]*u + sec[n-5]*v + sec[n-6]*w

    for ec in [print_ecuation(i) for i in range(7, 13)]:
        print(ec)

    for i in range(7, 16):
        print(i, sec[i], check(i, x = 7,y = -13,z = 10,u = -4,v = 5,w = -2))


if __name__ == '__main__':
    calc_all()
    for i in range(int(input())):
        print('Case #{}: {}'.format(i + 1, sec[int(input())] % (10 ** 9 + 7)))
