# https://www.codechef.com/WICP1901/problems/THESAV


def feeded(drop):
    feedable = 0
    for char in drop:
        if char == '*':
            feedable = 2
        elif feedable > 0:
            feedable -= 1
        else:
            return 'NO'
    return 'YES'


def readln():
    while True:
        line = input().strip()
        if line:
            return line


for _ in range(int(readln())):
    drop = readln()
    print(feeded(drop))
