#!/usr/bin/pypy3

N = 51
memo = []
for _ in range(N):
    memo.append([[None] * N for _ in range(N)])

def rectangles(n):
    global memo

    def aux(top, mid, bot):
        if top == 1 or mid == 1 or bot == 1:
            return 1
        if memo[top][mid][bot]:
            return memo[top][mid][bot]
        if memo[bot][mid][top]:
            return memo[bot][mid][top]
        new_top = min(top, mid) - 1
        new_mid = min(top, mid, bot) - 1
        new_bot = min(bot, mid) - 1
        count = 1
        for m in range(new_mid, 0, -1):
            for t in range(new_top, 0, -1):
                for b in range(new_bot, 0, -1):
                    count = (count + aux(t, m, b)) % (10 ** 9 + 7)
        memo[top][mid][bot] = count
        return count
    return aux(n, n, n)


if __name__ == '__main__':
    for i in range(int(input())):
        print('Case #{}: {}'.format(i + 1, rectangles(int(input()))))
