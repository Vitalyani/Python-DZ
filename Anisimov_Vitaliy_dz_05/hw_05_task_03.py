# 3.	Создайте программу для игры в "Крестики-нолики".

playing_field = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 9]

winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],
                        [0, 4, 8], [2, 4, 6]]


def print_playing_field():
    print(playing_field[0], end=' ')
    print(playing_field[1], end=' ')
    print(playing_field[2])

    print(playing_field[3], end=' ')
    print(playing_field[4], end=' ')
    print(playing_field[5])

    print(playing_field[6], end=' ')
    print(playing_field[7], end=' ')
    print(playing_field[8])


def step_playing(step, symbol):
    x = playing_field.index(step)
    playing_field[x] = symbol

def result():
    win = ""
    for i in winning_combinations:
        if playing_field[i[0]] == "X" and playing_field[i[1]] == "X" and playing_field[i[2]] == "X":
            win = "X"
        if playing_field[i[0]] == "O" and playing_field[i[1]] == "O" and playing_field[i[2]] == "O":
            win = "O"
    return win


game_over = 0
player = 1

while not game_over:
    print_playing_field()
    if player:
        symbol = "X"
        step = int(input('Ход игрока 1: '))
    else:
        symbol = "O"
        step = int(input('Ход игрока 2: '))
    step_playing(step, symbol)
    win = result()
    if win != "":
        game_over = True
    else:
        game_over = False
    player = not(player)

print_playing_field()
print('Победил', win)

