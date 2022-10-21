# import sqlite3


def get_contacts(cursor):
    cursor.execute("select * from users")
    results = cursor.fetchall()
    return results


def get_contact(item, cursor):
    cursor.execute(f'select * from users where last_name like "%{item}%"'
                   f'or first_name like "%{item}%"')
    results = cursor.fetchall()
    if results:
        return results
    return 'Контакт не найден'


def add_contact(data, connection, cursor):
    first_name, last_name, phone_number, held_post, note = data
    cursor.execute(f'insert into users (first_name, last_name, phone_number, held_post, note) '
                   f'values ("{first_name}", "{last_name}", "{phone_number}", "{held_post}", "{note}")')
    connection.commit()


def delete(id, connection, cursor):
    try:
        cursor.execute(f'delete from users where id={id}')
        connection.commit()
        return 'Контакт успешно удален'
    except:
        return 'Контакт не найден.'