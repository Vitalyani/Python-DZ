# 1.	Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst = [int(i) for i in input().split(', ')]
# или
# lst = [2, 3, 5, 9, 3]
# sum_uneven_i = 0
# for i in range(len(lst)):
#     if i % 2 != 0:
#         sum_uneven_i += lst[i]
# print(sum_uneven_i)

# при помощи list comprehension
lst = [2, 3, 5, 9, 3]
lst_uneven_i = [lst[i] for i in range(len(lst)) if i % 2 != 0]
print(sum(lst_uneven_i))
