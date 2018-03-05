#!/usr/bin/python3

import random
from collections import Counter

def solution(K, A):
    dict_a = Counter(A)
    count = 0
    for i in dict_a:
        if (K - i) in dict_a:
            count += dict_a[i] * dict_a[K - i]
    return count


if __name__ == '__main__':
    # Some tests
    print(solution(6, [1, 8, -3, 0, 1, 3, -2, 4, 5]), 7)
    print(solution(random.randint(-2147483648, 2147483647),
                   [random.randint(-2147483648, 2147483647) for _ in range(40000)]))
    print(solution(100, [80, 80, 30, 50, 100, 0, 70, 80, 20]))
    r = [random.randint(-2147483648, 2147483647) for _ in range(40000)]
    a = r[0:4000] + [80] + \
        r[4000:8000] + [80] + \
        r[8000:12000] + [30] + \
        r[12000:16000] + [50] + \
        r[16000:20000] + [100] + \
        r[20000:24000] + [0] + \
        r[24000:28000] + [70] + \
        r[28000:32000] + [80] + \
        r[32000:36000] + [20] + r[36000:]
    print(solution(100, a))
    print(solution(4, []))
