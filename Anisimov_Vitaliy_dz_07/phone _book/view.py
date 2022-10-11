def user_selection():
    user_menu = ('Импорт данных в файл CSV', 'Экспорт справочника из файла CSV',
                 'Импорт данных в файл XML', 'Экспорт справочника из файла XML',
                 'Импорт данных в файл TXT', 'Экспорт справочника из файла TXT')
    for i in enumerate(user_menu, 1):
        print(i[0], i[1])
    while True:
        try:
            number = int(input('Введите номер пункта меню: '))
            if 1 <= number <= 6:
                return number
            else:
                raise ValueError
        except ValueError:
            print('Функционал ограничен цифрами от 1 до 5. Введите номер пункта: ')


def user_data_entry():
    first_name = input('Введите Имя нового пользователя: ')
    last_name = input('Введите Фамилию нового пользователя: ')
    phone_number = input('Введите номер телефона нового пользователя: ')
    note = input('Введите описание/примечание нового пользователя: ')
    directory_entry = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number,
        'note': note
    }
    return directory_entry


def view_result(data):
    print(data)
