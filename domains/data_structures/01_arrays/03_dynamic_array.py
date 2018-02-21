#!/usr/bin/python2
# https://www.hackerrank.com/challenges/dynamic-array/problem

if __name__ == '__main__':
    n, q = map(int, raw_input().split())
    s = [[] for i in range(n)]
    last_answer = 0
    for _ in xrange(q):
        query_type, query_arg1, query_arg2 = map(int, raw_input().split())
        seq = (query_arg1 ^ last_answer) % n
        if query_type == 1:
            s[seq].append(query_arg2)
        else:
            last_answer = s[seq][query_arg2 % len(s[seq])]
            print last_answer
