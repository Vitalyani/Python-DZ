# 3.	Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [float(i) for i in input('Введите список из вещественных чисел: ').split(', ')]
# lst = [1.1, 1.2, 3.1, 5, 10.01]
print(lst)
lst_decimal_point = [x - int(x) for x in lst]
print(f'разница между максимальным и минимальным значением дробной '
      f'части элементов => {max(lst_decimal_point) - min(lst_decimal_point)}')
