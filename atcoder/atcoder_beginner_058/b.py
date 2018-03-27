#!/usr/bin/python3
# https://abc058.contest.atcoder.jp/tasks/abc058_b

odd = input()
even = input()
password = ''
i = 0
while i < len(even):
    password += odd[i] + even[i]
    i += 1
if i < len(odd):
    password += odd[i]
print(password)
