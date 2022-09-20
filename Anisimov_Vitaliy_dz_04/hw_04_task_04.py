# 4.	Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input("Введите натуральную степень k = "))
list_random_values = [random.randint(0, 100) for i in range(k + 1)]
print(list_random_values)

polynomial = ''
if len(list_random_values) < 1:
    polynomial = 'x = 0'
else:
    for i in range(len(list_random_values)):
        if i != len(list_random_values) - 1 and list_random_values[i] != 0 and i != len(list_random_values) - 2:
            polynomial += f'{list_random_values[i]}x^{len(list_random_values) - i - 1}'
            if list_random_values[i + 1] != 0:
                polynomial += ' + '
        elif i == len(list_random_values) - 2 and list_random_values[i] != 0:
            polynomial += f'{list_random_values[i]}x'
            if list_random_values[i + 1] != 0:
                polynomial += ' + '
        elif i == len(list_random_values) - 1 and list_random_values[i] != 0:
            polynomial += f'{list_random_values[i]} = 0'
        elif i == len(list_random_values) - 1 and list_random_values[i] == 0:
            polynomial += ' = 0'
print(polynomial)

with open('file_hw_04_task_04.txt', 'w') as data:
    data.write(polynomial)
