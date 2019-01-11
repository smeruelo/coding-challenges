#!/usr/bin/python3
# https://adventofcode.com/2017/day/1

if __name__ == '__main__':
    with open('01_inverse_captcha.input') as f:
        s = list(map(int, f.read()))

    # part 1
    print(sum([s[i] for i in range(len(s)) if s[i] == s[(i+1) % len(s)]]))

    # part 2
    print(sum([s[i] for i in range(len(s)) if s[i] == s[(i + len(s)//2) % len(s)]]))
