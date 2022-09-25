# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все
# конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


# Первый ход определяется жеребьёвкой.

from random import randint
# sweets = int(input('Введите кол-во конфет: '))

def input_count_sweets(gamers): # ввод количества конфет от 1 до 29
    sweets = int(input(f'{gamers}, Взять конфет (1-28): '))
    while 1 > sweets or sweets > 28:
        sweets = int(input(f'{gamers}, Можно только от 1 до 28. Повтори ввод: '))
    return sweets

def input_count_sweets_bot(candies): # БОТ определеяет количества конфет от 1 до 29 для выйгрыша
    count = candies % 29
    if 1 > count or count > 28:
        count = randint(1, 29)
    return count

# Выбор с кем играть: с игроком или ботом:
game_pvp_or_pvb = int(input('Введите "0", если хотите играть с игроком или "1", если с ботом: '))
while not game_pvp_or_pvb == 0 and not game_pvp_or_pvb == 1:
    game_pvp_or_pvb = int(input('Можно использовать только цифры 0 или 1. Повтори ввод: '))

candies = 90
gamers_2 = {1: 'Бот', 0: 'Игрок 2'}
gamers = {0: 'Игрок 1', 1: gamers_2[game_pvp_or_pvb]}

lottery = randint(0, 1) # Первый ход определяется жеребьёвкой.
print(f'Первым ходит: {gamers[lottery]}')
if game_pvp_or_pvb == 0: # Если играют ирок против игрока
    while candies > 28:
        if not lottery:
            k = input_count_sweets(gamers[lottery])
            candies -= k
            lottery = True
            print(f'    Ходил Игрок 1. Осталось конфет: {candies}')
        else:
            k = input_count_sweets(gamers[lottery])
            candies -= k
            lottery = False
            print(f'    Ходил Игрок 2. Осталось конфет: {candies}')
    if not lottery:
        print(f'Выйграл Игрок 1')
    else:
        print(f'Выйграл Игрок 2')
else: # Если играют ирок против бота
    while candies > 28:
        if not lottery:
            k = input_count_sweets(gamers[lottery])
            candies -= k
            lottery = True
            print(f'    Ходил Игрок 1. Осталось конфет: {candies}')
        else:
            k = input_count_sweets_bot(candies)
            candies -= k
            lottery = False
            print(f'    Ходил Бот. Он взял {k}. Осталось конфет: {candies}')
    if lottery:
        print(f'Выйграл Бот')
    else:
        print(f'Выйграл Игрок 1')
