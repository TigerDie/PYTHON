# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет
# a = int(input('a = '))
# b = int(input('b = '))
# if a**2 == b or b**2 == a:
#     print(True)
# else:
#     print(False)

# a = int(input('a = '))
# b = int(input('b = '))
# if a**2 == b:
#     print(f'{a} quad of digit {b}')
# elif b**2 == a:
#     print(f'{b} quad of digit {a}')
# else:
#     print(False)

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

my_list = []
for i in range(5):
    number = (int(input('введите число: ')))
    my_list.append(number) 
    my_max = my_list[0]
for item in my_list:
    if my_max < item:
        my_max = item
print(f'Максимальное значение списка {my_max}')