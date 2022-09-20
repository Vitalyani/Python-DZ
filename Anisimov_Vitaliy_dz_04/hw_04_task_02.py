# 2.	Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.

n = int(input('Введите натуральное число: '))
num = n # эта переменная нужна только для вывода
lst = []
simple_num = 2
while n > 1:
    if n % simple_num == 0:
        lst.append(simple_num)
        n = n / simple_num
    else:
        simple_num += 1
print(f'{lst} - список простых множитеей числа {num}')