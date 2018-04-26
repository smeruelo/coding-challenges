#!/usr/bin/python2

import socket

def recover(parts):
    def aux(s1, s2, used, p, j):
        s1p = s1 + p
        usedp = used + [j]
        if len(s1p) == len(s2):
            return usedp
        elif len(s1p) > len(s2):
            ssort = s2
            slong = s1p
        else:
            ssort = s1p
            slong = s2
        prefix = slong[len(ssort):]
        for i, p in enumerate(parts):
            if i not in usedp:
                result = None
                if p in prefix or prefix in p:
                    result = aux(ssort, slong, usedp, p, i)
                if result:
                    return result
        return None

    for i1, p1 in enumerate(parts):
        for i, p2 in enumerate(parts[i1+1:]):
            i2 = i + i1 + 1
            result = None
            if p1 in p2 or p2 in p1:
                result = aux('', p1, [i1], p2, i2)
            if result:
                return(sorted(map(lambda x: x + 1, result)))


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('52.49.91.111', 3241))
    f = s.makefile(mode='w')
    f.readline()
    f.readline()
    # f.write('TEST\n'); f.flush()
    f.write('SUBMIT\n'); f.flush()
    for _ in range(20):
        print(f.readline())
        parts = f.readline().split()
        print(parts)
        f.write(','.join(map(str, recover(parts))) + '\n'); f.flush()
    print(f.readline())
    f.close()
    s.close()
