#!/usr/bin/python3
# https://adventofcode.com/2018/day/14

def new_recipes(old1, old2):
    return list(map(int, list(str(old1 + old2))))

def create_recipes_1(n):
# creates n recipes
    board = [3, 7]
    elf1 = 0
    elf2 = 1
    while len(board) < n + 10:
        board.extend(new_recipes(board[elf1], board[elf2]))
        steps1 = 1 + board[elf1]
        steps2 = 1 + board[elf2]
        elf1 = (elf1 + steps1) % len(board)
        elf2 = (elf2 + steps2) % len(board)
    return board

def create_recipes_2(n):
# creates recipes until last ones are the digits in n
    board = [3, 7]
    elf1 = 0
    elf2 = 1
    while True:
        board.extend(new_recipes(board[elf1], board[elf2]))
        lasts = list(map(str, board[-(len(n)):]))
        if ''.join(lasts) == n:
            return board
        lasts = list(map(str, board[-(len(n) + 1):-1]))
        if ''.join(lasts) == n:
            return board[:-1]
        steps1 = 1 + board[elf1]
        steps2 = 1 + board[elf2]
        elf1 = (elf1 + steps1) % len(board)
        elf2 = (elf2 + steps2) % len(board)


if __name__ == '__main__':
    with open('14_chocolate_charts.input') as f:
        n_str = f.read()
        n = int(n_str)

    # part 1
    recipes = create_recipes_1(n)
    print(''.join(map(str, recipes[n:n+10])))

    # part 2
    recipes = create_recipes_2(n_str)
    print(len(recipes) - len(n_str))
