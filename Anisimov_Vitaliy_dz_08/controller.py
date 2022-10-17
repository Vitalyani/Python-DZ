import view
import model


def selection_user_manu():
    number_user_menu = view.main_menu()
    if number_user_menu == 1: # вывести весь список сотрудников
        view.view_all_users(model.show_all_users())
    elif number_user_menu == 2: # поиск сотрудников по значению
        view.view_user(model.looking_for())
    elif number_user_menu == 3: # добавление сотрудника в БД
        model.add_new_user()
    elif number_user_menu == 4: # удаление сотрудника из БД
        model.delete_user()
    elif number_user_menu == 5: # Обновить запись сотрудника
        model.update_date_user()
    elif number_user_menu == 6: # Экспорт БД сотрудников в csv
        model.file_csv_write(model.show_all_users())
    else:
        view.oops()