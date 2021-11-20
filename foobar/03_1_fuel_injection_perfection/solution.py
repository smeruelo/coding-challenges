# def operations(n):
#     if n < 4:
#         return n - 1

#     if n % 2 == 0:
#         return 1 + operations(n / 2)

#     if n % 4 == 1:
#         return 1 + operations(n - 1)

#     return 1 + operations(n + 1)


def solution(s):
    # return operations(int(s)
    # Had to do an iterative solution cause python's recursion sucks

    n = int(s)
    count = 0

    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        elif n == 3 or n % 4 == 1:
            n = n - 1
        else:
            n = n + 1

    return count
