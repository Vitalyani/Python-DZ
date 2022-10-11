name_file = 'phone directory.txt'


def file_writing(data):

    with open(name_file, 'a', encoding='utf-8') as file:

        for key, value in data.items():
            file.write(f'{key} - {value}\n')
            if key != len(data) - 1:
                file.write('\n')


# def file_reading():
#     with open(name_file, 'r', encoding='utf-8') as file:
#         return file.read()

def file_reading():
    with open(name_file, 'r', encoding='utf-8') as file:
        lines = [_.rstrip('\n') for _ in file if not _.isspace()]
        return lines
