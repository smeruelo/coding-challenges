#!/usr/bin/env python
# https://www.codechef.com/WICP2002/problems/ENCOMS

from string import ascii_lowercase


def encode(s, n):
    def swap(s):
        to = n if n % 2 == 0 else n - 1
        x = [s[i+1] + s[i] for i in range(0, to, 2)]
        if n % 2 == 1:
            x.append(s[-1])
        return ''.join(x)

    def replace(s):
        d = dict(zip(ascii_lowercase, ascii_lowercase[::-1]))
        return ''.join([d[c] for c in s])

    return replace(swap(s))


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(encode(s, n))
