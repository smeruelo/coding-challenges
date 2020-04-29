from collections import defaultdict


for i in range(int(input())):
    players = defaultdict(int)
    for _ in range(int(input())):
        match = list(map(int, input().split()))
        winner = match[(match[2] + 1) % 2]
        players[winner] += 1
    player, points = max(players.items(), key=lambda kv: kv[1])
    print(f'Case #{i+1}: {player}')
