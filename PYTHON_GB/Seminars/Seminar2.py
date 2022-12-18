# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# number = int (input('Введите целое число '))

# for degree in range(number):
#     print ((-3)**degree, end= ' ')

# 2. напишите программу, которая будет на вход принимать число
# N и выводить числа от -N до N

# number = int(input('Введите число: '))

# for i in range(-number, number+1):
#     if i == number:
#         print(i)
#     else:
#         print(i, end = ', ')

# number = int(input('Введите число: '))

# my_list = []

# for i in range(-number, number + abs(number)//number, abs(number)//number):
#     my_list.append(i)

# print(*my_list, sep = ', ')

# 3. Напишите программу, которая будет принимать на 
# вход дробь и показывать первую цифру 
# дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3

# number = float(input('Введите дробное число: '))

# value = number % 1
# if value == 0:
#     print('Нет!')
# else:
#     print(f'Первая цифра дробной части: {int((value*10) % 10)}')

# a = float(input('Введите число: '))
# my_list = str(a)
# b = my_list.find('.')
# print(my_list[b+1])

# n = float(input('Введите число'))
# if(int(n) == n):
#     print('Нет!')
# else:
#     print(int(abs(n)*10)%10)

# number = float(input('Введите дробное число: '))
# if number != int(number):
#     print(f'Первая цифра дробной части числа {number}'
#           f' -> {int(abs(number)*10)%10}')
# else:
#     print(f' У числа {int(number)} нет дробной части')

# number = float(input('Введите дробное число: '))
# number = number.split('.')
# if len(number)>1:
#     print(number[1][0])
# else:
#     print('Число целое')

# from decimal import Decimal

# numberD = Decimal('0.567899')
# number = 0.567899
# numberD*= 100
# print(number*10)
# print(numberD)

# from random import randint as RI
# print(RI(0,100))
# print(RI(0,100))
# print(RI(0,100))
# print(RI(0,100))
# print(RI(0,100))


# import random
# random.randint(a, b)

# from random import randint
# randint(a, b)

# from random import randint as RI
# RI(a, b)