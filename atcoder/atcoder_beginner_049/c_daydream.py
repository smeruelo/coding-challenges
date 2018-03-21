#!/usr/bin/python3
# https://abc049.contest.atcoder.jp/tasks/arc065_a

s = input()
index = 0
result = 'YES'
while index < len(s):
    if s.startswith('dreameraser', index):
        index += 11
    elif s.startswith('dreamerase', index):
        index += 10
    elif s.startswith('dreamer', index):
        index += 7
    elif s.startswith('eraser', index):
        index += 6
    elif s.startswith('dream', index) or s.startswith('erase', index):
        index += 5
    else:
        result = 'NO'
        break
print(result)
