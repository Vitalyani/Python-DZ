# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# запишем какойнибудь многочлен в файл file_hw_04_task_05.txt:
with open('file_hw_04_task_05.txt', 'w') as data:
    data.write('4x^3 + 11x^2 + 5x + 8 = 0')


def read_to_file(file):
    with open(file, 'r') as data:
        polynomial = data.readline()
    return polynomial


def polynomial_str_to_dict(polynomial):
    list_of_poly_1 = polynomial.split()
    # print(list_of_poly_1)
    polynomial_dict = {}
    for i in list_of_poly_1:
        if 'x^' in i:
            value, key = i.split('x^')
            polynomial_dict['x^' + key] = int(value)
        elif 'x' in i:
            value, key = i.split('x')
            polynomial_dict['x^' + '1'] = int(value)
        elif i.isdigit():
            # print(i)
            value, key = i, 'x^0'
            polynomial_dict['x^0'] = int(value)
        elif i == '=':
            break
    return polynomial_dict


file1 = read_to_file('file_hw_04_task_04.txt')
file2 = read_to_file('file_hw_04_task_05.txt')
print(f'1-й многочлен: {file1} \n'
      f'2-й многочлен: {file2}')


polynomial_dict1 = polynomial_str_to_dict(file1)
polynomial_dict2 = polynomial_str_to_dict(file2)
print(f'словарь 1-го многочлена: {polynomial_dict1} \n'
      f'словарь 2-го многочлена: {polynomial_dict2}')

# сложим значения словарей, а потом выведем
sum_polynomial_dict = {}
for key in polynomial_dict1.keys():
    if key in polynomial_dict2.keys():
        sum_polynomial_dict[key] = polynomial_dict1[key] + polynomial_dict2[key]
print(sum_polynomial_dict)

# преобразуем значения словаря в список
sum_polynomial_list = list(sum_polynomial_dict.values())
print(sum_polynomial_list)

with open('file_hw_04_task_05_sum.txt', 'w') as data:
    data.write(str(sum_polynomial_list))