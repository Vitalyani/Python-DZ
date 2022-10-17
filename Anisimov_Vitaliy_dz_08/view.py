# def main_menu():
#     menu = ['Показать всех сотрудников', 'Поиск сотрудника(-ов) по ...', 'Добавить сотрудника',
#             'Удалить сотрудника', 'Внести изменения в существующую запись', 'Экспорт справочника из БД в файл csv']
#     for item in enumerate(menu, 1):
#         print(*item)
#     num = int(input('\nВведите номер пункта меню для продолжения: '))
#     return num
def main_menu():
    menu = ['Показать всех сотрудников', 'Поиск сотрудника(-ов) по ...', 'Добавить сотрудника',
            'Удалить сотрудника', 'Внести изменения в существующую запись', 'Экспорт справочника из БД в файл csv']
    for item in enumerate(menu, 1):
        print(*item)
    try:
        num = int(input('\nВведите номер пункта меню для продолжения: '))
        if int(num):
            return num
        else:
            raise ValueError
    except ValueError:
        print('Функционал ограничен лишь цифрами.')


def view_all_users(data):
    for row in data:
        print(row)


def view_user(data):
    print(*data)


def view_looking_for_user_menu():
    menu = ['...имени', '...фамилии', '...номеру телефона',
            '...должности', '...значению поля "описание"']
    for item in enumerate(menu, 1):
        print(*item)
    try:
        num = int(input('\nВыберите пункт меню для продолжения: '))
        if int(num):
            return num
        else:
            raise ValueError
    except ValueError:
        print('Функционал ограничен лишь цифрами.')


def text_to_search():
    text = input('Введите текст, что нужно найти/обновить: ')
    return text


def add_new_user():
    first_name = input('Введите Имя нового пользователя: ')
    last_name = input('Введите Фамилию нового пользователя: ')
    phone_number = input('Введите номер телефона нового пользователя: ')
    held_post = input('Введите должность специалиста: ')
    note = input('Введите описание/примечание нового пользователя: ')
    new_user = [first_name, last_name, phone_number, held_post, note]
    return new_user


def delete_user():
    id_user = input('Введите id сотрудника, которого необходимо удалить: ')
    return id_user


def update_user():
    id_user = input('Введите id сотрудника, данные которого необходимо обновить: ')
    print('\nОбновить данные сотрудника по')
    return id_user


def oops():
    print('OOOOPS!'
          '\nЧто-то пошло не так')
