def play(s1, s2):
    if s1 == s2:
        return '-'
    if s1 == 'R':
        return 'R' if s2 == 'S' else 'P'
    if s1 == 'S':
        return 'S' if s2 == 'P' else 'R'
    if s1 == 'P':
        return 'P' if s2 == 'R' else 'S'

for i in range(int(input())):
    s1, s2 = input().split()
    print(f'Case #{i+1}: {play(s1, s2)}')
