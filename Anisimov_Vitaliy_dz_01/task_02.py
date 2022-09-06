# 2.	Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result = 0
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            left_part = (not(x or y or z))
            right_part = (not x) and (not y) and (not z)
            result += 1
            print(f'{result}) ', x, y, z, left_part, right_part, left_part == right_part)
print('конец')

# Можно еще усложнить (не знаю зачем):
# result = 0
# for n in range(0, 8):
#      num = bin(n)
#      num = num.replace('b', '0')
#      X = int(num[-3])
#      Y = int(num[-2])
#      Z = int(num[-1])
#      left_part = not(X or Y or Z)
#      right_part = (not X) and (not Y) and (not Z)
#      if left_part == right_part:
#         result += 1
#      print(f'{result}) ',X, Y, Z, left_part, right_part, left_part == right_part)

