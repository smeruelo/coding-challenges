#!/usr/bin/python3
# https://abc043.contest.atcoder.jp/tasks/abc043_b

keystrokes = input()
word = []
for k in keystrokes:
    if k == '0' or k == '1':
        word.append(k)
    elif word:
        word.pop()
print(''.join(word))
