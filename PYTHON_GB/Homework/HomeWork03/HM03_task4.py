# Напишите программу, которая будет преобразовывать
#  десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Введите число: '))
a = number
my_list = []
while a > 0:
    num = a % 2
    my_list.append(str(num))
    a = a // 2
my_list.reverse()
num = int(''.join(my_list))
print(f'{number} -> {num}')