#!/usr/bin/python3

from sympy.ntheory.modular import crt
# from functools import reduce

# def inv_mod_m(a, m):
#     if m == 1:
#         return 0
#     for i in range(1, m):
#         if (i * a) % m == 1:
#             return i
#     return None

def sync_doors(doors):
    # Chinese remainder theorem
    m = list(map(lambda x: x[0], doors))
    a = list(map(lambda x, y: x - y,
                 map(lambda x: x[0] - x[1] if x[1] != 0 else 0, doors),
                 range(len(doors))))
    # M = reduce(lambda x, y: x * y, m, 1)
    # x = list(map(lambda x: M // x, m))
    # inverses = list(map(lambda x, y: inv_mod_m(x, y), x, m))
    # if any(map(lambda x, y: x == None and y != 0, inverses, a)):
    #     return 'NEVER'
    # else:
    #     return sum(map(lambda x, y, z: x * y * z, a, x, inverses)) % M
    chinese = crt(m, a)
    return chinese[0] if chinese else 'NEVER'

if __name__ == '__main__':
    for i in range(int(input())):
        doors = [list(map(int, input().split())) for _ in range(int(input()))]
        print('Case #{}: {}'.format(i + 1, sync_doors(doors)))
