# 4.	Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в
# файле file.txt в одной строке одно число.


with open('file.txt','r') as f:
    position_one = f.readline()
    position_two = f.readline()

#вариант со списком от -N до N:
# n = 5
# lst = []
# for i in range(-n, n + 1):
#     lst.append(i)

#вариант со списком N элементов, в котором элементы принимает значения из промежутка от -N до N:
from random import randint
n = 5
lst = []
for i in range(n):
    lst.append(randint(-n, n))

prod = lst[int(position_one)] * lst[int(position_two)]
print(lst)
print(f'Произведение значений индексов {int(position_one)} и {int(position_two)} равно {prod}')

