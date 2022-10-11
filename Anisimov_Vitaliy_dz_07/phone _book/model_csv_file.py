import csv
name_file = 'phone directory.csv'


def file_recording(data):
    with open(name_file, mode='a', encoding='utf-8') as w_file:
        directory_entry = ['Имя', 'Фамилия', 'Номер телефона', 'Описание']
        file_writer = csv.DictWriter(w_file, delimiter=';', lineterminator='\r',
                                     fieldnames=directory_entry)
        # file_writer.writeheader()
        file_writer.writerow({'Имя': data['first_name'],
                              'Фамилия': data['last_name'],
                              'Номер телефона': data['phone_number'],
                              'Описание': data['note']})


def file_reading():
    list_from_file = []
    with open(name_file, 'r', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=';')
        for row in file_reader:
            list_from_file.append(row)
    return list_from_file
