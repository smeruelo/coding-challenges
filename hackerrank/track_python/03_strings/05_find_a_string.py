#!/usr/bin/python2
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    def aux(begin, count):
        pos = string.find(sub_string, begin)
        if pos == -1:
            return count
        else:
            return aux(pos + 1, count + 1)

    return aux(0, 0)


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    print count_substring(string, sub_string)
