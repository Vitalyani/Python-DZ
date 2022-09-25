# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Если просто принять текст и строку "абв":
# str_text = 'Привет забвение сабвуфер котёнок абв Зимбабве'
# content = "абв"
# result = [itr for itr in str_text.split() if content not in itr]
# print(' '.join(result))
# Или:
# res = list(filter(lambda x: content not in x, str_text.split()))
# print(' '.join(res))


# Если нужно из файла считать:
with open('file_hw_05_task_01_read.txt', 'r', encoding='utf-8') as f:
    lst_text = [i for i in f.readline().split()]
    content = f.readline(2)
    result = ' '.join(list(filter(lambda x: content not in x, [i for i in lst_text])))
    # print(result)

with open('file_hw_05_task_01_write.txt', 'w') as f:
    f.write(result)


with open('file_hw_05_task_01_write.txt', 'r') as f:
    print(f.readline())