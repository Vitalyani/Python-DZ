import sqlite3
import view
import csv
name_file = 'Company_database_file.csv'
path_db = '../Company_database.db'
connection = sqlite3.connect(path_db)
cursor = connection.cursor()


def show_all_users(): # показать всех сотрудников
    cursor.execute("select * from users")
    results = cursor.fetchall()
    connection.close()
    return results


def number_looking_for(): # выбор значения из словаря для поиска по значению
    num_view_user_menu = view.view_looking_for_user_menu()
    num_looking_for_user = {0: 'id', 1: 'first_name', 2: 'last_name', 3: 'phone_number', 4: 'held_post', 5: 'note'}
    value_num_looking_for = num_looking_for_user[num_view_user_menu]
    return value_num_looking_for


def looking_for(): # поиск по значению
    # num_view_user_menu = view.view_looking_for_user_menu()
    # num_looking_for_user = {0: 'id', 1: 'first_name', 2: 'last_name', 3: 'phone_number', 4: 'held_post', 5: 'note'}
    # num_looking_for = num_looking_for_user[num_view_user_menu]
    num_looking_for = number_looking_for()
    text_looking_for = view.text_to_search()
    cursor.execute(f'select * from users where {num_looking_for} like "%{text_looking_for}%"')
    results = cursor.fetchall()
    connection.close()
    return results


def add_new_user(): # Добавление сотрудника
    new_user = view.add_new_user()
    first_name = new_user[0]
    last_name = new_user[1]
    phone_number = new_user[2]
    held_post = new_user[3]
    note = new_user[4]
    cursor.execute(f'insert into users(first_name, last_name, phone_number,'
                   f'held_post, note) '
                   f'values ("{first_name}", "{last_name}", "{phone_number}", '
                   f'"{held_post}", "{note}")')
    connection.commit()
    connection.close()


def delete_user(): # Удалить сотрудника
    id_delete_user = view.delete_user()
    cursor.execute(f'delete from users where id={id_delete_user}')
    connection.commit()
    connection.close()


def view_delete_user(): # показать удаляемого сотрудника
    id_delete_user = view.delete_user()
    cursor.execute(f'select * from users where id={id_delete_user}')
    results = cursor.fetchall()
    connection.close()
    return results


def update_date_user(): # Обновить запись сотрудника
    id_update_user = view.update_user()
    num_looking_for = number_looking_for()
    text = view.text_to_search()
    cursor.execute(f'update users set {num_looking_for}="{text}" where id={id_update_user}')
    connection.commit()
    connection.close()


def file_csv_write(data):
    with open(name_file, mode='w', encoding='utf-8') as w_file:
        directory_entry = ['id', 'Имя', 'Фамилия', 'Номер телефона', 'Должность', 'Описание']
        file_writer = csv.DictWriter(w_file, delimiter=';', lineterminator='\r',
                                     fieldnames=directory_entry)
        file_writer.writeheader()
        for itr in data:
            file_writer.writerow({'id': itr[0],
                                  'Имя': itr[1],
                                  'Фамилия': itr[2],
                                  'Номер телефона': itr[3],
                                  'Должность': itr[4],
                                  'Описание': itr[5]})
