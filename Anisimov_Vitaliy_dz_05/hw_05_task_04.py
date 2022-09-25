# 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('file_hw_05_task_04_read.txt', 'r') as f:
    str_code = f.readline()

def rle_coding_text(txt):
    count = 1
    result = ''
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            count += 1
        else:
            result = result + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt) - 2] != txt[-1]):
        result = result + str(count) + txt[-1]
    return result

def rle_decoding_text(txt):
    number = ''
    result = ''
    for i in range(len(txt)):
        if txt[i].isdigit():
            number += txt[i]
        else:
            result = result + txt[i] * int(number)
            number = ''
    return result

# str_code = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(f"Текст после кодировки: {rle_coding_text(str_code)}")
# print(f"Текст после декодирования: {rle_decoding_text('12W1B12W3B24W1B14W')}")
print(f"Текст после декодирования: {rle_decoding_text(rle_coding_text(str_code))}")

with open('file_hw_05_task_04_write.txt', 'w') as f:
    f.write(rle_decoding_text(rle_coding_text(str_code)))