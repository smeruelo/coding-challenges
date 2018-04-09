#!/usr/bin/python3
# https://abc066.contest.atcoder.jp/tasks/abc066_b

def even(s):
    return s[0:len(s)//2] == s[(len(s)//2):]

def longest_even(s):
    for i in range(1, len(s)+1):
        if even(s[0:len(s)-i]):
            return(len(s)-i)


if __name__ == '__main__':
    s = input()
    print(longest_even(s))

