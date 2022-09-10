# 5.	Реализуйте алгоритм перемешивания списка.

from random import randint

list = [1, 2, 3, 4, 5]
print(f'Оригинальный список: {list}')

test_list = list[:]
for i in range(len(test_list)):
    x = randint(0, len(test_list) - 1)
    y = test_list[i]
    test_list[i] = test_list[x]
    test_list[x] = y
print(f'Перемешанный список: {test_list}')