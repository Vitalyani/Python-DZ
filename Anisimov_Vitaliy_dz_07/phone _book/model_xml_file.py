name_file = 'phone directory.xml'


def file_recording(data):
    xml = '<xml>\n'
    xml += '   <first_name units = "Имя">{}</first_name>\n'\
        .format(data['first_name'])
    xml += '   <last_name units = "Фамилия">{}</last_name>\n' \
        .format(data['last_name'])
    xml += '   <phone_number units = "№ телефона">{}</phone_number>\n' \
        .format(data['phone_number'])
    xml += '   <note units = "Примечание">{}</note>\n' \
        .format(data['note'])
    xml += '</xml>\n'
    with open(name_file, 'a', encoding='utf-8') as file:
        file.writelines(xml)


def file_reading():
    with open(name_file, 'r', encoding='utf-8') as file:
        return file.read()
