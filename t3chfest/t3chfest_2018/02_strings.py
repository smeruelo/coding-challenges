#!/usr/bin/python3

# There are 3 possible operations on a string:
# - insert one character
# - delete one character
# - swap two characters
# Given two strings, if one of those operations would convert one string into the other, say which one
# If they're already equal, say 'nothing'.
# If conversion can't be made with one operation, say 'impossible'

def solution(S, T):
    if S == T:
        return "NOTHING"
    if len(T) == len(S) + 1:
        for i in range(len(T)):
            if T[0:i] + T[i+1:] == S:
                return 'INSERT {}'.format(T[i])
    if len(T) == len(S) - 1:
        for i in range(len(S)):
            if S[0:i] + S[i+1:] == T:
                return 'DELETE {}'.format(S[i])
    if len(T) == len(S):
        for i in range(len(S) - 1):
            if S[0:i] + S[i+1] + S[i] + S[i+2:] == T:
                return 'SWAP {} {}'.format(S[i], S[i+1])
    return "IMPOSSIBLE"
