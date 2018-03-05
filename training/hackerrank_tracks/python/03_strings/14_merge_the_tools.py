#!/usr/bin/python2
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(s, k):
    def uniques(t):
        u = ""
        for c in t:
            if c not in u:
                u += c
        return u

    t = [s[i:i+k] for i in range(0, len(s), k)]
    u = map(uniques, t)
    for i in u:
        print i

if __name__ == '__main__':
    s, k = raw_input(), int(raw_input())
    merge_the_tools(s, k)
