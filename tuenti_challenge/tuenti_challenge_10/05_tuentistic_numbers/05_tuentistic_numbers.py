def tuentify(n):
    tuentis = n // 20
    rest = n % 20
    return tuentis if rest <= tuentis * 9 else None

for i in range(int(input())):
    n = int(input())
    result = tuentify(n)
    if result:
        print(f'Case #{i+1}: {result}')
    else:
        print(f'Case #{i+1}: IMPOSSIBLE')
