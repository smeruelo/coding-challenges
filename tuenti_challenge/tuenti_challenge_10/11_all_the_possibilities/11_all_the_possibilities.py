def possibilities(x, m):
    valid = list(filter(lambda n: n not in m, range(1, x)))
    count = [0] * 101
    count[0] = 1
    for c in valid:
        for i in range(1, x+1):
            if i - c >= 0:
                count[i] += count[i-c]
    return count[x]


for i in range(int(input())):
    x, *m = map(int, input().split())
    result = possibilities(x, m)
    print(f'Case #{i+1}: {result}')
