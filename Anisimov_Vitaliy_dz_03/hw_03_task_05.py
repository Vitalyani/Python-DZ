# 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для
# отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число k: '))


def get_negafibonacci(k):
    fibonacci_nums = []
    a, b = 1, 1
    for i in range(k):
        fibonacci_nums.append(a) # сначала заполняем список вправо
        a, b = b, a + b
    a, b = 0, 1
    for i in range(k + 1):
        fibonacci_nums.insert(0, a) # потом заполняем список влево
        a, b = b, a - b
    return fibonacci_nums


print(f"Cписок чисел негаибоначчи числа {k}:")
print(get_negafibonacci(k))

